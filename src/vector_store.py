from loader import load_documents
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

docs = load_documents("../docs")

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [doc["content"] for doc in docs]

embeddings = model.encode(texts)

if not os.path.isdir("../data"):
    os.mkdir("../data")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(
    np.array(embeddings).astype("float32")
)

faiss.write_index(
    index,
    "../data/faiss_index.bin"
)

with open("../data/documents.pkl", "wb") as f:
    pickle.dump(docs, f)

print("FAISS index created successfully")
print("Documents indexed:", len(docs))