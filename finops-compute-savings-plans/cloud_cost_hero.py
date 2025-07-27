import streamlit as st
import random
import time
from datetime import datetime, timedelta

# Constants
PERSONAS = [
    {"name": "Steady SaaS", "base_rate": 2.0, "spike_prob": 0.15, "spike_factor": 2.0},
    {"name": "Spiky Batch", "base_rate": 1.0, "spike_prob": 0.35, "spike_factor": 4.0},
    {"name": "Weekend Peak", "base_rate": 1.5, "spike_prob": 0.25, "spike_factor": 3.5},
]

ON_DEMAND_RATE = 0.05  # $/GB-hour
TOTAL_HOURS = 720  # 30 days * 24 hours

def generate_usage(persona, hour):
    """Generate RAM usage for a given hour based on persona characteristics"""
    base = persona["base_rate"]
    if random.random() < persona["spike_prob"]:
        return base * persona["spike_factor"]
    return base

def calculate_costs(usage_log, commit):
    """Calculate all cost metrics"""
    total_usage = sum(usage_log)
    on_demand_cost = total_usage * ON_DEMAND_RATE
    savings_plan_cost = commit * TOTAL_HOURS
    overage_cost = max(0, total_usage - commit * TOTAL_HOURS) * ON_DEMAND_RATE
    total_cost = savings_plan_cost + overage_cost
    savings_pct = (on_demand_cost - total_cost) / on_demand_cost * 100 if on_demand_cost > 0 else 0
    
    return {
        "on_demand_cost": on_demand_cost,
        "savings_plan_cost": savings_plan_cost,
        "overage_cost": overage_cost,
        "total_cost": total_cost,
        "savings_pct": savings_pct
    }

def generate_full_simulation(persona):
    """Generate complete 30-day simulation data"""
    full_usage = []
    for hour in range(TOTAL_HOURS):
        usage = generate_usage(persona, hour)
        full_usage.append(usage)
    return full_usage

def initialize_game():
    """Initialize or reset the game state"""
    if "persona" not in st.session_state:
        st.session_state.persona = random.choice(PERSONAS)
    if "usage_log" not in st.session_state:
        st.session_state.usage_log = []
    if "commit" not in st.session_state:
        st.session_state.commit = 1.0
    if "locked" not in st.session_state:
        st.session_state.locked = False
    if "tick" not in st.session_state:
        st.session_state.tick = 0
    if "game_complete" not in st.session_state:
        st.session_state.game_complete = False

def reset_game():
    """Reset the game state for a new game"""
    for key in ["persona", "usage_log", "commit", "locked", "tick", "game_complete"]:
        if key in st.session_state:
            del st.session_state[key]
    initialize_game()

