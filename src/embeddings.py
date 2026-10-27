from loader import load_documents
from sentence_transformers import SentenceTransformer

docs = load_documents("../docs")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

texts = []

for doc in docs:
    texts.append(doc["content"])

embeddings = model.encode(texts)

print("Documents:", len(texts))
print("Embedding Shape:", embeddings.shape)