from parsing.parser import parse_file

text = parse_file("data/resumes/sample_resume.pdf")
print(text[:500])
