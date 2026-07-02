import pdfplumber
import re

# ==========================================================
# JOB ROLE SKILLS
# ==========================================================

JOB_ROLES = {

    "Python Developer": [
        "python",
        "flask",
        "django",
        "sql",
        "mysql",
        "git",
        "github",
        "rest api",
        "api"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "bootstrap",
        "react",
        "tailwind"
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "python",
        "flask",
        "django",
        "sql",
        "mysql",
        "mongodb",
        "git",
        "github"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "pandas",
        "numpy",
        "matplotlib",
        "power bi"
    ]

}

# ==========================================================
# ALL SKILLS
# ==========================================================

ALL_SKILLS = sorted(list(set(

    skill

    for role in JOB_ROLES.values()

    for skill in role

)))

# ==========================================================
# RESUME SECTIONS
# ==========================================================

SECTIONS = {

    "Career Objective": [
        "career objective",
        "objective",
        "professional summary",
        "summary"
    ],

    "Education": [
        "education",
        "qualification",
        "academic"
    ],

    "Skills": [
        "technical skills",
        "skills"
    ],

    "Projects": [
        "projects",
        "project"
    ],

    "Internships": [
        "internship",
        "experience",
        "work experience"
    ],

    "Certifications": [
        "certification",
        "certifications",
        "certificate"
    ],

    "Achievements": [
        "achievement",
        "achievements"
    ]

}

# ==========================================================
# EXTRACT TEXT FROM PDF
# ==========================================================

def extract_text(filepath):

    text = ""

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text.lower() + "\n"

    return text


# ==========================================================
# FIND SKILLS
# ==========================================================

def detect_skills(resume_text):

    found = []

    missing = []

    for skill in ALL_SKILLS:

        if skill.lower() in resume_text:

            found.append(skill.title())

        else:

            missing.append(skill.title())

    return found, missing


# ==========================================================
# DETECT RESUME SECTIONS
# ==========================================================

def detect_sections(resume_text):

    detected = {}

    for section, keywords in SECTIONS.items():

        detected[section] = False

        for word in keywords:

            if word in resume_text:

                detected[section] = True
                break

    return detected# ==========================================================
# ROLE MATCH SCORE
# ==========================================================

def calculate_role_scores(found_skills):

    role_scores = {}

    best_role = ""
    highest_score = 0

    found_lower = [skill.lower() for skill in found_skills]

    for role, skills in JOB_ROLES.items():

        matched = 0

        for skill in skills:

            if skill.lower() in found_lower:
                matched += 1

        score = round((matched / len(skills)) * 100)

        role_scores[role] = score

        if score > highest_score:
            highest_score = score
            best_role = role

    return role_scores, best_role, highest_score


# ==========================================================
# SECTION SCORING
# ==========================================================

def calculate_section_scores(detected_sections):

    scores = {}

    scores["Career Objective"] = 10 if detected_sections["Career Objective"] else 3

    scores["Education"] = 10 if detected_sections["Education"] else 2

    scores["Skills"] = 15 if detected_sections["Skills"] else 4

    scores["Projects"] = 20 if detected_sections["Projects"] else 5

    scores["Internships"] = 15 if detected_sections["Internships"] else 5

    scores["Certifications"] = 10 if detected_sections["Certifications"] else 3

    scores["Achievements"] = 10 if detected_sections["Achievements"] else 2

    return scores


# ==========================================================
# OVERALL SCORE
# ==========================================================

def calculate_overall_score(section_scores, highest_role_score):

    section_total = sum(section_scores.values())

    total = section_total + highest_role_score

    if total > 100:
        total = 100

    return total


# ==========================================================
# CONFIDENCE MESSAGE
# ==========================================================

def get_confidence(score):

    if score >= 90:
        return "Excellent Match ⭐⭐⭐⭐⭐"

    elif score >= 75:
        return "Good Match ⭐⭐⭐⭐"

    elif score >= 60:
        return "Fair Match ⭐⭐⭐"

    else:
        return "Needs Improvement ⭐⭐"


# ==========================================================
# STRENGTHS
# ==========================================================

