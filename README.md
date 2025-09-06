#  Ollama LLM with LangChain & Streamlit

This is a simple web application that integrates **[Ollama](https://ollama.ai/)** LLMs with **LangChain** and serves the responses through a **Streamlit** interface.  

The app takes a user’s question, passes it through a LangChain prompt, calls the Ollama model, and displays the answer interactively.

---

## 🚀 Features
- Streamlit UI for chatting with an LLM  
- LangChain prompt template and output parsing  
- Ollama integration (supports local models like `gemma3:1b`, `llama2`, etc.)  
- Environment variable management with `.env`  
- LangSmith tracing support  

---

## ⚙️ Environment Setup

LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name


### 1. Clone the repository
```bash
git clone https://github.com/your-username/ollama-langchain-app.git
cd ollama-langchain-app
