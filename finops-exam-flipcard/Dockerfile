FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
COPY streamlit_app.py ./
COPY flipcards.json ./

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"] 