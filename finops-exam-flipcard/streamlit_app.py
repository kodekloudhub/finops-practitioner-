import streamlit as st
import json
import random

# Load flip card data
@st.cache_data
def load_flipcards():
    with open("flipcards.json", "r") as f:
        return json.load(f)

def main():
    st.set_page_config(
        page_title="FinOps Exam Flip Cards",
        page_icon="🃏",
        layout="wide"
    )
    
    st.title("🃏 FinOps Exam Flip Cards")
    st.markdown("Click on any card to flip and reveal the answer!")
    
    # Load cards
    cards = load_flipcards()
    
    # Shuffle cards for variety
    if 'shuffled_cards' not in st.session_state:
        st.session_state.shuffled_cards = cards.copy()
        random.shuffle(st.session_state.shuffled_cards)
    
    # Create a grid layout
    cols = st.columns(5)
    
    # Display cards in a 5-column grid
    for i, card in enumerate(st.session_state.shuffled_cards):
        col_idx = i % 5
        with cols[col_idx]:
            # Create a unique key for each card
            card_key = f"card_{i}"
            
            # Initialize card state
            if card_key not in st.session_state:
                st.session_state[card_key] = False
            
            # Card styling
            if st.session_state[card_key]:
                # Show back of card
                st.markdown(
                    f"""
                    <div style="
                        background: white;
                        border: 2px solid #ddd;
                        border-radius: 10px;
                        padding: 20px;
                        margin: 10px 0;
                        min-height: 200px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        text-align: center;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        cursor: pointer;
                    ">
                        <div style="font-size: 14px; color: #333;">
                            {card['back']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # Show front of card
                colors = [
                    "#2196f3", "#e91e63", "#ff9800", "#4caf50", "#9c27b0",
                    "#00bcd4", "#ffeb3b", "#f44336", "#8bc34a", "#ff5722"
                ]
                color = colors[i % len(colors)]
                text_color = "#333" if color == "#ffeb3b" else "#fff"
                
                st.markdown(
                    f"""
                    <div style="
                        background: {color};
                        border: 2px solid {color};
                        border-radius: 10px;
                        padding: 20px;
                        margin: 10px 0;
                        min-height: 200px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        text-align: center;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        cursor: pointer;
                    ">
                        <div style="font-size: 14px; color: {text_color}; font-weight: bold;">
                            {card['front']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Click handler
            if st.button(f"Flip Card {i+1}", key=f"btn_{i}", use_container_width=True):
                st.session_state[card_key] = not st.session_state[card_key]
                st.rerun()
    
    # Add some spacing
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Reset button
    if st.button("🔄 Shuffle & Reset All Cards", use_container_width=True):
        # Clear all card states
        for key in list(st.session_state.keys()):
            if key.startswith("card_"):
                del st.session_state[key]
        # Reshuffle cards
        st.session_state.shuffled_cards = cards.copy()
        random.shuffle(st.session_state.shuffled_cards)
        st.rerun()

if __name__ == "__main__":
    main() 