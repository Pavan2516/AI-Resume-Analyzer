# 📄 AI Resume Analyzer

A Flask-based web application that analyzes PDF resumes by extracting technical skills, calculating a resume score, recommending suitable job roles, identifying missing skills, and providing personalized resume improvement suggestions.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🔍 Extract text from PDF resumes
- 💻 Detect technical skills automatically
- 📊 Calculate resume score
- 💼 Recommend suitable job roles
- 📌 Display matched skills for each role
- ⚠️ Identify missing skills for recommended roles
- 💡 Provide resume improvement suggestions
- 🎨 Clean and responsive user interface

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- PDFPlumber

---

## 📁 Project Structure

```
Smart Resume Analyzer/
│
├── app.py
├── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-resume-analyzer.git
```

### 2. Navigate to the project folder

```bash
cd smart-resume-analyzer
```

### 3. Install dependencies

```bash
pip install flask pdfplumber
```

Or, if using the requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📋 How It Works

1. Upload a PDF resume.
2. The application extracts the resume text.
3. Technical skills are detected from the resume.
4. A resume score is calculated.
5. Suitable job roles are recommended based on detected skills.
6. Missing skills for each recommended role are displayed.
7. Personalized suggestions are provided to improve the resume.

---

## 📸 Output

The application displays:

- Resume Score
- Detected Skills
- Recommended Job Roles
- Match Percentage
- Missing Skills
- Resume Improvement Suggestions

---

## 🎯 Future Improvements

- Resume ATS Compatibility Score
- Resume Download as PDF
- Resume Comparison
- Support for DOCX resumes
- Skill Charts and Analytics
- Resume Keyword Highlighting
- Dark Mode
- User Authentication
- Resume History

---

## 👨‍💻 Author

**Pawan Kumar**

GitHub: https://github.com/your-username

LinkedIn: https://www.linkedin.com/in/your-profile

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
