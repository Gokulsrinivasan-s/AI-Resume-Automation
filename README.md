# 🤖 AI Resume Automation

An AI-powered recruitment automation system that automatically analyzes resumes, matches them with a Job Description (JD), calculates a matching score, and sends selection or rejection emails based on the score.

---

## 📌 Project Overview

Recruiters often spend a lot of time manually reviewing resumes. This project automates the recruitment process by:

- Reading candidate details from Google Forms responses.
- Downloading candidate resumes from Google Drive.
- Extracting text from PDF resumes.
- Comparing resumes with the Job Description using AI/NLP.
- Calculating a resume matching score.
- Automatically sending emails to selected candidates.

---

## 🚀 Features

- ✅ Read candidate details from CSV (Google Forms responses)
- ✅ Download resumes automatically from Google Drive
- ✅ Extract text from PDF resumes
- ✅ Compare Resume and Job Description
- ✅ Calculate resume matching score
- ✅ Select candidates based on score threshold
- ✅ Automatically send selection/rejection emails
- ✅ Process multiple candidates in a single run

---

## 🛠️ Technologies Used

- Python
- Pandas
- PDF Processing
- Natural Language Processing (NLP)
- Google Drive Integration
- Google Forms
- Email Automation
- SMTP
- Git & GitHub

---

## 📂 Project Structure

```text
AI Resume Automation/
│
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│
├── responses.csv
├── csv_reader.py
├── resume_downloader.py
├── resume_parser.py
├── jd_matcher.py
├── email_sender.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Workflow

```text
Google Form
      │
      ▼
Responses CSV
      │
      ▼
Read Candidate Details
      │
      ▼
Download Resume
      │
      ▼
Extract PDF Text
      │
      ▼
Compare with Job Description
      │
      ▼
Calculate Matching Score
      │
      ▼
Decision
   ┌──────────────┐
   │ Score ≥ Threshold │
   └──────────────┘
      │
      ▼
Send Selection Email
      │
      ▼
Otherwise
      │
      ▼
Send Rejection Email
```

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Gokulsrinivasan-s/AI-Resume-Automation.git
```

Move into the project folder:

```bash
cd AI-Resume-Automation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📊 Future Improvements

- Web dashboard using Streamlit or FastAPI
- AI-powered skill extraction
- Resume ranking dashboard
- Interview scheduling automation
- Recruiter analytics dashboard
- LLM-based resume analysis
- Multi-job description support

---

## 🎯 Learning Outcomes

This project helped me learn:

- Python automation
- Data processing with Pandas
- PDF text extraction
- Natural Language Processing (NLP)
- Email automation
- Working with Google Forms and Google Drive
- End-to-end AI workflow development
- Git and GitHub project management

---

## 👨‍💻 Author

**Gokul S**

Aspiring AI Engineer | Machine Learning Engineer | Generative AI Enthusiast

GitHub: https://github.com/Gokulsrinivasan-s
