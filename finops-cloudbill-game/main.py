import streamlit as st
import random
import json
import os

# Page configuration
st.set_page_config(
    page_title="FinOps CloudBill Game",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2d3a4a;
        margin-bottom: 2rem;
    }
    .step-header {
        color: #1f77b4;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
    .results-box {
        background-color: #e6ffe6;
        border: 1px solid #b2ffb2;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .tip-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .feedback-correct {
        color: #28a745;
        font-weight: bold;
    }
    .feedback-incorrect {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Game constants
CATEGORIES = ['idle', 'underprovisioned', 'overprovisioned']
OPTIMIZATIONS = ['rightsizing', 'lifecycle policy', 'release', 'no action']
TIPS = [
    "Rightsizing means matching resource size to actual usage.",
    "Lifecycle policies can automatically delete old backups.",
    "Idle resources are a common source of cloud waste.",
    "Overprovisioned databases can be downsized for savings.",
    "Elastic IPs incur charges when not attached to running instances."
]

def load_mock_bills():
    """Load mock bills from JSON file"""
    mock_bills_path = os.path.join(os.path.dirname(__file__), "mock_bills.json")
    with open(mock_bills_path, "r") as f:
        return json.load(f)

def get_random_bill():
    """Get a random bill from the mock data"""
    bills = load_mock_bills()
    return random.choice(bills)

def validate_categories(bill, user_categories):
    """Validate user category selections"""
    results = {}
    for item in bill["items"]:
        correct = item["category_answer"]
        user = user_categories.get(item["id"])
        results[item["id"]] = {
            "user": user, 
            "correct": correct, 
            "is_correct": user == correct
        }
    return results

def validate_optimizations(bill, user_optimizations):
    """Validate user optimization selections and calculate savings"""
    before_total = sum(item["cost"] for item in bill["items"])
    after_items = []
    savings = 0
    
    for item in bill["items"]:
        correct_opt = item["optimization_answer"]
        user_opt = user_optimizations.get(item["id"])
        cost = item["cost"]
        
        if user_opt == correct_opt and correct_opt != "no action":
            # Assume 80% savings for correct optimization
            saved = round(cost * 0.8, 2)
            after_cost = round(cost - saved, 2)
            savings += saved
        else:
            after_cost = cost
            
        after_items.append({
            **item, 
            "after_cost": after_cost, 
            "user_opt": user_opt, 
            "correct_opt": correct_opt
        })
    
    after_total = sum(i["after_cost"] for i in after_items)
    
    return {
        "before_total": before_total,
        "after_total": after_total,
        "savings": round(savings, 2),
        "details": after_items
    }

def main():
    # Initialize session state
    if 'current_bill' not in st.session_state:
        st.session_state.current_bill = get_random_bill()
    if 'game_step' not in st.session_state:
        st.session_state.game_step = 'categorize'
    if 'user_categories' not in st.session_state:
        st.session_state.user_categories = {}
    if 'user_optimizations' not in st.session_state:
        st.session_state.user_optimizations = {}
    if 'category_results' not in st.session_state:
        st.session_state.category_results = {}
    if 'optimization_results' not in st.session_state:
        st.session_state.optimization_results = {}

    # Main header
    st.markdown('<h1 class="main-header">💰 FinOps CloudBill Game</h1>', unsafe_allow_html=True)

    # Sidebar for game controls
    with st.sidebar:
        st.header("Game Controls")
        if st.button("🔄 New Game"):
            st.session_state.current_bill = get_random_bill()
            st.session_state.game_step = 'categorize'
            st.session_state.user_categories = {}
            st.session_state.user_optimizations = {}
            st.session_state.category_results = {}
            st.session_state.optimization_results = {}
            st.rerun()

    # Step 1: Categorization
    if st.session_state.game_step == 'categorize':
        st.markdown('<h2 class="step-header">Step 1: Categorize Each Line Item</h2>', unsafe_allow_html=True)
        
        # Display bill items in a dataframe
        bill_data = []
        for item in st.session_state.current_bill["items"]:
            bill_data.append({
                "Resource": item["resource"],
                "Description": item["description"],
                "Cost ($)": f"${item['cost']:.2f}"
            })
        
        st.dataframe(bill_data, use_container_width=True)
        
        # Category selection form
        with st.form("category_form"):
            st.subheader("Select the correct category for each item:")
            
            # Create columns for better layout
            cols = st.columns(2)
            col_idx = 0
            
            for item in st.session_state.current_bill["items"]:
                with cols[col_idx]:
                    category = st.selectbox(
                        f"{item['resource']} - ${item['cost']:.2f}",
                        options=[""] + CATEGORIES,
                        key=f"cat_{item['id']}",
                        help=item['description']
                    )
                    st.session_state.user_categories[item['id']] = category
                
                col_idx = (col_idx + 1) % 2
            
            submitted = st.form_submit_button("Submit Categories")
            
            if submitted:
                # Validate all categories are selected
                if all(st.session_state.user_categories.values()):
                    st.session_state.category_results = validate_categories(
                        st.session_state.current_bill, 
                        st.session_state.user_categories
                    )
                    st.session_state.game_step = 'category_results'
                    st.rerun()
                else:
                    st.error("Please select a category for all items.")

    # Show category results
    elif st.session_state.game_step == 'category_results':
        st.markdown('<h2 class="step-header">Category Results</h2>', unsafe_allow_html=True)
        
        # Display results
        all_correct = True
        for item in st.session_state.current_bill["items"]:
            result = st.session_state.category_results[item["id"]]
            status = "✅" if result["is_correct"] else "❌"
            color_class = "feedback-correct" if result["is_correct"] else "feedback-incorrect"
            
            st.markdown(f"""
            **{item['resource']}** - {status} 
            <span class="{color_class}">Your answer: {result['user']} | Correct: {result['correct']}</span>
            """, unsafe_allow_html=True)
            
            if not result["is_correct"]:
                all_correct = False
        
        if all_correct:
            st.success("🎉 All categories correct! Moving to optimization step.")
            st.session_state.game_step = 'optimize'
            st.rerun()
        else:
            st.error("❌ Please correct your mistakes and try again.")
            if st.button("Try Again"):
                st.session_state.game_step = 'categorize'
                st.rerun()

    # Step 2: Optimization
    elif st.session_state.game_step == 'optimize':
        st.markdown('<h2 class="step-header">Step 2: Choose Best Optimization for Each Item</h2>', unsafe_allow_html=True)
        
        # Display bill items again
        bill_data = []
        for item in st.session_state.current_bill["items"]:
            bill_data.append({
                "Resource": item["resource"],
                "Description": item["description"],
                "Cost ($)": f"${item['cost']:.2f}",
                "Category": st.session_state.category_results[item["id"]]["correct"]
            })
        
        st.dataframe(bill_data, use_container_width=True)
        
        # Optimization selection form
        with st.form("optimization_form"):
            st.subheader("Select the best optimization for each item:")
            
            # Create columns for better layout
            cols = st.columns(2)
            col_idx = 0
            
            for item in st.session_state.current_bill["items"]:
                with cols[col_idx]:
                    optimization = st.selectbox(
                        f"{item['resource']} - ${item['cost']:.2f}",
                        options=[""] + OPTIMIZATIONS,
                        key=f"opt_{item['id']}",
                        help=item['description']
                    )
                    st.session_state.user_optimizations[item['id']] = optimization
                
                col_idx = (col_idx + 1) % 2
            
            submitted = st.form_submit_button("Submit Optimizations")
            
            if submitted:
                # Validate all optimizations are selected
                if all(st.session_state.user_optimizations.values()):
                    st.session_state.optimization_results = validate_optimizations(
                        st.session_state.current_bill, 
                        st.session_state.user_optimizations
                    )
                    st.session_state.game_step = 'final_results'
                    st.rerun()
                else:
                    st.error("Please select an optimization for all items.")

    # Final results
    elif st.session_state.game_step == 'final_results':
        st.markdown('<h2 class="step-header">🎯 Final Results</h2>', unsafe_allow_html=True)
        
        results = st.session_state.optimization_results
        
        # Results summary
        st.markdown(f"""
        <div class="results-box">
        <h3>💰 Cost Savings Summary</h3>
        <p><strong>Before:</strong> ${results['before_total']:.2f}</p>
        <p><strong>After:</strong> ${results['after_total']:.2f}</p>
        <p><strong>Total Savings:</strong> ${results['savings']:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed results table
        st.subheader("Detailed Results")
        results_data = []
        for item in results["details"]:
            is_correct = item["user_opt"] == item["correct_opt"]
            status = "✅" if is_correct else "❌"
            
            results_data.append({
                "Resource": item["resource"],
                "Your Choice": item["user_opt"],
                "Correct Choice": item["correct_opt"],
                "Before": f"${item['cost']:.2f}",
                "After": f"${item['after_cost']:.2f}",
                "Status": status
            })
        
        st.dataframe(results_data, use_container_width=True)
        
        # Show tip
        tip = random.choice(TIPS)
        st.markdown(f"""
        <div class="tip-box">
        <h4>💡 FinOps Tip</h4>
        <p>{tip}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Play again button
        if st.button("🎮 Play Again"):
            st.session_state.current_bill = get_random_bill()
            st.session_state.game_step = 'categorize'
            st.session_state.user_categories = {}
            st.session_state.user_optimizations = {}
            st.session_state.category_results = {}
            st.session_state.optimization_results = {}
            st.rerun()

if __name__ == "__main__":
    main() 