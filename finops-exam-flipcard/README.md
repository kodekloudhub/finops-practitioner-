# FinOps Exam Flip Cards

A Streamlit-based flip card web app for studying FinOps concepts. The app displays interactive flip cards with questions and answers. Click on any card to flip and reveal the answer!

## Features
- Streamlit backend and frontend
- Interactive flip cards with colorful design
- Shuffle and reset functionality
- Responsive grid layout
- All card data loaded from JSON file

## How to Run

### Option 1: Direct Streamlit Run

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```sh
   streamlit run streamlit_app.py
   ```

3. **Open your browser:**
   The app will automatically open at [http://localhost:8501](http://localhost:8501)

### Option 2: Docker (if you prefer)

1. **Build the Docker image:**
   ```sh
   docker build -t finops-flipcards .
   ```

2. **Run the container:**
   ```sh
   docker run -p 8501:8501 finops-flipcards
   ```

3. **Open your browser:**
   Visit [http://localhost:8501](http://localhost:8501)

## Project Structure

- `streamlit_app.py` - Main Streamlit application
- `flipcards.json` - Flip card data (questions and answers)
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container setup (optional)

## Usage

- Click on any card to flip it and see the answer
- Use the "Shuffle & Reset All Cards" button to randomize the order and reset all cards
- Cards are automatically shuffled on first load for variety

---

Feel free to customize the card data in `flipcards.json`! 