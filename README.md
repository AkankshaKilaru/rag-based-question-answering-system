# RAG-Based Question Answering System

A Retrieval-Augmented Generation (RAG) based question-answering application built using Python, Streamlit, FAISS, Sentence Transformers, and Google Gemini. The system retrieves relevant information from a knowledge base and generates contextual answers using a large language model.

## Overview

Traditional question-answering systems may provide generic answers that are not specific to a given knowledge base. This project combines semantic document retrieval with generative AI to produce relevant, context-aware responses.

The application also incorporates persona detection, sentiment analysis, and human escalation to support more personalized customer support interactions.

## Features

- **Retrieval-Augmented Generation (RAG):** Retrieves relevant documents before generating answers.
- **Semantic Search:** Uses Sentence Transformers to generate text embeddings.
- **Vector Search:** Uses FAISS for efficient similarity search.
- **AI-Powered Responses:** Uses Google Gemini to generate contextual answers.
- **Persona Detection:** Identifies Technical Expert, Frustrated User, and Business Executive personas.
- **Sentiment Analysis:** Performs basic keyword-based sentiment detection.
- **Escalation Handling:** Flags selected issues for human support.
- **Human Handoff:** Generates a summary containing the customer issue and retrieved sources.
- **Conversation History:** Displays previous questions and responses during the session.
- **Interactive Interface:** Provides a user-friendly Streamlit application.

## Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini
- **RAG Framework:** Custom retrieval and generation pipeline
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** FAISS
- **Numerical Computing:** NumPy
- **Environment Configuration:** Python dotenv

## Project Structure

rag-based-question-answering-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── data/
│   ├── documents.pkl
│   └── faiss_index.bin
│
├── docs/
│   ├── account_access.txt
│   ├── billing_policy.txt
│   ├── data_export.txt
│   ├── login_issues.txt
│   ├── password_reset.txt
│   ├── payment_issues.txt
│   ├── refund_policy.txt
│   ├── security_guide.txt
│   ├── subscription_faq.txt
│   ├── system_errors.txt
│   ├── two_factor_auth.txt
│   └── user_permissions.txt
│
└── src/
    ├── chunker.py
    ├── embeddings.py
    ├── escalation.py
    ├── generator.py
    ├── handoff.py
    ├── loader.py
    ├── persona.py
    ├── retriever.py
    └── vector_store.py


## How It Works

1. **User Query:** The user enters a question through the Streamlit interface.
2. **Persona Detection:** The system identifies the likely customer persona.
3. **Sentiment Analysis:** The system estimates sentiment using predefined keywords.
4. **Embedding Generation:** Sentence Transformers converts the query into a vector representation.
5. **Document Retrieval:** FAISS searches the knowledge-base index for relevant documents.
6. **Context Preparation:** Retrieved document content is combined into a context.
7. **Response Generation:** Google Gemini generates a response based on the query and retrieved context.
8. **Escalation Check:** The system checks whether human support is required.
9. **Human Handoff:** When escalation is triggered, the application can display a structured handoff summary.

## Installation and Setup

### Prerequisites

- Python 3.11 or later
- pip
- A Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/AkankshaKilaru/rag-based-question-answering-system.git
cd rag-based-question-answering-system
```


### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the root directory:

GEMINI_API_KEY=your_gemini_api_key

Replace the placeholder with your own API key. Never publish the actual key.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.


## Example Queries

**Technical Expert**

> I'm getting an authentication error when using the API. How can I troubleshoot it?

**Frustrated User**

> I've tried resetting my password three times, and it's still not working. This is extremely frustrating!

**Business Executive**

> Our system downtime is affecting business operations and revenue. What is the recommended resolution?

## Future Improvements

- Improve persona and sentiment classification using NLP models.
- Add calibrated retrieval relevance scoring.
- Improve source citations and answer-grounding validation.
- Support conversation-aware escalation and repeated-issue tracking.
- Add document upload and automatic knowledge-base indexing.
- Introduce automated evaluation for retrieval and response quality.
- Add unit tests and integration tests.

## Learning Outcomes

This project demonstrates practical experience with:

- Retrieval-Augmented Generation architecture
- Text embeddings and vector similarity search
- Integration of a large language model API
- Python application development
- Basic NLP classification
- Customer support workflow automation
- Human-in-the-loop escalation