def get_strengths(found_skills, detected_sections):

    strengths = []

    if "Python" in found_skills:
        strengths.append("Strong Python knowledge")

    if "JavaScript" in found_skills:
        strengths.append("Good JavaScript skills")

    if detected_sections["Projects"]:
        strengths.append("Projects section included")

    if detected_sections["Education"]:
        strengths.append("Education section available")

    if detected_sections["Internships"]:
        strengths.append("Internship/Experience section present")

    if "Git" in found_skills and "Github" in found_skills:
        strengths.append("Version Control knowledge")

    return strengths


# ==========================================================
# IMPROVEMENTS
# ==========================================================

def get_improvements(missing_skills, detected_sections):

    improvements = []

    if not detected_sections["Career Objective"]:
        improvements.append("Add a Career Objective")

    if not detected_sections["Projects"]:
        improvements.append("Add Projects")

    if not detected_sections["Certifications"]:
        improvements.append("Add Certifications")

    if not detected_sections["Achievements"]:
        improvements.append("Add Achievements")

    if len(missing_skills) > 0:

        for skill in missing_skills[:5]:

            improvements.append(f"Learn {skill}")

    return improvements


# ==========================================================
# SUGGESTIONS
# ==========================================================

def generate_suggestions(best_role):

    suggestions = []

    if best_role == "Python Developer":

        suggestions = [
            "Learn Django",
            "Learn REST API",
            "Build Flask Projects",
            "Practice SQL",
            "Deploy projects online"
        ]

    elif best_role == "Frontend Developer":

        suggestions = [
            "Learn React",
            "Master JavaScript",
            "Learn Tailwind CSS",
            "Build Responsive Websites",
            "Create Portfolio Website"
        ]

    elif best_role == "Full Stack Developer":

        suggestions = [
            "Learn React",
            "Learn MongoDB",
            "Practice Flask APIs",
            "Deploy Full Stack Projects",
            "Learn Docker Basics"
        ]

    elif best_role == "Data Analyst":

        suggestions = [
            "Learn Pandas",
            "Learn NumPy",
            "Learn Power BI",
            "Practice SQL Queries",
            "Create Data Visualization Projects"
        ]

    return suggestions# ==========================================================
# MAIN ANALYSIS FUNCTION
# ==========================================================

def analyze_resume(filepath):

    # Extract resume text
    resume_text = extract_text(filepath)

    # Detect skills
    found_skills, missing_skills = detect_skills(resume_text)

    # Detect sections
    detected_sections = detect_sections(resume_text)

    # Calculate role match
    role_scores, best_role, highest_role_score = calculate_role_scores(found_skills)

    # Section scores
    section_scores = calculate_section_scores(detected_sections)

    # Overall score
    overall_score = calculate_overall_score(
        section_scores,
        highest_role_score
    )

    # Confidence
    confidence = get_confidence(highest_role_score)

    # Strengths
    strengths = get_strengths(
        found_skills,
        detected_sections
    )

    # Improvements
    improvements = get_improvements(
        missing_skills,
        detected_sections
    )

    # Suggestions
    suggestions = generate_suggestions(best_role)

    # ======================================================
    # ADDITIONAL CHECKS
    # ======================================================

    # Email
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    # Phone Number
    phone = re.search(
        r"\+?\d[\d\s-]{8,}\d",
        resume_text
    )

    # LinkedIn
    linkedin = "linkedin" in resume_text

    # GitHub
    github = "github" in resume_text

    # Resume Summary
    summary = []

    if email:
        summary.append("Email Found")
    else:
        summary.append("Email Missing")

    if phone:
        summary.append("Phone Number Found")
    else:
        summary.append("Phone Number Missing")

    if linkedin:
        summary.append("LinkedIn Profile Added")
    else:
        summary.append("Add LinkedIn Profile")

    if github:
        summary.append("GitHub Profile Added")
    else:
        summary.append("Add GitHub Profile")

    # ======================================================
    # FINAL RESULT
    # ======================================================

    return {

        "overall_score": overall_score,

        "recommended_role": best_role,

        "confidence": confidence,

        "role_scores": role_scores,

        "found_skills": found_skills,

        "missing_skills": missing_skills,

        "section_scores": section_scores,

        "strengths": strengths,

        "improvements": improvements,

        "suggestions": suggestions,

        "summary": summary

    }