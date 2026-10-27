from src.loader import load_documents

docs = load_documents("docs")

print("Total Documents:", len(docs))

for doc in docs:
    print(doc["source"])