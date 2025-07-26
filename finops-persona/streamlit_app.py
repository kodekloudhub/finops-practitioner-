import streamlit as st
import json
import random
from typing import Dict, List, Tuple
import time

# Page configuration
st.set_page_config(
    page_title="FinOps City: Match & Solve",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .problem-card {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .problem-card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
        transform: translateY(-2px);
    }
    
    .problem-card.selected {
        border-color: #667eea;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .persona-card {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .persona-card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
        transform: translateY(-2px);
    }
    
    .persona-card.selected {
        border-color: #667eea;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .persona-card.matched {
        border-color: #4caf50;
        background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
        color: white;
    }
    
    .persona-type {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .persona-type.core {
        background: #ff6b6b;
        color: white;
    }
    
    .persona-type.allied {
        background: #4ecdc4;
        color: white;
    }
    
    .score-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .progress-bar {
        background: #e0e0e0;
        border-radius: 10px;
        height: 20px;
        margin: 1rem 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #4caf50 0%, #45a049 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    .feedback-success {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .feedback-error {
        background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .mission-card {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    .mission-option {
        background: #f8f9fa;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .mission-option:hover {
        border-color: #667eea;
        background: #e3f2fd;
    }
    
    .mission-option.selected {
        border-color: #667eea;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .results-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .match-summary-item {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #4caf50;
    }
    
    .match-summary-item.incorrect {
        border-left-color: #f44336;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:disabled {
        background: #e0e0e0;
        color: #666;
        transform: none;
        box-shadow: none;
    }
</style>
""", unsafe_allow_html=True)

# Game data
PROBLEMS = [
    {
        "id": 1,
        "title": "Unexpected Cost Spike",
        "description": "Cloud bill jumped by 50% due to unoptimized resources running 24/7",
        "correct_persona": "Cloud Engineer (Core)",
        "category": "Cost Optimization"
    },
    {
        "id": 2,
        "title": "Budget Forecasting Issue",
        "description": "Need to predict next quarter's cloud spending for accurate budgeting",
        "correct_persona": "Finance Analyst (Allied)",
        "category": "Financial Planning"
    },
    {
        "id": 3,
        "title": "Lack of Cost Visibility",
        "description": "Teams unaware of cloud usage costs and resource consumption patterns",
        "correct_persona": "Finance Analyst (Allied)",
        "category": "Cost Transparency"
    },
    {
        "id": 4,
        "title": "Resource Scaling Dilemma",
        "description": "Scale resources for a product launch while controlling costs effectively",
        "correct_persona": "Product Manager (Allied)",
        "category": "Resource Management"
    },
    {
        "id": 5,
        "title": "Compliance Gap",
        "description": "Risk of violating cloud spending policies and governance requirements",
        "correct_persona": "Executive Leader (Allied)",
        "category": "Governance"
    }
]

PERSONAS = [
    {
        "name": "Cloud Engineer (Core)",
        "type": "Core",
        "description": "Optimizes cloud resources, implements cost-saving measures, and manages infrastructure efficiency",
        "responsibilities": ["Resource optimization", "Cost monitoring", "Infrastructure management"]
    },
    {
        "name": "Finance Analyst (Allied)",
        "type": "Allied",
        "description": "Handles budgeting, forecasting, cost allocation, and financial reporting for cloud spending",
        "responsibilities": ["Budget planning", "Cost forecasting", "Financial reporting"]
    },
    {
        "name": "Product Manager (Allied)",
        "type": "Allied",
        "description": "Balances business needs with cost considerations and makes resource allocation decisions",
        "responsibilities": ["Business alignment", "Resource planning", "Cost-benefit analysis"]
    },
    {
        "name": "Procurement Specialist (Allied)",
        "type": "Allied",
        "description": "Manages vendor relationships, negotiates contracts, and ensures policy compliance",
        "responsibilities": ["Vendor management", "Contract negotiation", "Policy compliance"]
    },
    {
        "name": "Executive Leader (Allied)",
        "type": "Allied",
        "description": "Ensures accountability, sets strategic direction, and oversees FinOps governance",
        "responsibilities": ["Strategic oversight", "Governance", "Accountability"]
    }
]

MINI_MISSIONS = {
    1: {
        "title": "Cost Optimization Challenge",
        "question": "What's the best immediate action to reduce the cost spike?",
        "options": [
            {"id": "a", "text": "Shut down unused instances during off-hours", "correct": True},
            {"id": "b", "text": "Increase instance sizes for better performance", "correct": False},
            {"id": "c", "text": "Wait for the next billing cycle", "correct": False}
        ]
    },
    2: {
        "title": "Budget Planning Mission",
        "question": "Which approach is best for accurate cloud spending forecasting?",
        "options": [
            {"id": "a", "text": "Use historical data and growth trends", "correct": True},
            {"id": "b", "text": "Guess based on current month", "correct": False},
            {"id": "c", "text": "Set a flat budget increase", "correct": False}
        ]
    },
    3: {
        "title": "Cost Transparency Mission",
        "question": "How can you improve cost visibility across teams?",
        "options": [
            {"id": "a", "text": "Implement cost allocation tags and dashboards", "correct": True},
            {"id": "b", "text": "Hide cost information from teams", "correct": False},
            {"id": "c", "text": "Send monthly email reports", "correct": False}
        ]
    },
    4: {
        "title": "Resource Planning Mission",
        "question": "What's the best approach for scaling during a product launch?",
        "options": [
            {"id": "a", "text": "Use auto-scaling with cost alerts", "correct": True},
            {"id": "b", "text": "Over-provision to be safe", "correct": False},
            {"id": "c", "text": "Use only on-demand instances", "correct": False}
        ]
    },
    5: {
        "title": "Governance Mission",
        "question": "How should you address compliance gaps in cloud spending?",
        "options": [
            {"id": "a", "text": "Implement spending policies and approval workflows", "correct": True},
            {"id": "b", "text": "Ignore the policies for now", "correct": False},
            {"id": "c", "text": "Let teams spend freely", "correct": False}
        ]
    }
}

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'current_screen': 'start',
        'score': 0,
        'matches': {},
        'completed_problems': set(),
        'current_mission': None,
        'selected_problem': None,
        'selected_persona': None
    }

def render_start_screen():
    """Render the start screen with game introduction"""
    st.markdown("""
    <div class="main-header">
        <h1>🎮 FinOps City: Match & Solve</h1>
        <p>Master FinOps roles through interactive problem-solving!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ### 🎯 Game Overview
        Welcome to **FinOps City: Match & Solve**! This interactive game will help you understand 
        FinOps personas and their responsibilities by matching real-world cloud cost management 
        problems to the appropriate FinOps roles.
        
        ### 🎮 How to Play
        1. **Match Problems to Personas**: Connect 5 cloud cost challenges to the correct FinOps personas
        2. **Complete Mini-Missions**: After each correct match, solve a quick scenario for bonus points
        3. **Learn & Improve**: Get detailed feedback and explanations for each decision
        4. **Track Progress**: Monitor your score and learning outcomes
        
        ### 🏆 Scoring System
        - **Correct Match**: 10 points
        - **Mini-Mission Success**: 5 points
        - **Maximum Score**: 75 points
        
        ### 🎓 Learning Objectives
        - Understand FinOps personas and their responsibilities
        - Learn which persona is best suited for different cloud cost challenges
        - Gain knowledge of practical cost optimization strategies
        - Understand the collaborative nature of FinOps
        """)
        
        if st.button("🚀 Start Game", use_container_width=True):
            st.session_state.game_state['current_screen'] = 'game'
            st.rerun()

def render_game_screen():
    """Render the main game screen"""
    st.markdown("""
    <div class="main-header">
        <h1>🎮 FinOps City: Match & Solve</h1>
        <p>Match problems to the correct FinOps personas!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Score and progress display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="score-display">
            <h3>Score</h3>
            <h2>{st.session_state.game_state['score']}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        progress = len(st.session_state.game_state['completed_problems']) / len(PROBLEMS)
        st.markdown(f"""
        <div class="score-display">
            <h3>Progress</h3>
            <h2>{len(st.session_state.game_state['completed_problems'])}/{len(PROBLEMS)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("🔄 Reset Game", use_container_width=True):
            st.session_state.game_state = {
                'current_screen': 'game',
                'score': 0,
                'matches': {},
                'completed_problems': set(),
                'current_mission': None,
                'selected_problem': None,
                'selected_persona': None
            }
            st.rerun()
    
    # Progress bar
    progress = len(st.session_state.game_state['completed_problems']) / len(PROBLEMS)
    st.markdown(f"""
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress * 100}%"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Game area
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Cloud Cost Problems")
        for problem in PROBLEMS:
            is_completed = problem['id'] in st.session_state.game_state['completed_problems']
            is_selected = st.session_state.game_state['selected_problem'] == problem['id']
            
            card_class = "problem-card"
            if is_completed:
                card_class += " matched"
            elif is_selected:
                card_class += " selected"
            
            st.markdown(f"""
            <div class="{card_class}" onclick="selectProblem({problem['id']})">
                <h4>{problem['title']}</h4>
                <p><strong>Category:</strong> {problem['category']}</p>
                <p>{problem['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Select Problem {problem['id']}", key=f"prob_{problem['id']}", use_container_width=True):
                if not is_completed:
                    st.session_state.game_state['selected_problem'] = problem['id']
                    st.session_state.game_state['selected_persona'] = None
                    st.rerun()
    
    with col2:
        st.markdown("### 👥 FinOps Personas")
        for persona in PERSONAS:
            is_matched = persona['name'] in st.session_state.game_state['matches'].values()
            is_selected = st.session_state.game_state['selected_persona'] == persona['name']
            
            card_class = "persona-card"
            if is_matched:
                card_class += " matched"
            elif is_selected:
                card_class += " selected"
            
            st.markdown(f"""
            <div class="{card_class}">
                <h4>{persona['name']}</h4>
                <span class="persona-type {persona['type'].lower()}">{persona['type']}</span>
                <p>{persona['description']}</p>
                <p><strong>Key Responsibilities:</strong></p>
                <ul>
                    {''.join([f'<li>{resp}</li>' for resp in persona['responsibilities']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Select {persona['name']}", key=f"pers_{persona['name']}", use_container_width=True):
                if not is_matched:
                    st.session_state.game_state['selected_persona'] = persona['name']
                    st.rerun()
    
    # Check match button
    if st.session_state.game_state['selected_problem'] and st.session_state.game_state['selected_persona']:
        if st.button("✅ Check Match", use_container_width=True):
            check_match()

def check_match():
    """Check if the selected problem-persona match is correct"""
    problem_id = st.session_state.game_state['selected_problem']
    persona_name = st.session_state.game_state['selected_persona']
    
    problem = next(p for p in PROBLEMS if p['id'] == problem_id)
    correct_persona = problem['correct_persona']
    
    is_correct = persona_name == correct_persona
    
    # Update game state
    st.session_state.game_state['matches'][problem_id] = persona_name
    
    if is_correct:
        st.session_state.game_state['score'] += 10
        st.session_state.game_state['completed_problems'].add(problem_id)
        st.session_state.game_state['current_mission'] = problem_id
        
        # Show success feedback
        st.markdown(f"""
        <div class="feedback-success">
            <h3>✅ Correct Match!</h3>
            <p>Great job! You correctly matched <strong>{problem['title']}</strong> to <strong>{persona_name}</strong>.</p>
            <p><strong>Explanation:</strong> {persona_name} is responsible for {problem['category'].lower()} and can effectively address this challenge.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if game is complete
        if len(st.session_state.game_state['completed_problems']) == len(PROBLEMS):
            time.sleep(2)
            st.session_state.game_state['current_screen'] = 'results'
            st.rerun()
        else:
            # Show mini-mission
            st.session_state.game_state['current_screen'] = 'mission'
            st.rerun()
    else:
        # Show error feedback
        st.markdown(f"""
        <div class="feedback-error">
            <h3>❌ Incorrect Match</h3>
            <p>The correct persona for <strong>{problem['title']}</strong> is <strong>{correct_persona}</strong>.</p>
            <p><strong>Explanation:</strong> {correct_persona} specializes in {problem['category'].lower()} and is best suited to handle this challenge.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Clear selections
    st.session_state.game_state['selected_problem'] = None
    st.session_state.game_state['selected_persona'] = None

def render_mission_screen():
    """Render the mini-mission screen"""
    mission_id = st.session_state.game_state['current_mission']
    mission = MINI_MISSIONS[mission_id]
    
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Mini-Mission</h1>
        <p>Test your FinOps knowledge with a quick scenario!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="mission-card">
        <h2>{mission['title']}</h2>
        <p><strong>Question:</strong> {mission['question']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mission options
    selected_option = st.radio(
        "Choose the best answer:",
        [f"{opt['id'].upper()}. {opt['text']}" for opt in mission['options']],
        key="mission_radio"
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🚀 Submit Answer", use_container_width=True):
            # Check answer
            selected_id = selected_option[0].lower()
            correct_option = next(opt for opt in mission['options'] if opt['correct'])
            
            if selected_id == correct_option['id']:
                st.session_state.game_state['score'] += 5
                st.markdown("""
                <div class="feedback-success">
                    <h3>🎯 Mission Accomplished!</h3>
                    <p>Great job! You chose the correct action.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="feedback-error">
                    <h3>❌ Mission Failed</h3>
                    <p>The correct answer was: <strong>{correct_option['id'].upper()}. {correct_option['text']}</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            time.sleep(2)
            st.session_state.game_state['current_mission'] = None
            st.session_state.game_state['current_screen'] = 'game'
            st.rerun()
    
    with col3:
        if st.button("⏭️ Skip Mission", use_container_width=True):
            st.session_state.game_state['current_mission'] = None
            st.session_state.game_state['current_screen'] = 'game'
            st.rerun()

def render_results_screen():
    """Render the results screen"""
    st.markdown("""
    <div class="main-header">
        <h1>🏆 Game Complete!</h1>
        <p>Congratulations on completing FinOps City: Match & Solve!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final score
    max_score = len(PROBLEMS) * 15  # 10 for match + 5 for mission
    final_score = st.session_state.game_state['score']
    
    col1, col2, col3 = st.columns(3)
    
    with col2:
        st.markdown(f"""
        <div class="score-display">
            <h2>Final Score</h2>
            <h1>{final_score}/{max_score}</h1>
            <p>{'🎉 Excellent!' if final_score >= max_score * 0.8 else '👍 Good job!' if final_score >= max_score * 0.6 else '📚 Keep learning!'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Match summary
    st.markdown("### 📊 Match Summary")
    for problem in PROBLEMS:
        matched_persona = st.session_state.game_state['matches'].get(problem['id'])
        is_correct = matched_persona == problem['correct_persona']
        
        summary_class = "match-summary-item"
        if not is_correct:
            summary_class += " incorrect"
        
        st.markdown(f"""
        <div class="{summary_class}">
            <h4>{problem['title']}</h4>
            <p><strong>Your match:</strong> {matched_persona or 'Not matched'}</p>
            <p><strong>Correct answer:</strong> {problem['correct_persona']}</p>
            <p><strong>Status:</strong> {'✅ Correct' if is_correct else '❌ Incorrect'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Learning outcomes
    st.markdown("### 🎓 Key Learning Outcomes")
    st.markdown("""
    - **FinOps Collaboration**: Understanding how different personas work together
    - **Role Clarity**: Clear distinction between Core and Allied FinOps personas
    - **Problem-Solving**: How to approach different cloud cost challenges
    - **Best Practices**: Practical strategies for cost optimization and governance
    """)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.game_state = {
                'current_screen': 'game',
                'score': 0,
                'matches': {},
                'completed_problems': set(),
                'current_mission': None,
                'selected_problem': None,
                'selected_persona': None
            }
            st.rerun()
    
    with col2:
        if st.button("🏠 Back to Start", use_container_width=True):
            st.session_state.game_state['current_screen'] = 'start'
            st.rerun()

# Main app logic
def main():
    current_screen = st.session_state.game_state['current_screen']
    
    if current_screen == 'start':
        render_start_screen()
    elif current_screen == 'game':
        render_game_screen()
    elif current_screen == 'mission':
        render_mission_screen()
    elif current_screen == 'results':
        render_results_screen()

if __name__ == "__main__":
    main() 