def main():
    st.set_page_config(
        page_title="Cloud Cost Hero",
        page_icon="🎮",
        layout="wide"
    )
    
    # Initialize game state
    initialize_game()
    
    # Title
    st.title("🎮 Cloud Cost Hero")
    st.markdown("**Minimize your 30-day AWS bill by choosing the right Compute Savings Plan!**")
    
    # Game Instructions
    with st.expander("📖 How to Play", expanded=True):
        st.markdown("""
        **🎯 Your Mission:** Choose the optimal hourly commitment for your Compute Savings Plan to minimize costs!
        
        **📚 What are Compute Savings Plans?**
        AWS Compute Savings Plans offer discounted rates in exchange for a consistent hourly spend commitment. You commit to spending a certain amount per hour, and AWS gives you a discount on your RAM usage.
        
        **📊 Step 1:** Watch the live usage simulation for at least 5 data points to understand your startup's pattern
        **💰 Step 2:** Set your hourly commitment using the slider (how much you'll pay per hour)
        **🔒 Step 3:** Lock in your plan when you're confident
        **🏆 Step 4:** See your final bill and savings percentage!
        
        **💡 Pro Tips:**
        - **Higher commitment** = lower per-hour cost but you pay even when not using
        - **Lower commitment** = pay only for what you use, but higher per-hour cost
        - **Watch for usage spikes** to avoid expensive overage charges
        - **Aim for 30%+ savings** to get the balloons celebration! 🎈
        """)
    
    # Persona Card
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.info(f"**Startup:** {st.session_state.persona['name']}")
        with col2:
            st.write(f"Base usage: {st.session_state.persona['base_rate']:.1f} GB RAM/hour")
            st.write(f"Spike probability: {st.session_state.persona['spike_prob']*100:.0f}% (higher = more spikes)")
            st.write(f"Spike factor: {st.session_state.persona['spike_factor']}x (higher = bigger spikes)")
            
            # Add persona-specific guidance
            if st.session_state.persona['name'] == "Steady SaaS":
                st.caption("💡 Moderate spikes, good for learning")
            elif st.session_state.persona['name'] == "Spiky Batch":
                st.caption("💡 Frequent large spikes - watch out!")
            elif st.session_state.persona['name'] == "Weekend Peak":
                st.caption("💡 Occasional big spikes - plan carefully")
    
    # Live Usage Chart
    st.subheader("📊 Live RAM Usage Simulation")
    
    # Guidance for decision making
    if len(st.session_state.usage_log) < 5:
        st.warning(f"⏳ **Please observe {5 - len(st.session_state.usage_log)} more data points** before making your decision!")
        st.info("📊 **Why 5 data points?** This helps you understand the usage pattern, including any spikes or variations.")
        
        # Progress bar for data collection
        progress = len(st.session_state.usage_log) / 5
        st.progress(progress, text=f"Data points collected: {len(st.session_state.usage_log)}/5")
    elif len(st.session_state.usage_log) == 5:
        st.success("✅ **Perfect!** You've observed 5 data points. Now analyze the pattern and set your commitment!")
    else:
        st.success("✅ **Ready to decide!** You've observed the RAM usage pattern. Set your commitment and lock in your plan!")
    
    if st.session_state.usage_log:
        # Show last 50 points for responsiveness
        chart_data = st.session_state.usage_log[-50:]
        
        # Create a DataFrame for better chart display
        import pandas as pd
        df = pd.DataFrame({
            'RAM Usage (GB)': chart_data,
            'Hour': range(len(chart_data))
        })
        
        # Enhanced chart with better styling
        st.line_chart(df.set_index('Hour'))
        
        # Show current usage stats
        col1, col2, col3 = st.columns(3)
        with col1:
            current_usage = st.session_state.usage_log[-1]
            st.metric("Current Usage", f"{current_usage:.2f} GB RAM")
        with col2:
            avg_usage = sum(st.session_state.usage_log)/len(st.session_state.usage_log)
            st.metric("Average Usage", f"{avg_usage:.2f} GB RAM")
        with col3:
            peak_usage = max(st.session_state.usage_log)
            st.metric("Peak Usage", f"{peak_usage:.2f} GB RAM")
        
        # Show spike detection
        if len(st.session_state.usage_log) >= 2:
            recent_usage = st.session_state.usage_log[-3:]  # Last 3 points
            avg_recent = sum(recent_usage) / len(recent_usage)
            if current_usage > avg_recent * 1.5:
                st.warning("🚨 **SPIKE DETECTED!** Current usage is significantly higher than recent average.")
            elif current_usage < avg_recent * 0.7:
                st.info("📉 **LOW USAGE** - Current usage is below recent average.")
    else:
        st.write("Usage data will appear here as the simulation runs...")
    
    # Game Controls
    st.subheader("🎯 Set Your Savings Plan")
    
    if not st.session_state.locked:
        # Pre-lock controls
        col1, col2 = st.columns([2, 1])
        with col1:
            st.session_state.commit = st.slider(
                "Hourly commitment ($)", 
                min_value=0.0, 
                max_value=5.0, 
                value=st.session_state.commit, 
                step=0.1,
                help="Set your hourly commitment for the Compute Savings Plan (how much you'll pay per hour for RAM)"
            )
        with col2:
            # Disable lock button until 5 data points are observed
            can_lock = len(st.session_state.usage_log) >= 5
            if st.button("🔒 Lock-in Plan", type="primary", disabled=not can_lock):
                st.session_state.locked = True
                st.rerun()
            
            if not can_lock:
                st.caption("⏳ Wait for 5 data points")
        
        # Show current projection
        if st.session_state.usage_log:
            costs = calculate_costs(st.session_state.usage_log, st.session_state.commit)
            st.metric(
                "Current Projection", 
                f"${costs['total_cost']:,.2f}",
                delta=f"{costs['savings_pct']:.1f}% savings"
            )
            
            # Commitment guidance
            avg_usage = sum(st.session_state.usage_log) / len(st.session_state.usage_log)
            if st.session_state.commit < avg_usage * 0.8:
                st.warning("⚠️ **Low commitment:** You might face expensive overage charges during RAM spikes!")
            elif st.session_state.commit > avg_usage * 1.5:
                st.info("ℹ️ **High commitment:** You're paying for more RAM than you typically use.")
            else:
                st.success("✅ **Good balance:** Your commitment aligns well with current RAM usage patterns!")
    else:
        # Post-lock display
        st.success("✅ Plan locked! Jumping to results...")
        st.metric(
            "Locked Commitment", 
            f"${st.session_state.commit:.1f}/hour"
        )
    
    # Progress Bar
    progress = st.session_state.tick / TOTAL_HOURS
    st.progress(progress, text=f"Day {st.session_state.tick // 24 + 1}/30 - Hour {st.session_state.tick % 24 + 1}/24")
    
    # Simulation Logic
    if not st.session_state.game_complete:
        if st.session_state.tick < TOTAL_HOURS:
            # Generate usage for current hour
            usage = generate_usage(st.session_state.persona, st.session_state.tick)
            st.session_state.usage_log.append(usage)
            st.session_state.tick += 1
            
            # Control simulation speed
            if st.session_state.locked:
                # Jump to results immediately after lock
                st.session_state.usage_log = generate_full_simulation(st.session_state.persona)
                st.session_state.tick = TOTAL_HOURS
                st.session_state.game_complete = True
                st.rerun()
            else:
                time.sleep(1)  # Faster simulation to show spikes quickly
            
            st.rerun()
        else:
            # Game complete
            st.session_state.game_complete = True
            st.rerun()
    
    # Results Display
    if st.session_state.game_complete:
        st.subheader("🏆 Final Results")
        
        costs = calculate_costs(st.session_state.usage_log, st.session_state.commit)
        
        # Results metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "On-Demand Cost", 
                f"${costs['on_demand_cost']:,.2f}"
            )
        with col2:
            st.metric(
                "Your Total Cost", 
                f"${costs['total_cost']:,.2f}",
                delta=f"{costs['savings_pct']:.1f}% savings"
            )
        with col3:
            st.metric(
                "Amount Saved", 
                f"${costs['on_demand_cost'] - costs['total_cost']:,.2f}"
            )
        
        # Cost breakdown
        st.subheader("💰 Cost Breakdown")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Savings Plan Cost", f"${costs['savings_plan_cost']:,.2f}")
        with col2:
            st.metric("Overage Cost", f"${costs['overage_cost']:,.2f}")
        
        # Feedback
        if costs['savings_pct'] >= 30:
            st.balloons()
            st.success("🎉 Excellent! You saved 30% or more!")
        elif costs['savings_pct'] > 0:
            st.info(f"Good job! You saved {costs['savings_pct']:.1f}%")
        elif costs['savings_pct'] < 0:
            st.error("❌ You paid more than On-Demand! Try a lower commitment next time.")
        else:
            st.warning("You broke even. Consider adjusting your commitment.")
        
        # Usage statistics
        st.subheader("📈 RAM Usage Statistics")
        total_usage = sum(st.session_state.usage_log)
        avg_usage = total_usage / len(st.session_state.usage_log)
        max_usage = max(st.session_state.usage_log)
        min_usage = min(st.session_state.usage_log)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Usage", f"{total_usage:,.1f} GB-hours")
        with col2:
            st.metric("Average/Hour", f"{avg_usage:.2f} GB RAM")
        with col3:
            st.metric("Peak Usage", f"{max_usage:.2f} GB RAM")
        with col4:
            st.metric("Min Usage", f"{min_usage:.2f} GB RAM")
    
    # Replay Button
    if st.session_state.game_complete:
        st.subheader("🔄 Play Again")
        if st.button("🎮 New Game", type="primary"):
            reset_game()
            st.rerun()

if __name__ == "__main__":
    main() 