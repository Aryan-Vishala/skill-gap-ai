from skill_extraction import extract_skills
from similarity import calculate_similarity


def analyze(resume_text, job_text):

    resume_skills = list(set(extract_skills(resume_text)))
    job_skills = list(set(extract_skills(job_text)))

    missing_skills = list(set(job_skills) - set(resume_skills))

    # NEW: matched skills
    matched_skills = list(set(job_skills) & set(resume_skills))

    resume_skills.sort()
    missing_skills.sort()

    # compare only skills instead of full text
    resume_string = " ".join(resume_skills)
    job_string = " ".join(job_skills)

    score = calculate_similarity(resume_string, job_string)

    # ensure score stays between 0 and 1
    if score > 1:
        score = 1
    if score < 0:
        score = 0

    # NEW: skill match score
    if len(job_skills) > 0:
        skill_match_score = (len(matched_skills) / len(job_skills)) * 100
    else:
        skill_match_score = 0

    return {
        "semantic_score": round(score * 100, 2),
        "skill_match_score": round(skill_match_score, 2),
        "matched_skills": matched_skills,
        "resume_skills": resume_skills,
        "missing_skills": missing_skills
    }

def categorize(skills_list):
    categorized = {}

    for category, skill_list in skills.items():
        matched = [s for s in skills_list if s in skills_list]
        if matched:
            categorized[category] = matched

    return categorized