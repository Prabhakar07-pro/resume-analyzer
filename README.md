# Resume Analyzer

A full-stack Resume Analyzer web application that extracts skills from uploaded resumes and recommends suitable job roles with match percentages.

## 🔗 Live Demo
👉 https://resume-analyzer-dr6t.onrender.com

## 🚀 Features
- Resume upload (PDF)
- Automatic skill extraction
- Role recommendation engine
- Match percentage calculation
- Clean and responsive UI

## 🛠 Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript

## 📂 Project Structure
- `app/` – FastAPI application entry point  
- `parsing/` – Resume parsing logic  
- `extraction/` – Skill extraction  
- `recommendation/` – Role matching logic  
- `templates/` – HTML templates  
- `static/` – CSS styles  

## ▶️ Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
