import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if token.is_alpha and not token.is_stop]

def analyze_resume(resume_text, job_description):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    combined = [' '.join(resume_keywords), ' '.join(job_keywords)]

    vectorizer = CountVectorizer().fit_transform(combined)
    score = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]

    missing = list(set(job_keywords) - set(resume_keywords))

    suggestions = [f"Add keyword: {word}" for word in missing[:10]]

    return {
        "score": round(score * 100, 2),
        "missing_skills": ', '.join(missing[:10]),
        "suggestions": suggestions
    }
