from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files['resume']
    job_desc = request.form['jobdesc']

    resume_text = extract_text_from_pdf(resume)
    results = analyze_resume(resume_text, job_desc)

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
