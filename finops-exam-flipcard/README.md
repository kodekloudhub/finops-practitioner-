# Flip Cards App

A simple flip card web app built with FastAPI, HTML, CSS, and JavaScript. The app displays 10 flip cards. Click a card to flip and reveal its back content. All card data is loaded from a JSON file.

## Features
- FastAPI backend
- 10 interactive flip cards
- Responsive frontend (HTML/CSS/JS)
- Dockerized for easy deployment

## How to Run (with Docker)

1. **Build the Docker image:**

   ```sh
   docker build -t flipcards-app .
   ```

2. **Run the container:**

   ```sh
   docker run -p 8000:8000 flipcards-app
   ```

3. **Open your browser:**

   Visit [http://localhost:8000](http://localhost:8000)

---

## Project Structure

- `main.py` - FastAPI backend
- `flipcards.json` - Flip card data
- `static/` - Frontend files (HTML, CSS, JS)
- `Dockerfile` - Container setup

---

Feel free to customize the card data in `flipcards.json`! 