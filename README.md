# Rich Dad Poor Dad Chatbot

   A simple Python-based chatbot that answers questions about the renowned financial education book *Rich Dad Poor Dad* by Robert T. Kiyosaki and Sharon Lechter.

---


##  Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AlokDhanush/rich_dad_poor_dad_chatbot.git
   cd rich_dad_poor_dad_chatbot
   ```

---

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  #macOS/Linux
   venv\Scripts\activate     #Windows
   ```

---

3. **Install dependencies:**

   Install Ollama from [Install](https://ollama.com/download)<br>
   Add the installed path to the system variable.<br>
   Download Llama3.2 (or any model which supports your system software) by running the below command in command prompt.<br>
   ```bash
      ollama pull llama3.2
   ```
   Also install other dependencies<br>
   ```bash
   pip install chromadb langchain langchain_chroma langchain_huggingface langchain_ollama langchain_community
   ```
---
