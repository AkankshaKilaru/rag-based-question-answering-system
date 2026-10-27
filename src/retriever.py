import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("../data/faiss_index.bin")

with open("../data/documents.pkl", "rb") as f:
    docs = pickle.load(f)

while True:

    query = input("\nEnter query (or 'exit'): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype("float32"),
        k=3
    )

    print("\nTop Results:\n")

    for rank, idx in enumerate(I[0], start=1):

        print(f"{rank}. {docs[idx]['source']}")