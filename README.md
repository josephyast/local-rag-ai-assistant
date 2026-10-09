# Local RAG AI Assistant

A fully local Retrieval-Augmented Generation (RAG) assistant that answers questions about hotels using TripAdvisor reviews. It runs entirely on your machine with [Ollama](https://ollama.com), [LangChain](https://www.langchain.com) and [Chroma](https://www.trychroma.com). No API keys and no cloud calls.

## How it works

1. `vector.py` loads `tripadvisor_hotel_reviews.csv`, embeds each review with `nomic-embed-text`, and stores the embeddings in a local Chroma database (`chrome_langchain_db/`). This only happens on the first run. After that, the existing database is reused.
2. `main.py` takes your question, retrieves the 5 most relevant reviews, and passes them with the question to `llama3:8b`, which generates the answer.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/download) installed and running

## Setup

```bash
# 1. Pull the models
ollama pull llama3:8b
ollama pull nomic-embed-text

# 2. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Download the [TripAdvisor Hotel Reviews dataset](https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews) and save it as `tripadvisor_hotel_reviews.csv` in the project root. It must have `Review` and `Rating` columns.

## Usage

```bash
python main.py
```

Type a question at the prompt, for example:

```
What would you like to ask? (type 'quit' to exit): Are the rooms clean and is the staff friendly?
```

Type `quit` to exit.

> **Note:** If you change the CSV, delete the `chrome_langchain_db/` folder so the embeddings are rebuilt on the next run.

## Project structure

```
.
├── main.py              # Interactive Q&A loop (prompt + LLM chain)
├── vector.py            # Builds/loads the Chroma vector store and retriever
├── requirements.txt     # Python dependencies
└── tripadvisor_hotel_reviews.csv   # Dataset (not tracked in git)
```

## Configuration

- **LLM model:** change `OllamaLLM(model="llama3:8b")` in `main.py`
- **Embedding model:** change `OllamaEmbeddings(model="nomic-embed-text")` in `vector.py`
- **Number of retrieved reviews:** change `search_kwargs={"k": 5}` in `vector.py`
