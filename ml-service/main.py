from fastapi import FastAPI, UploadFile, File, Form
from pdf_parser import extract_text_from_pdf
from analyzer import analyze
import shutil

app = FastAPI()


@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    result = analyze(resume_text, job_description)

    return result