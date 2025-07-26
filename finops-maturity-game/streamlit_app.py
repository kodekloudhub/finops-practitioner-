import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="FinOps Journey Simulation",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stInfo {
        font-size: 18px !important;
        line-height: 1.6 !important;
    }
    .stMarkdown {
        font-size: 16px !important;
    }
    .stRadio > label {
        font-size: 16px !important;
    }
    .stMultiSelect > label {
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'current_scenario_index' not in st.session_state:
    st.session_state.current_scenario_index = 0

if 'feedback_message' not in st.session_state:
    st.session_state.feedback_message = ""

# Define comprehensive scenarios
scenarios = [
    {
        "title": "Acme Corp's Cloud Chaos",
        "description": """Acme Corp, a mid-sized e-commerce company, has been using cloud services for the past 2 years. 
        Their engineering teams have been deploying applications directly to AWS without any centralized oversight. 
        Each team uses their own AWS accounts and billing methods. The finance team receives monthly bills that are 
        completely unexpected and often 3-4 times higher than budgeted. Engineers are not involved in cost discussions 
        and have no visibility into the financial impact of their decisions. The company has no cloud governance 
        policies, and resources are frequently left running even when not needed. Monthly cost reports are manually 
        compiled by the finance team and are often outdated by the time they reach leadership.""",
        "correct_maturity_stage": "Crawl",
        "correct_challenges": [
            "Lack of cost visibility",
            "No central governance", 
            "Engineers not involved in cost discussions",
            "Inefficient resource utilization",
            "Manual reporting processes"
        ],
        "maturity_options": ["Crawl", "Walk", "Run", "Unsure"],
        "challenge_options": [
            "Lack of cost visibility",
            "No central governance",
            "Engineers not involved in cost discussions"
        ]
    },
    {
        "title": "TechStart Inc's Growing Pains",
        "description": """TechStart Inc, a rapidly growing SaaS company, has established a FinOps team and implemented 
        basic cost allocation using tags. They have centralized their cloud accounts and created some governance policies. 
        Engineers now receive weekly cost reports for their teams, and there's a monthly FinOps review meeting. However, 
        the cost allocation is only 60% accurate due to inconsistent tagging practices. Some teams still don't understand 
        the cost implications of their architectural decisions. The company has started implementing some automated 
        cost optimization recommendations, but adoption is slow. Budget alerts exist but are often ignored, and there's 
        still a disconnect between engineering decisions and financial outcomes.""",
        "correct_maturity_stage": "Walk", 
        "correct_challenges": [
            "Inconsistent tagging practices",
            "Low automation adoption",
            "Budget alerts ignored",
            "Engineers not fully cost-aware",
            "Disconnect between engineering and finance"
        ],
        "maturity_options": ["Crawl", "Walk", "Run", "Unsure"],
        "challenge_options": [
            "Inconsistent tagging practices",
            "Low automation adoption",
            "Budget alerts ignored"
        ]
    },
    {
        "title": "CloudScale Enterprise's FinOps Excellence",
        "description": """CloudScale Enterprise has a mature FinOps practice with a dedicated team of 8 FinOps engineers. 
        They have achieved 95% cost allocation accuracy through automated tagging and governance policies. Engineers are 
        actively involved in cost optimization and receive real-time cost feedback during development. The company has 
        implemented automated cost optimization that saves 15-20% monthly. They use predictive analytics for budget 
        forecasting and have established chargeback/showback models. Teams are incentivized to optimize costs, and 
        there's a strong culture of cost awareness. The FinOps team collaborates closely with engineering, finance, 
        and business teams to align cloud spending with business value.""",
        "correct_maturity_stage": "Run",
        "correct_challenges": [
            "Maintaining high allocation accuracy",
            "Scaling FinOps practices",
            "Keeping up with new services",
            "Balancing optimization with innovation",
            "Managing complex multi-cloud environment"
        ],
        "maturity_options": ["Crawl", "Walk", "Run", "Unsure"],
        "challenge_options": [
            "Maintaining high allocation accuracy",
            "Scaling FinOps practices",
            "Balancing optimization with innovation"
        ]
    }
]

# Main Title and Instructions
st.title("FinOps Journey Simulation")
st.write("Read the scenario below and answer the questions to help the company improve its FinOps maturity.")

# Get current scenario
current_scenario = scenarios[st.session_state.current_scenario_index]

# Display Scenario
st.header(current_scenario['title'])
st.info(current_scenario['description'])
st.divider()

# User Input Widgets
st.subheader("Scenario Analysis")

# Maturity Stage Question
company_name = current_scenario['title'].split("'")[0]
user_maturity_choice = st.radio(
    f"What FinOps maturity stage does {company_name} seem to be in?",
    current_scenario['maturity_options']
)

# Challenges Question  
user_challenge_choices = st.multiselect(
    "What are the key FinOps challenges or opportunities present in this scenario? (Select all that apply)",
    current_scenario['challenge_options']
)

# Submit Button and Evaluation Logic
if st.button("Analyze Scenario"):
    feedback_parts = []
    
    # Maturity Check
    if user_maturity_choice == current_scenario['correct_maturity_stage']:
        maturity_feedback = f"✅ **Excellent!** You correctly identified this as a **{current_scenario['correct_maturity_stage']}** stage organization."
    else:
        maturity_feedback = f"❌ **Not quite right.** This organization is actually in the **{current_scenario['correct_maturity_stage']}** stage. "
        if current_scenario['correct_maturity_stage'] == "Crawl":
            maturity_feedback += "Look for signs of basic cloud usage without governance or cost awareness."
        elif current_scenario['correct_maturity_stage'] == "Walk":
            maturity_feedback += "Look for some governance and cost allocation, but with gaps in implementation."
        else:  # Run
            maturity_feedback += "Look for mature practices with high automation, accuracy, and team involvement."
    
    feedback_parts.append(maturity_feedback)
    
    # Challenges Check
    user_challenges_set = set(user_challenge_choices)
    correct_challenges_set = set(current_scenario['correct_challenges'])
    
    if user_challenges_set == correct_challenges_set:
        challenges_feedback = "✅ **Perfect!** You identified all the key challenges correctly."
    else:
        challenges_feedback = "📋 **Challenges Analysis:**\n"
        
        # Identify missed challenges
        missed_challenges = correct_challenges_set - user_challenges_set
        if missed_challenges:
            challenges_feedback += f"**Missed challenges:** {', '.join(missed_challenges)}\n"
        
        # Identify incorrect selections
        incorrect_challenges = user_challenges_set - correct_challenges_set
        if incorrect_challenges:
            challenges_feedback += f"**Incorrect selections:** {', '.join(incorrect_challenges)}\n"
        
        challenges_feedback += f"**Correct challenges:** {', '.join(correct_challenges_set)}"
    
    feedback_parts.append(challenges_feedback)
    
    # Combine feedback
    st.session_state.feedback_message = "\n\n".join(feedback_parts)
    
    # Show progression message
    if st.session_state.current_scenario_index < len(scenarios) - 1:
        st.success("Ready to move to the next scenario! Use the navigation below.")

# Display Feedback
if st.session_state.feedback_message:
    st.divider()
    st.markdown(st.session_state.feedback_message)

# Navigation
st.divider()
st.subheader("Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Previous Scenario") and st.session_state.current_scenario_index > 0:
        st.session_state.current_scenario_index -= 1
        st.session_state.feedback_message = ""
        st.rerun()

with col2:
    st.write(f"Scenario {st.session_state.current_scenario_index + 1} of {len(scenarios)}")

with col3:
    if st.button("Next Scenario") and st.session_state.current_scenario_index < len(scenarios) - 1:
        st.session_state.current_scenario_index += 1
        st.session_state.feedback_message = ""
        st.rerun()

# Reset button
if st.button("Reset Game"):
    st.session_state.current_scenario_index = 0
    st.session_state.feedback_message = ""
    st.rerun() 