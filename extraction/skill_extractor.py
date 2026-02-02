import re
from typing import List, Set


SKILL_KEYWORDS = {

    # ===== Programming Languages =====
    "python", "java", "c", "c++",

    # ===== Web Technologies =====
    "html", "css", "javascript", "react", "node.js",
    "django", "flask", "fastapi",

    # ===== Databases =====
    "sql",

    # ===== APIs =====
    "rest api", "rest apis", "restful api", "restful apis", "api development",

    # ===== Tools & Version Control =====
    "git", "github",

    # ===== Containers / DevOps =====
    "docker", "kubernetes", "ci cd", "linux", "monitoring",

    # ===== Cloud =====
    "aws", "cloud", "cloud computing",

    # ===== Data / Analytics =====
    "data analysis", "data visualization",
    "statistics",
    "pandas", "numpy",
    "excel", "power bi", "tableau",

    # ===== Machine Learning / AI =====
    "machine learning", "deep learning",
    "nlp", "computer vision",
    "model evaluation", "model deployment",
    "transformers", "model optimization",

    # ===== Deep Learning Frameworks =====
    "tensorflow", "tf", "keras",
    "pytorch", "torch",

    # ===== Software Engineering =====
    "data structures", "algorithms",
    "object oriented programming",
    "problem solving", "system design",

    # ===== Web / Frontend Concepts =====
    "responsive design", "ui ux",
    "browser compatibility", "browser rendering",

    # ===== Backend Concepts =====
    "authentication",

    # ===== Automation / DevOps =====
    "automation"
}



def extract_skills(text: str) -> List[str]:
    """
    Extract skills from resume or job description text.
    """
    text = text.lower()
    found_skills: Set[str] = set()

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)
