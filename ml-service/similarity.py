from model_loader import model
from sklearn.metrics.pairwise import cosine_similarity

# load model once

def calculate_similarity(text1, text2):

    embeddings = model.encode([text1, text2])

    score = cosine_similarity(
        embeddings[0].reshape(1, -1),
        embeddings[1].reshape(1, -1)
    )[0][0]

    return float(score)