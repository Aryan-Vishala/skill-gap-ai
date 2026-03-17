import re

from model_loader import model
from sklearn.metrics.pairwise import cosine_similarity
from skills_db import skills

# flatten skills
all_skills = [skill for category in skills.values() for skill in category]

# Precompute skill embeddings once
skill_embeddings = model.encode(all_skills)

def generate_ngrams(words):
    bigrams = [" ".join(words[i:i+2]) for i in range(len(words)-1)]
    return list(set(words + bigrams))


def extract_skills(text):

    base_words = re.findall(r"[a-zA-Z0-9\.]+", text.lower())
    words = generate_ngrams(base_words)

    # Encode all words together (much faster)
    word_embeddings = model.encode(words)

    detected_skills = []

    for word_embedding in word_embeddings:

        similarity = cosine_similarity([word_embedding], skill_embeddings)

        best_match_index = similarity.argmax()

        score = similarity[0][best_match_index]

        if score > 0.6:
            detected_skills.append(all_skills[best_match_index])

    return list(set(detected_skills))