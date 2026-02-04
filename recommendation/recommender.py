from typing import List, Dict, Set
from recommendation.role_data import ROLE_DATA


SKILL_ALIASES = {
    # ===== REST APIs =====
    "rest api": "rest api",
    "rest apis": "rest api",
    "rest-api": "rest api",
    "restful api": "rest api",
    "restful apis": "rest api",
    "api": "rest api",
    "apis": "rest api",

    # ===== TensorFlow / Deep Learning =====
    "tensorflow": "tensorflow",
    "tf": "tensorflow",
    "keras": "tensorflow",

    # ===== PyTorch =====
    "torch": "pytorch",
    "pytorch": "pytorch",

    # ===== Generative AI =====
    "gen ai": "generative ai",
    "generative ai": "generative ai",
    "llm": "llms",
    "llms": "llms",
    "large language models": "llms",

    # ===== NLP / AI Variants =====
    "natural language processing": "nlp",

    # TensorFlow
    "tf": "tensorflow",
    "keras": "tensorflow",

    # PyTorch
    "torch": "pytorch",

    # UI/UX
    "ui/ux": "ui ux",

    # CI/CD
    "ci/cd": "ci cd"



}



def normalize_skills(skills: List[str]) -> Set[str]:
    normalized = set()

    for skill in skills:
        s = skill.strip().lower()
        s = SKILL_ALIASES.get(s, s)  # map alias → canonical form
        normalized.add(s)

    return normalized



def calculate_match_score(
    resume_skills: Set[str],
    role_skills: Set[str]
) -> float:
    """
    Calculate match percentage between resume skills and role skills.
    """
    if not role_skills:
        return 0.0

    matched_skills = resume_skills.intersection(role_skills)
    score = (len(matched_skills) / len(role_skills)) * 100
    return round(score, 2)


def recommend_roles(
    resume_skills: List[str],
    top_n: int = 4,
    min_score: float = 50.0 
) -> List[Dict]:
    """
    Recommend roles based on extracted resume skills.

    Returns:
        - role
        - match_score
        - matched_skills
        - missing_skills
    """


    resume_skills_set = normalize_skills(resume_skills)
    recommendations = []

    for role_name, role_info in ROLE_DATA.items():
        role_skills = normalize_skills(role_info.get("skills", []))

        score = calculate_match_score(resume_skills_set, role_skills)

        if score >= min_score:
            matched = sorted(resume_skills_set.intersection(role_skills))
            missing = sorted(role_skills - resume_skills_set)

            recommendations.append({
                "role": role_name,
                "match_score": score,
                "matched_skills": matched,
                "missing_skills": missing
            })

    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return recommendations[:top_n]


# -------- Manual test --------
if __name__ == "__main__":
    sample_skills = [
        "python", "sql", "machine learning",
        "html", "css", "javascript"
    ]

    results = recommend_roles(sample_skills)

    for r in results:
        print(f"\nRole: {r['role']}")
        print(f"Match Score: {r['match_score']}%")
        print(f"Matched Skills: {r['matched_skills']}")
        print(f"Missing Skills: {r['missing_skills']}")
