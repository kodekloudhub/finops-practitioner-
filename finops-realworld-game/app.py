import streamlit as st
import random
from typing import List, Dict, Tuple
import pandas as pd
from streamlit_sortables import sort_items

# Page configuration
st.set_page_config(
    page_title="Azure Cost Optimization Puzzle",
    page_icon="💰",
    layout="centered"
)

# Define colors for each step (7 distinct colors)
STEP_COLORS = [
    "#3B82F6",  # Blue
    "#8B5CF6",  # Purple
    "#EC4899",  # Pink
    "#F59E0B",  # Orange
    "#10B981",  # Emerald
    "#06B6D4",  # Cyan
    "#6366F1",  # Indigo
]

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
    }
    .scenario-box {
        background-color: #E3F2FD;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    /* Style for sortable items to look like colored containers */
    div[data-testid="sortable-container"] > div {
        background-color: #f8f9fa;
        border-radius: 8px;
        margin: 4px 0;
        padding: 2px;
    }
    div[data-testid="sortable-container"] > div > div {
        padding: 16px 20px !important;
        border-radius: 8px;
        color: white !important;
        font-weight: 500;
        cursor: move;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    div[data-testid="sortable-container"] > div:nth-child(1) > div { background-color: #3B82F6; }
    div[data-testid="sortable-container"] > div:nth-child(2) > div { background-color: #8B5CF6; }
    div[data-testid="sortable-container"] > div:nth-child(3) > div { background-color: #EC4899; }
    div[data-testid="sortable-container"] > div:nth-child(4) > div { background-color: #F59E0B; }
    div[data-testid="sortable-container"] > div:nth-child(5) > div { background-color: #10B981; }
    div[data-testid="sortable-container"] > div:nth-child(6) > div { background-color: #06B6D4; }
    div[data-testid="sortable-container"] > div:nth-child(7) > div { background-color: #6366F1; }
    
    div[data-testid="sortable-container"] > div > div:hover {
        transform: translateX(8px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Define the correct order of steps
CORRECT_STEPS = [
    "Gather Data: Review current Azure bills and usage reports to understand where costs are coming from.",
    "Identify Cost Drivers: Analyze the data to pinpoint the services and resources driving the high costs.",
    "Set Budgets and Alerts: Establish budgets for different departments or projects and set up alerts for when costs approach limits.",
    "Optimize Resources: Rightsize over-provisioned resources, delete unused ones, and switch to cost-effective alternatives.",
    "Implement Reservations and Savings Plans: Purchase reserved instances or savings plans for predictable workloads.",
    "Enforce Tagging and Governance: Mandate resource tagging for better cost allocation and implement policies to prevent wasteful spending.",
    "Monitor and Iterate: Continuously monitor costs, review optimizations, and adjust strategies as needed."
]

# Explanations for why each step comes in its position
STEP_EXPLANATIONS = {
    0: "You must first gather data to understand the current state before taking any action.",
    1: "After gathering data, you need to analyze it to identify what's causing the high costs.",
    2: "Once you know the cost drivers, set budgets and alerts to prevent future overspending.",
    3: "With budgets in place, optimize existing resources to achieve immediate cost savings.",
    4: "After optimization, implement long-term savings through reservations for predictable workloads.",
    5: "Establish governance to ensure ongoing cost control and proper resource allocation.",
    6: "Finally, continuously monitor to ensure optimizations are working and adjust as needed."
}

def initialize_session_state():
    """Initialize session state variables"""
    if 'jumbled_steps' not in st.session_state:
        st.session_state.jumbled_steps = CORRECT_STEPS.copy()
        random.shuffle(st.session_state.jumbled_steps)
    
    if 'user_order' not in st.session_state:
        st.session_state.user_order = st.session_state.jumbled_steps.copy()
    
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    
    if 'show_correct' not in st.session_state:
        st.session_state.show_correct = False
    
    # Create a mapping of steps to their original colors
    if 'step_colors' not in st.session_state:
        st.session_state.step_colors = {step: STEP_COLORS[i] for i, step in enumerate(CORRECT_STEPS)}

def reset_game():
    """Reset the game state"""
    st.session_state.jumbled_steps = CORRECT_STEPS.copy()
    random.shuffle(st.session_state.jumbled_steps)
    st.session_state.user_order = st.session_state.jumbled_steps.copy()
    st.session_state.submitted = False
    st.session_state.show_correct = False

def get_step_title(step: str) -> str:
    """Extract the title from a step description"""
    return step.split(":")[0]

def get_step_description(step: str) -> str:
    """Extract the description from a step"""
    return step.split(": ", 1)[1] if ": " in step else ""

def validate_order(user_order: List[str]) -> List[Dict[str, str]]:
    """Validate user's order against correct order"""
    feedback = []
    
    for i, (user_step, correct_step) in enumerate(zip(user_order, CORRECT_STEPS)):
        is_correct = user_step == correct_step
        
        feedback_item = {
            "Position": i + 1,
            "Your Step": get_step_title(user_step),
            "Status": "✅" if is_correct else "❌",
            "Explanation": "" if is_correct else STEP_EXPLANATIONS[i]
        }
        feedback.append(feedback_item)
    
    return feedback

def create_step_item(step: str, index: int) -> str:
    """Create a step item for the sortable list"""
    title = get_step_title(step)
    description = get_step_description(step)
    
    # Return formatted text for sortable component
    return f"{index + 1}. {title} - {description}"

def display_step_card(step: str, index: int, color: str):
    """Display a step card with proper formatting and color"""
    title = get_step_title(step)
    description = get_step_description(step)
    
    st.markdown(f"""
    <div style="
        background-color: {color}15;
        border: 2px solid {color};
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    ">
        <div style="display: flex; align-items: start;">
            <span style="
                background-color: {color};
                color: white;
                border-radius: 50%;
                width: 30px;
                height: 30px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                margin-right: 15px;
                font-weight: bold;
                flex-shrink: 0;
            ">{index + 1}</span>
            <div style="flex: 1;">
                <div style="font-weight: bold; color: #1f2937; margin-bottom: 5px;">{title}</div>
                <div style="color: #6b7280; font-size: 14px;">{description}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown("<h1 class='main-header'>🎯 Azure Cost Optimization Puzzle Game</h1>", unsafe_allow_html=True)
    
    # Scenario
    st.markdown("### 📋 Scenario")
    st.markdown("""
    <div class='scenario-box'>
        You are an Engineering Manager in a mid-size company with skyrocketing Azure bills. 
        You've been asked to also handle FinOps. <strong>In which order will you solve the Azure cost issues?</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📝 Instructions")
    st.markdown(
        "Drag and drop the 7 colored steps below to arrange them in the correct logical sequence. "
        "Think about the dependencies between each step!"
    )
    
    # Game area
    if not st.session_state.submitted:
        st.markdown("### 🔄 Arrange the Steps")
        st.markdown("*Drag the items below to reorder them:*")
        
        # Create items for sortable component
        items = []
        for i, step in enumerate(st.session_state.user_order):
            items.append(create_step_item(step, i))
        
        # Use sortable component with custom styling
        with st.container():
            sorted_items = sort_items(items, key="sortable_steps", direction="vertical")
        
        # Update user order based on sorted items
        if sorted_items:
            # Map back to original steps
            new_order = []
            for sorted_item in sorted_items:
                # Extract the title from the formatted string
                for step in st.session_state.user_order:
                    if get_step_title(step) in sorted_item:
                        new_order.append(step)
                        break
            st.session_state.user_order = new_order
        
        # Buttons
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if st.button("🚀 Submit", type="primary", use_container_width=True):
                st.session_state.submitted = True
                st.rerun()
        
        with col2:
            if st.button("🔄 Reset", use_container_width=True):
                reset_game()
                st.rerun()
    
    else:
        # Show results
        st.markdown("### 📊 Results")
        
        # Check if all correct
        feedback = validate_order(st.session_state.user_order)
        all_correct = all(item["Status"] == "✅" for item in feedback)
        
        if all_correct:
            st.success("🎉 **Congratulations!** You've mastered the Azure cost optimization workflow!")
            st.balloons()
        else:
            st.error("❌ Some steps are in the wrong order. Review the feedback below:")
        
        # Show feedback table
        st.markdown("#### Your Submission:")
        df = pd.DataFrame(feedback)
        
        # Style the dataframe
        def style_status(val):
            if val == "✅":
                return 'color: green'
            elif val == "❌":
                return 'color: red'
            return ''
        
        styled_df = df.style.applymap(style_status, subset=['Status'])
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
        
        # Show correct order button
        if st.button("📖 Show Correct Order" if not st.session_state.show_correct else "📖 Hide Correct Order"):
            st.session_state.show_correct = not st.session_state.show_correct
        
        if st.session_state.show_correct:
            st.markdown("#### ✅ Correct Order:")
            for i, step in enumerate(CORRECT_STEPS):
                display_step_card(step, i, STEP_COLORS[i])
            
            st.markdown("#### 💡 Why This Order?")
            with st.expander("Click to understand the logic"):
                for i, explanation in STEP_EXPLANATIONS.items():
                    color = STEP_COLORS[i]
                    st.markdown(f"""
                    <div style="
                        border-left: 4px solid {color};
                        padding-left: 1rem;
                        margin: 0.5rem 0;
                    ">
                        <strong style="color: {color};">Step {i+1}:</strong> {explanation}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Reset button
        st.markdown("---")
        if st.button("🔄 Try Again", type="primary", use_container_width=True):
            reset_game()
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "💡 **Learning Tip:** The key to successful FinOps is following a systematic approach. "
        "Each step builds on the previous one!"
    )

if __name__ == "__main__":
    main()