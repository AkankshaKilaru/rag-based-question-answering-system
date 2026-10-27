import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

from src.persona import detect_persona, get_sentiment
from src.generator import generate_response
from src.escalation import should_escalate
from src.handoff import create_handoff

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("data/faiss_index.bin")

with open("data/documents.pkl", "rb") as f:
    docs = pickle.load(f)

st.set_page_config(page_title="Persona-Aware Support Agent")

st.title("🤖 Persona-Aware Customer Support Agent")
st.caption("RAG + Gemini + Persona Detection + Human Handoff")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask a question")

if query:

    persona = detect_persona(query)

    sentiment = get_sentiment(query)

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype("float32"),
        k=3
    )

    distance = float(D[0][0])

    confidence = round(
        max(60, min(95, 100 - distance * 10)),
        2
    )

    retrieved_docs = []
    retrieved_sources = []

    for idx in I[0]:
        retrieved_docs.append(docs[idx]["content"])
        retrieved_sources.append(docs[idx]["source"])

    context = "\n\n".join(retrieved_docs)

    response = generate_response(
        persona,
        context,
        query
    )

    st.session_state.history.append(
        {
            "query": query,
            "response": response
        }
    )

    escalation = should_escalate(
        query,
        confidence
    )

    st.subheader("Detected Persona")
    st.write(persona)

    st.subheader("Sentiment")
    st.write(sentiment)

    st.subheader("Retrieved Sources")
    st.write(f"Documents Retrieved: {len(retrieved_sources)}")

    for source in retrieved_sources:
        st.write(f"• {source}")

    st.subheader("Confidence Score")

    if confidence >= 70:
        st.success(f"{confidence}%")
    elif confidence >= 40:
        st.warning(f"{confidence}%")
    else:
        st.error(f"{confidence}%")

    st.subheader("Response")
    st.write(response)

    st.subheader("Escalation Status")

    if escalation:

        st.error("Escalation Required")

        st.warning("Human approval required")

        approve = st.button("Approve Escalation")

        if approve:

            handoff = create_handoff(
                persona,
                query,
                retrieved_sources
            )

            st.subheader("Human Handoff Summary")
            st.json(handoff)

    else:

        st.success("No Escalation Needed")

    st.subheader("Conversation History")

    for item in st.session_state.history:

        st.write(f"👤 User: {item['query']}")
        st.write(f"🤖 Bot: {item['response']}")
        st.divider()

    st.subheader("Feedback")

    feedback = st.radio(
        "Was this response helpful?",
        ["👍 Yes", "👎 No"]
    )

    if st.button("Submit Feedback"):
        st.success("Feedback recorded.")
