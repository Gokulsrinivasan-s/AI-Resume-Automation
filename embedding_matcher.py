from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load AI model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


resume = """
Python developer with experience in
Machine Learning, SQL, Pandas,
FastAPI and TensorFlow.
"""


jd = """
Looking for a Machine Learning Engineer
with Python, SQL, Deep Learning,
API development and data processing skills.
"""


# Convert text into embeddings

resume_embedding = model.encode(
    resume
)


jd_embedding = model.encode(
    jd
)


# Compare similarity

score = cosine_similarity(
    [resume_embedding],
    [jd_embedding]
)


similarity_score = score[0][0] * 100


print(
    "Resume Match Score:",
    round(similarity_score,2),
    "%"
)