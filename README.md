# Developer Skill Gap Analyzer

Welcome to the Developer Skill Gap Analyzer! This tool helps you discover your learning path and close your skill gaps by analyzing your resume against job descriptions and optionally your GitHub profile.

## Project Structure

This project is divided into three main components:

1. **`ml-service` (Python/FastAPI)**
   - Handles resume parsing, text extraction, and machine learning based skill matching.
2. **`backend-node` (Node.js/Express)**
   - The main API gateway that connects the frontend to the ML service and external APIs (like GitHub).
3. **`frontend` (React)**
   - The user interface for uploading resumes, entering job descriptions, and viewing analysis results.

## How to Run

You will need to open three separate terminals to run all services simultaneously.

### 1. ML Service
```bash
cd ml-service
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```
Runs on `http://127.0.0.1:8000`

### 2. Backend Service
```bash
cd backend-node
npm install
npm start
```
Runs on `http://localhost:5000`

### 3. Frontend Service
```bash
cd frontend
npm install
npm start
```
Runs on `http://localhost:3000`

## Features
- **Resume Analysis**: Upload your PDF resume to extract skills.
- **Job Matching**: Compare your skills against a target job description.
- **GitHub Integration**: Add your GitHub username to automatically fetch programming languages and skills from your public repositories.
- **Learning Path**: Get actionable, prioritized steps to bridge the gap between your current skills and your dream job.

Crafted by Aryan Vishala 😁
