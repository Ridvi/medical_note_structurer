# Medical Note Structuring Assistant – HealthCare+ Clinic

An AI-powered application that converts **unstructured clinical notes** into clean, structured medical data using **LLaMA 2** via Ollama.

This tool helps healthcare professionals transform free‑form doctor notes into standardized formats suitable for EMR systems, analytics, and reporting.

---

## 🏥 Real-World Healthcare Context

At **HealthCare+ Clinic**, physicians often write patient notes in natural language during consultations. These notes:

* Vary widely in structure
* Contain critical clinical information
* Are difficult to analyze automatically
* Require manual effort to organize

This project automates that process using AI.

---

## 🚨 The Problem

* Clinical notes are inconsistent and unstructured
* Important details are buried in long text
* Extracting data manually is slow and error-prone
* EMR systems require structured input

---

## 🎯 Project Goal

Build a **Medical Note Structuring Assistant** that automatically extracts key medical information from raw clinical notes.

### Input

* CSV file containing raw doctor notes

### Output (for each note)

* Symptoms
* Diagnosis
* Medications
* Follow-up instructions
* Concise structured summary

### Additional Capabilities

* Batch processing of multiple notes
* Export structured results as CSV
* Consistent schema for EMR integration

---

## 🧠 Model Used

**LLaMA 2 (via Ollama)**

* Handles complex medical language effectively
* Works well with prompt-based information extraction
* Runs completely locally for privacy and security

> ⚠️ **Important Disclaimer:**
> This project is for **educational and prototyping purposes only** and is NOT a certified medical device. It should not be used for real clinical decision-making without professional oversight.

---

## 🛠️ Technology Stack

| Component       | Technology            |
| --------------- | --------------------- |
| LLM             | LLaMA 2 via Ollama    |
| Backend         | FastAPI               |
| Frontend        | Streamlit             |
| Data Handling   | Pandas + CSV          |
| Output Format   | Structured JSON / CSV |
| Version Control | Git & GitHub          |

---

## ✨ Features

* 🩺 Extract structured medical entities
* 📁 Upload CSV with multiple notes
* ⚡ Automated batch processing
* 📤 Export clean structured datasets
* 🔒 Fully local and privacy-friendly
* 🖥️ Simple interactive UI

---

## 📁 Project Structure

```
medical-note-structurer/
│
├── backend/
│   └── main.py           # FastAPI application
│
├── frontend/
│   └── app.py            # Streamlit interface
│
├── data/
│   └── example_notes.csv
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/medical-note-structurer.git
cd medical-note-structurer
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Install Ollama and Pull Model

Download Ollama from:
[https://ollama.com](https://ollama.com)

Pull the LLaMA 2 model:

```
ollama pull llama2
```

Make sure Ollama is running before starting the app.

---

## ▶️ Running the Application

### Start Backend

```
uvicorn backend.main:app --reload
```

Backend available at:

```
http://127.0.0.1:8000
```

### Start Frontend

```
streamlit run frontend/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🔄 Workflow

1. Upload CSV file with raw clinical notes
2. Each note is processed by LLaMA 2
3. Structured fields are extracted
4. Results displayed in dashboard
5. User downloads structured CSV

---

## ✅ Example Use Cases

* Preparing notes for EMR systems
* Clinical data analysis
* Hospital reporting
* Research dataset preparation
* Reducing administrative workload

