from flask import Flask, render_template, request, jsonify
import re
import math
from collections import Counter

app = Flask(__name__)

# ---------------------------------------------------------
# AI Text Summarizer & Viva Question Generator Engine
# Uses Extractive NLP (TF-IDF Scoring) + Keyword Extraction
# ---------------------------------------------------------

STOPWORDS = {
    "the", "is", "in", "and", "to", "of", "a", "for", "on", "with", "as",
    "by", "at", "an", "be", "this", "that", "from", "or", "are", "it",
    "was", "were", "can", "will", "has", "have", "had", "not", "but", "what",
    "which", "their", "they", "we", "you", "your", "our", "its", "also", "used"
}

def clean_and_tokenize(text):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    return [w for w in words if w not in STOPWORDS]

def generate_summary(text, num_sentences=3):
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if len(s.strip()) > 15]
    if len(sentences) <= num_sentences:
        return " ".join(sentences)

    words = clean_and_tokenize(text)
    if not words:
        return " ".join(sentences[:num_sentences])

    word_freq = Counter(words)
    max_freq = max(word_freq.values())
    for w in word_freq:
        word_freq[w] = word_freq[w] / max_freq

    sentence_scores = {}
    for idx, sentence in enumerate(sentences):
        s_words = clean_and_tokenize(sentence)
        if not s_words:
            continue
        score = sum(word_freq.get(w, 0) for w in s_words) / math.sqrt(len(s_words))
        sentence_scores[idx] = score

    top_indices = sorted(
        sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    )
    return " ".join([sentences[i] for i in top_indices])

def extract_keywords(text, top_n=6):
    words = clean_and_tokenize(text)
    freq = Counter(words)
    return [word.capitalize() for word, _ in freq.most_common(top_n)]

def generate_viva_questions(text):
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if len(s.strip()) > 20]
    keywords = extract_keywords(text, top_n=5)
    questions = []

    for kw in keywords:
        matching_sentence = next((s for s in sentences if kw.lower() in s.lower()), None)
        if matching_sentence:
            questions.append({
                "question": f"What is the role or meaning of '{kw}' based on your notes?",
                "answer": matching_sentence
            })

    if not questions and sentences:
        questions.append({
            "question": "Explain the main concept of this topic in your own words.",
            "answer": sentences[0]
        })

    return questions[:5]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    notes = data.get("notes", "").strip()

    if len(notes) < 40:
        return jsonify({"error": "Please enter at least 2-3 sentences of study notes."}), 400

    summary = generate_summary(notes, num_sentences=3)
    keywords = extract_keywords(notes, top_n=6)
    viva_qa = generate_viva_questions(notes)

    return jsonify({
        "summary": summary,
        "keywords": keywords,
        "viva_qa": viva_qa,
        "word_count": len(notes.split())
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
