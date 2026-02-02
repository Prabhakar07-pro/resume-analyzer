from parsing.parser import parse_file
from extraction.skill_extractor import extract_skills
from recommendation.recommender import recommend_roles


def run_pipeline(resume_path: str):
    # Parse resume
    text = parse_file(resume_path)

    # Extract skills
    skills = extract_skills(text)

    # Get role recommendations
    recommendations = recommend_roles(skills)

    if not recommendations:
        print("No suitable roles found.")
        return

    # ✅ ONLY REQUIRED OUTPUT
    for idx, rec in enumerate(recommendations, start=1):
        print(f"\n{idx}. Suggested Role: {rec['role']}")
        print(f"   Match Score: {rec['match_score']}%")
        print(f"   Matched Skills: {rec['matched_skills']}")
        print(f"   Missing Skills: {rec['missing_skills']}")


if __name__ == "__main__":
    resume_file = "data/resumes/sample_resume.pdf"
    run_pipeline(resume_file)
