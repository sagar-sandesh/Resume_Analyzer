# 📄 Resume Analyzer App 🔍

A smart web-based tool that analyzes resumes against job descriptions using **Natural Language Processing**. Built with **Flask**, **spaCy**, and **scikit-learn**, this app calculates a **match score**, suggests **missing keywords**, and helps job seekers optimize their resumes.

---

## 🚀 Features

- 🗂 Upload PDF resumes via a clean web interface
- 💬 Paste job descriptions into the form
- 🧠 NLP-powered keyword analysis using spaCy
- 📊 Match scoring using cosine similarity
- 💡 Highlights missing keywords and gives smart suggestions
- 🖥️ Shows results clearly on a separate result page

---

## 🖼️ Web Interface Preview

### 🔘 Upload Page

----
html
<form action="/analyze" method="post" enctype="multipart/form-data">
    <input type="file" name="resume">
    <textarea name="jobdesc"></textarea>
    <input type="submit" value="Analyze">
</form>

<p><strong>Match Score:</strong> 72.5%</p>
<p><strong>Missing Skills:</strong> django, sql, docker</p>

<ul>
  <li>Add keyword: django</li>
  <li>Add keyword: sql</li>
  <li>Add keyword: docker</li>
</ul>

----

## 🛠 Tech Stack 
- Backend	   :                                 Flask
- NLP Processing :	                            spaCy (en_core_web_sm)
- PDF Handling :	                            pdfminer.six
- Matching Engine :	                            scikit-learn (Cosine Similarity)
- Frontend :	                                HTML (with Jinja2 templating)

----
## 📁 Project Structure
graphql
Copy
Edit
resume-analyzer/
- ├── app.py                    # Flask server with routes
- ├── analyzer.py               # Core NLP and keyword analysis
- ├── resume_parser.py          # Extracts text from PDFs
- ├── requirements.txt          # Python dependencies
- │
- ├── templates/
- │   ├── index.html            # Upload form
- │   └── result.html           # Display results
- │
- ├── static/                   # Optional: styles/im

----
## ⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer

2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
python -m spacy download en_core_web_sm

4. Run the Flask App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 to use the app.

----
## ✅ How It Works
User uploads a PDF resume and pastes a job description.

resume_parser.py extracts text from PDF.

analyzer.py:

Extracts and compares keywords.

Computes cosine similarity.

Identifies missing keywords.

Flask returns results on a new HTML page (result.html).

----
## 🧠 Future Improvements
📦 Downloadable report (PDF/CSV)

🧠 GPT-powered enhancement tips

🧾 Upload job description as file

🧑‍💼 Support multiple resume evaluation

----
## 📄 License
MIT License © 2025 [Your Name]

## 🙌 Author
