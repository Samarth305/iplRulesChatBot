# 🏏 IPL Rules Chatbot – Retrieval Augmented Generation (RAG)

An AI-powered chatbot that answers questions about **IPL Playing Conditions, DRS, Super Overs, Match Regulations, Player Conduct, and Tournament Rules** using the official IPL rulebook as its knowledge source.

Instead of relying on generic LLM knowledge, the system retrieves relevant sections directly from the official IPL rulebook and generates accurate, context-aware answers grounded in the source document.

---

## 📌 Overview

The IPL Rulebook contains hundreds of pages of detailed regulations that can be difficult to navigate manually.

This project solves that problem by implementing a **Retrieval Augmented Generation (RAG) pipeline** that:

1. Extracts and processes the official IPL rulebook.
2. Converts rulebook content into vector embeddings.
3. Stores embeddings in a local vector database.
4. Retrieves the most relevant rules for a user query.
5. Re-ranks results for maximum relevance.
6. Generates concise, human-readable answers using an LLM.

The result is an intelligent assistant capable of answering IPL rule-related questions with high accuracy and source-grounded responses.

---

## 🚀 Features

* 📖 **Rulebook-Grounded Responses** – Answers are generated from the official IPL rulebook, reducing hallucinations and improving accuracy.
* 🔒 **Local Document Processing** – Embeddings are generated locally using Ollama, ensuring privacy and zero embedding API costs.
* ⚡ **Fast Semantic Search** – LanceDB enables efficient vector similarity search across the complete rulebook.
* 🎯 **Intelligent Re-Ranking** – Cohere ReRank improves retrieval quality by prioritizing the most relevant rule sections.
* 🤖 **High-Speed LLM Inference** – Groq's Llama 3.3 70B provides near-instant answer generation.
* 📄 **Large Document Support** – Handles the complete IPL rulebook (119+ pages) with ease.
* 💰 **Cost Efficient** – No OpenAI or Gemini API required.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │ IPL Rulebook (PDF)  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Docling Parser      │
                    │ & Text Chunking     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Ollama Embeddings   │
                    │ nomic-embed-text    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ LanceDB Vector Store│
                    └──────────┬──────────┘
                               │
                               │
                               ▼
                       ┌────────────────┐
                       │   User Query   │
                       └────────┬───────┘
                       ┌──────────────────┐
                       │ Semantic Search  │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │ Cohere Re-Rank   │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │ Groq LLM         │
                       │ Llama 3.3 70B    │
                       └────────┬─────────┘
                                │
                                ▼
                         Final Answer
```

---

## 🛠️ Tech Stack

| Component              | Technology                   |
| ---------------------- | ---------------------------- |
| Language               | Python                       |
| LLM                    | Groq Llama 3.3 70B Versatile |
| Embeddings             | Ollama + nomic-embed-text    |
| Vector Database        | LanceDB                      |
| Document Processing    | Docling                      |
| Re-Ranking             | Cohere ReRank                |
| Environment Management | python-dotenv                |

---

## 📂 Project Structure

```text
.
├── datastore/
│   ├── lancedb_store.py
│   └── embedding_manager.py
│
├── indexer/
│   ├── document_parser.py
│   └── chunker.py
│
├── retriever/
│   ├── search.py
│   └── reranker.py
│
├── generator/
│   └── response_generator.py
│
├── sample_data/
│   └── source/
│       └── iplRuleBook.pdf
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ipl-rules-chatbot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Setup Ollama

Install Ollama and pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Ensure Ollama is running:

```bash
ollama serve
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
CO_API_KEY=your_cohere_api_key
```

> No OpenAI or Gemini API keys are required.

---

## 📥 Index the IPL Rulebook

### Step 1: Reset Existing Data

```bash
python main.py reset
```

### Step 2: Add the Rulebook

Place the official IPL PDF inside:

```text
sample_data/source/
```

Then run:

```bash
python main.py add -p "sample_data/source/"
```

The system will:

* Extract text from the PDF
* Chunk the content
* Generate embeddings locally
* Store vectors in LanceDB

---

## 💬 Usage

### Ask Questions

```bash
python main.py query "What are the rules for a Super Over?"
```

```bash
python main.py query "When can a team take a DRS review?"
```

```bash
python main.py query "What are the concussion substitute rules?"
```

```bash
python main.py query "What happens if rain interrupts an IPL match?"
```

```bash
python main.py query "What situations result in a no-ball?"
```

---

## 🎯 Example Workflow

```text
User Question
      │
      ▼
Convert Query to Embedding
      │
      ▼
Retrieve Relevant Rulebook Chunks
      │
      ▼
Re-rank Results with Cohere
      │
      ▼
Generate Context-Aware Answer
      │
      ▼
Return Final Response
```

---

## 🔮 Future Improvements

* Streamlit or React-based chat interface
* Source citations and highlighted references
* Multi-document support
* Conversation memory
* Hybrid search (keyword + vector)
* Docker deployment
* Support for ICC and BCCI rulebooks
* Evaluation metrics dashboard

---

## 📈 Learning Outcomes

This project demonstrates practical experience with:

* Retrieval Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* Semantic Search
* Re-ranking Pipelines
* Large Language Models
* Document Intelligence
* End-to-End AI System Design

---

## Example Query

**Question**

> What are the IPL Super Over rules?

**Pipeline**

1. Retrieve relevant Super Over sections from the IPL rulebook.
2. Re-rank retrieved passages using Cohere.
3. Generate a concise answer using Groq Llama 3.3 70B.
4. Return a grounded response based on official IPL regulations.

This approach ensures answers remain accurate, explainable, and grounded in the official IPL Playing Conditions document.
