from pdf_parser import extract_text_from_pdf
from analyzer import analyze

resume_text = extract_text_from_pdf("Resume-Sample-1-Software-Engineer.pdf")

job_description = """
Looking for a Python backend developer with experience in:
Python
Docker
AWS
MongoDB
REST APIs
"""

result = analyze(resume_text, job_description)

print(result)