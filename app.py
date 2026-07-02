from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from analyzer import analyze_resume
import os

app = Flask(__name__)

# ==========================
# Upload Folder Configuration
# ==========================

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ==========================
# Check Allowed File
# ==========================

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Analyze Resume
# ==========================

@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No file uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a PDF file."

    if not allowed_file(file.filename):
        return "Only PDF files are allowed."

    filename = secure_filename(file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    # Analyze the Resume
    result = analyze_resume(filepath)

    return render_template(
        "result.html",

        filename=filename,

        overall_score=result["overall_score"],

        recommended_role=result["recommended_role"],

        confidence=result["confidence"],

        role_scores=result["role_scores"],

        found_skills=result["found_skills"],

        missing_skills=result["missing_skills"],

        section_scores=result["section_scores"],

        strengths=result["strengths"],

        improvements=result["improvements"],

        suggestions=result["suggestions"],

        summary=result["summary"]
    )


# ==========================
# Run Flask Application
# ==========================

if __name__ == "__main__":
    app.run(debug=True)