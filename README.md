# AI Smart Study & Viva Assistant (Minor Project)

## 1. Problem Statement
Students often struggle to revise lengthy lecture notes quickly before internal exams and practical viva sessions. Manually reading long paragraphs, finding key terms, and preparing expected viva questions takes a lot of time.

## 2. Solution Overview
**AI Smart Study & Viva Assistant** is a lightweight AI-powered web application that solves this real-time student problem. Users simply paste their study notes or topic text, and the system automatically generates:
1. **AI Extractive Summary** (using TF-IDF sentence scoring)
2. **Important Keywords & Concepts**
3. **Auto-Generated Viva Questions & Answers**

## 3. Tech Stack Used
- **Backend:** Python 3, Flask
- **AI / NLP Logic:** Natural Language Processing (Stopword Filtering, Term Frequency-Inverse Document Frequency / TF-IDF Sentence Scoring, Keyword Extraction)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)

## 4. How to Run Locally
1. Install Flask:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser and visit:
   `http://127.0.0.1:5000`

## 5. Project Structure
```text
AI-Smart-Study-Assistant/
├── app.py               # Flask server & AI/NLP summarization engine
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation for GitHub
├── templates/
│   └── index.html       # Frontend user interface
└── static/
    └── style.css        # Styling and responsive layout
```

## 6. Author
- **Name:** Utkarsh Singh
- **Course:** BCA 3rd Year, Shri Ramswaroop Memorial University (SRMU)
