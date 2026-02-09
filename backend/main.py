from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_llama(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

@app.post("/extract/")
def extract_medical_info(note: str = Form(...)):
    prompt = (
 f"""
You are given a doctor's clinical note. Extract the key information listed below and return the result strictly in valid JSON format.

Required Fields to Extract:
- Symptoms
- Diagnosis
- Medications
- Follow-up Instructions

Instructions:
- Use only the information explicitly mentioned in the note.
- If any field is not present, return it as an empty string or empty list where appropriate.
- Do not include any explanations outside the JSON output.
- Do not include any extra word at the first of JSON output.

Doctor's Note:
{note}
"""
    )

    structured_data = query_llama(prompt)
    return {"structured": structured_data}




#for batch processing https://chatgpt.com/share/6989922e-112c-8003-a476-89273fd84877