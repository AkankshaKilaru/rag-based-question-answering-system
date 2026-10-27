from loader import load_documents

docs = load_documents("../docs")

chunks = []

for doc in docs:
    text = doc["content"]

    for i in range(0, len(text), 500):
        chunks.append({
            "source": doc["source"],
            "text": text[i:i+500]
        })

print("Total Documents:", len(docs))
print("Total Chunks:", len(chunks))

if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0]["text"][:200])