from parsing.parser import parse_file
from extraction.skill_extractor import extract_skills

text = parse_file("data/resumes/sample_resume.pdf")
skills = extract_skills(text)

print("Extracted skills:")
for skill in skills:
    print("-", skill)
