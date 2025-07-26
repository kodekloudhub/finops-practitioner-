import streamlit as st
import random
from typing import Dict, List, Optional
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Kubecost FinOps Detective 🕵️‍♂️",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        background-color: #2196F3;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        border-radius: 8px;
        width: 100%;
        margin: 0.5rem 0;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #1976D2;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Success button */
    .success-button > button {
        background-color: #4CAF50 !important;
    }
    
    .success-button > button:hover {
        background-color: #45a049 !important;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    
    /* Info boxes */
    .info-box {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
    
    /* Success box */
    .success-box {
        background-color: #e8f5e9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    
    /* Error box */
    .error-box {
        background-color: #ffebee;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #f44336;
        margin: 1rem 0;
    }
    
    /* Table styling */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Header styling */
    h1 {
        color: #1976D2;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    h2 {
        color: #424242;
        margin-top: 1.5rem;
    }
    
    h3 {
        color: #616161;
    }
</style>
""", unsafe_allow_html=True)

# Game scenarios data
def get_scenarios():
    return {
        "stage1": {
            "description": "Your Kubernetes cluster monthly cost is **${cost}**. Kubecost shows unusually high usage patterns across namespaces.",
            "data": {
                "Namespace": ["prod", "dev", "staging"],
                "Monthly Cost": ["${prod_cost}", "${dev_cost}", "${stage_cost}"],
                "CPU Efficiency": ["40%", "70%", "55%"],
                "Memory Efficiency": ["35%", "65%", "50%"]
            },
            "choices": [
                {
                    "text": "🔍 Drill into 'prod' namespace for detailed analysis",
                    "points": 100,
                    "next": "stage2",
                    "feedback": "✅ Excellent! In FinOps, visibility is the first step. Kubecost's namespace drill-down reveals resource waste."
                },
                {
                    "text": "⚡ Immediately scale down all namespaces by 50%",
                    "points": -50,
                    "next": "stage2",
                    "feedback": "❌ Risky move! Without data-driven insights, you might break production. Always analyze before acting."
                },
                {
                    "text": "📊 Check workload-level costs first",
                    "points": 50,
                    "next": "stage2",
                    "feedback": "🔍 Good approach! Workload analysis helps, but namespace view gives better initial overview."
                },
                {
                    "text": "🔔 Set budget alerts without investigation",
                    "points": -25,
                    "next": "stage2",
                    "feedback": "⚠️ Premature! Alerts without understanding baseline costs lead to noise. Investigate first."
                }
            ]
        },
        "stage2": {
            "description": "Drilling into the 'prod' namespace, Kubecost reveals several deployments with concerning metrics:",
            "data": {
                "Workload": ["api-server", "data-processor", "legacy-app"],
                "Monthly Cost": ["${api_cost}", "${data_cost}", "${legacy_cost}"],
                "CPU Request": ["4000m", "8000m", "2000m"],
                "CPU Usage": ["800m", "7500m", "100m"],
                "Memory Request": ["8Gi", "16Gi", "4Gi"],
                "Memory Usage": ["2Gi", "15Gi", "0.5Gi"]
            },
            "choices": [
                {
                    "text": "💰 Rightsize api-server and legacy-app immediately",
                    "points": 100,
                    "next": "stage3",
                    "feedback": "💰 Perfect! These show clear overprovisioning. Kubecost's efficiency metrics guide rightsizing decisions."
                },
                {
                    "text": "🗑️ Delete legacy-app without checking dependencies",
                    "points": -75,
                    "next": "stage3",
                    "feedback": "🚫 Dangerous! Even idle resources might be critical. Check dependencies and usage patterns first."
                },
                {
                    "text": "📈 Increase data-processor resources (it's near limits)",
                    "points": -50,
                    "next": "stage3",
                    "feedback": "📈 Counterproductive! This would increase costs. The workload is efficiently using resources."
                },
                {
                    "text": "💾 Export Kubecost data for offline analysis",
                    "points": 25,
                    "next": "stage3",
                    "feedback": "⏱️ Valid but slow. Kubecost enables real-time decisions. Act on clear inefficiencies now!"
                }
            ]
        },
        "stage3": {
            "description": "After rightsizing, you discover untagged resources making cost allocation difficult. Kubecost shows:",
            "data": {
                "Resource Type": ["Deployments", "Services", "PVCs"],
                "Count": [45, 60, 30],
                "Monthly Cost": ["${deploy_cost}", "${svc_cost}", "${pvc_cost}"],
                "Tagged %": ["20%", "15%", "5%"],
                "Team Owner": ["Unknown", "Unknown", "Unknown"]
            },
            "choices": [
                {
                    "text": "🏷️ Implement mandatory tagging policy with team/cost-center labels",
                    "points": 100,
                    "next": "stage4",
                    "feedback": "🏷️ Excellent! Proper tagging enables Kubecost's cost allocation features for accountability."
                },
                {
                    "text": "✏️ Manually assign costs based on namespace names",
                    "points": 25,
                    "next": "stage4",
                    "feedback": "📊 Temporary fix. Automated tagging scales better and integrates with Kubecost reports."
                },
                {
                    "text": "🚫 Ignore tagging and focus on total cost only",
                    "points": -50,
                    "next": "stage4",
                    "feedback": "❌ Short-sighted! Without allocation, teams lack ownership of their costs. FinOps requires accountability."
                },
                {
                    "text": "💥 Delete all untagged resources",
                    "points": -100,
                    "next": "stage4",
                    "feedback": "💥 Catastrophic! This would cause outages. Tagging should be enforced, not destructive."
                }
            ]
        },
        "stage4": {
            "description": "With better visibility, you notice usage patterns. Kubecost's recommendations engine suggests:",
            "data": {
                "Optimization Type": ["Spot Instances (dev)", "Reserved Instances", "Autoscaling (HPA/VPA)", "Off-hours Scaling"],
                "Potential Savings": ["${spot_save}/mo", "${ri_save}/mo", "${auto_save}/mo", "${offhour_save}/mo"],
                "Implementation Effort": ["Medium", "Low", "High", "Medium"],
                "Risk Level": ["Low", "Very Low", "Medium", "Low"]
            },
            "choices": [
                {
                    "text": "🎯 Implement Spot instances for dev/staging environments",
                    "points": 100,
                    "next": "stage5",
                    "feedback": "🎯 Smart choice! Spot instances are perfect for non-critical workloads. Kubecost tracks spot savings."
                },
                {
                    "text": "📅 Purchase 3-year Reserved Instances for everything",
                    "points": -25,
                    "next": "stage5",
                    "feedback": "📅 Too aggressive! Start with 1-year RIs for stable workloads. Kubecost helps identify candidates."
                },
                {
                    "text": "📈 Enable aggressive autoscaling on all workloads",
                    "points": 50,
                    "next": "stage5",
                    "feedback": "📈 Good but risky! Test autoscaling gradually. Kubecost monitors scaling impact on costs."
                },
                {
                    "text": "🔄 Implement all optimizations simultaneously",
                    "points": -50,
                    "next": "stage5",
                    "feedback": "🔄 Overwhelming! Phased approach reduces risk. Kubecost tracks each optimization's impact."
                }
            ]
        },
        "stage5": {
            "description": "Final step: Establishing ongoing FinOps practices. Kubecost offers these monitoring features:",
            "data": {
                "Feature": ["Budget Alerts", "Efficiency Reports", "Cost Allocation", "Savings Tracking"],
                "Purpose": ["Proactive cost control", "Continuous optimization", "Team accountability", "Measure FinOps impact"],
                "FinOps Pillar": ["Operate", "Optimize", "Inform", "All"]
            },
            "choices": [
                {
                    "text": "📊 Set up weekly efficiency reports and monthly budget reviews",
                    "points": 100,
                    "next": "end",
                    "feedback": "🎉 Perfect! Regular cadence ensures continuous FinOps improvement. Kubecost automates this!"
                },
                {
                    "text": "⚠️ Create alerts for 200% budget overrun only",
                    "points": -25,
                    "next": "end",
                    "feedback": "⚠️ Too late! Earlier alerts (e.g., 80%) enable proactive action. Kubecost supports multiple thresholds."
                },
                {
                    "text": "👤 Assign FinOps to one person part-time",
                    "points": 25,
                    "next": "end",
                    "feedback": "👥 Okay start, but FinOps needs cross-functional collaboration. Kubecost dashboards enable team self-service."
                },
                {
                    "text": "📉 Rely on quarterly manual reviews",
                    "points": -50,
                    "next": "end",
                    "feedback": "📉 Insufficient! Cloud costs change daily. Kubecost's real-time monitoring is essential."
                }
            ]
        }
    }

# Initialize session state
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 'intro'
    st.session_state.points = 0
    st.session_state.choices_made = []
    st.session_state.badges = []
    st.session_state.feedback = None
    st.session_state.stage_data = {}
    
    # Randomize costs
    multiplier = random.uniform(0.9, 1.1)
    base_costs = {
        "cost": 5000,
        "prod_cost": 3000,
        "dev_cost": 1500,
        "stage_cost": 500,
        "api_cost": 1200,
        "data_cost": 1500,
        "legacy_cost": 300,
        "deploy_cost": 2500,
        "svc_cost": 1000,
        "pvc_cost": 1500,
        "spot_save": 800,
        "ri_save": 1200,
        "auto_save": 600,
        "offhour_save": 400
    }
    st.session_state.stage_data = {k: int(v * multiplier) for k, v in base_costs.items()}

def calculate_badges():
    """Calculate badges based on performance"""
    badges = []
    if st.session_state.points >= 400:
        badges.append("🏆 Master Detective")
    elif st.session_state.points >= 300:
        badges.append("🕵️ Senior Detective")
    elif st.session_state.points >= 200:
        badges.append("🔍 Junior Detective")
    
    # Special badges
    if any("Drill into" in choice for choice in st.session_state.choices_made):
        badges.append("🔎 Investigator")
    if any("tagging" in choice.lower() for choice in st.session_state.choices_made):
        badges.append("🏷️ Organizer")
    if any("Spot instances" in choice for choice in st.session_state.choices_made):
        badges.append("💰 Cost Optimizer")
    if st.session_state.points >= 300:
        badges.append("🎯 FinOps Expert")
    
    return badges

def format_data_with_values(data: Dict, values: Dict[str, any]) -> pd.DataFrame:
    """Replace placeholders in data with actual values"""
    formatted_data = {}
    for key, value_list in data.items():
        formatted_list = []
        for value in value_list:
            if isinstance(value, str) and "${" in value:
                for var_name, var_value in values.items():
                    value = value.replace(f"${{{var_name}}}", f"${var_value}")
            formatted_list.append(value)
        formatted_data[key] = formatted_list
    return pd.DataFrame(formatted_data)

def show_intro():
    """Display introduction screen"""
    st.markdown("# Kubecost FinOps Detective 🕵️‍♂️")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>📢 Alert: Cloud Costs Out of Control!</h3>
        <p>Your Kubernetes cluster costs are spiraling out of control! 💸</p>
        <p>As the company's new <strong>FinOps Detective</strong>, you must use Kubecost to investigate 
        the rising cloud bills and implement cost optimizations.</p>
        <p>Make strategic decisions to reduce costs while maintaining performance.
        Each choice affects your score and the company's bottom line!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### 🎯 Your Mission:
        - **Investigate** high costs using Kubecost
        - **Optimize** resources efficiently
        - **Implement** FinOps best practices
        - **Save** at least 40% to succeed!
        
        ### 🏆 Scoring:
        - Max points: 500
        - Success threshold: 300+
        - Earn badges for achievements
        """)
    
    if st.button("🔍 Begin Investigation", key="start", help="Start your FinOps detective journey"):
        st.session_state.current_stage = "stage1"
        st.session_state.feedback = None
        st.rerun()

def show_game_stage():
    """Display current game stage"""
    scenarios = get_scenarios()
    current = scenarios.get(st.session_state.current_stage)
    
    if not current:
        return
    
    # Progress bar
    stage_num = int(st.session_state.current_stage[-1]) if st.session_state.current_stage.startswith("stage") else 0
    progress = stage_num / 5
    
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.progress(progress)
        st.caption(f"Stage {stage_num}/5")
    with col2:
        st.metric("Points", st.session_state.points, delta=None)
    with col3:
        if st.session_state.badges:
            st.caption("Badges: " + " ".join(st.session_state.badges[-2:]))
    
    # Show feedback if available
    if st.session_state.feedback:
        if st.session_state.feedback.startswith("✅") or st.session_state.feedback.startswith("🎯") or st.session_state.feedback.startswith("💰") or st.session_state.feedback.startswith("🏷️") or st.session_state.feedback.startswith("🎉"):
            st.success(st.session_state.feedback)
        elif st.session_state.feedback.startswith("❌") or st.session_state.feedback.startswith("🚫") or st.session_state.feedback.startswith("💥") or st.session_state.feedback.startswith("📉"):
            st.error(st.session_state.feedback)
        else:
            st.warning(st.session_state.feedback)
    
    # Stage description
    st.markdown("---")
    description = current["description"]
    for key, value in st.session_state.stage_data.items():
        description = description.replace(f"${{{key}}}", str(value))
    st.markdown(f"### {description}")
    
    # Kubecost data display
    if current.get("data"):
        st.markdown("#### 📊 Kubecost Report:")
        df = format_data_with_values(current["data"], st.session_state.stage_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Choices
    st.markdown("#### What's your next move?")
    
    cols = st.columns(2)
    for i, choice in enumerate(current["choices"]):
        with cols[i % 2]:
            if st.button(choice["text"], key=f"choice_{i}", use_container_width=True):
                make_choice(choice)

def show_end_screen():
    """Display end game screen"""
    st.session_state.badges = calculate_badges()
    
    # Calculate savings
    initial_cost = st.session_state.stage_data.get("cost", 5000)
    savings_percent = min((st.session_state.points / 500) * 50, 45)
    final_cost = int(initial_cost * (1 - savings_percent / 100))
    
    # Success or failure
    success = st.session_state.points >= 300
    
    if success:
        st.balloons()
        st.markdown("""
        <div class="success-box">
        <h1>🎉 Investigation Complete! 🎉</h1>
        <h3>Congratulations, Detective! You've successfully reduced the cloud costs!</h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="error-box">
        <h1>😔 Investigation Failed 😔</h1>
        <h3>The cloud costs remain high. Try again with better strategies!</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Results
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Final Report")
        metrics_data = {
            "Metric": ["Total Points", "Initial Monthly Cost", "Final Monthly Cost", "Cost Reduction", "Annual Savings"],
            "Value": [
                f"{st.session_state.points}/500",
                f"${initial_cost}",
                f"${final_cost}",
                f"{savings_percent:.1f}%",
                f"${(initial_cost - final_cost) * 12}"
            ]
        }
        st.table(pd.DataFrame(metrics_data))
    
    with col2:
        st.markdown("### 🏅 Badges Earned")
        if st.session_state.badges:
            for badge in st.session_state.badges:
                st.markdown(f"# {badge}")
        else:
            st.markdown("No badges earned. Try again!")
    
    # Key learnings
    st.markdown("---")
    st.markdown("### 📚 Key FinOps Learnings")
    
    learnings = [
        "**Visibility First**: Kubecost provides detailed cost breakdowns essential for informed decisions",
        "**Data-Driven Optimization**: Efficiency metrics guide rightsizing and resource allocation",
        "**Continuous Monitoring**: Regular reviews and alerts prevent cost creep",
        "**Team Accountability**: Proper tagging and allocation drives ownership",
        "**Phased Implementation**: Gradual optimization reduces risk while maximizing savings"
    ]
    
    for learning in learnings:
        st.markdown(f"- {learning}")
    
    # Retry button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Play Again", key="retry", use_container_width=True):
            reset_game()

def make_choice(choice):
    """Process player's choice"""
    st.session_state.points += choice["points"]
    st.session_state.choices_made.append(choice["text"])
    st.session_state.feedback = choice["feedback"]
    st.session_state.current_stage = choice["next"]
    st.rerun()

def reset_game():
    """Reset game state"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Main app logic
def main():
    if st.session_state.current_stage == "intro":
        show_intro()
    elif st.session_state.current_stage == "end":
        show_end_screen()
    else:
        show_game_stage()

if __name__ == "__main__":
    main()