def calculate_match_score(resume_text, jd_text):

    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    skills = [
        "python",
        "sql",
        "machine learning",
        "fastapi",
        "tensorflow",
        "pandas",
        "git"
    ]

    matched_skills = []

    for skill in skills:

        if skill in resume_text and skill in jd_text:
            matched_skills.append(skill)


    score = (
        len(matched_skills)
        /
        len(skills)
    ) * 100


    return score, matched_skills