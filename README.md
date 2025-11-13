# 🤖 Simple Bot — LangGraph + GPT-4o Integration

This project demonstrates how to build a **Simple ChatBot** using **LangGraph** and **LangChain’s ChatOpenAI**.  
It serves as an introduction to how **LLMs can be integrated into graph-based workflows**.

---

## 🎯 Objectives

1. Define a **state** structure with a list of `HumanMessage` objects.  
2. Initialize a **GPT-4o** model using `LangChain’s ChatOpenAI`.  
3. Send and handle **different types of messages**.  
4. Build and compile the **graph of the Agent**.

---

### 🧩 Main Goal
> Understand how to integrate **LLMs** in **LangGraph-based workflows**.

---

## 🏗️ Project Structure
LangGraph-SimpleBot/
│
├── bot.py
├── requirements.txt
└── README.md

---

## 🚀 How to Run

```bash
# 1️⃣ Create environment
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Set OpenAI key
export OPENAI_API_KEY="your_api_key_here"

# 4️⃣ Run the bot
python bot.py


Output Example
User: Hello, who are you?
Bot: I’m a simple bot powered by GPT-4o and LangGraph!


📚 Concepts Used

LangGraph for graph-based execution flow

LangChain for LLM integration

ChatOpenAI (GPT-4o) for natural conversation

StateGraph to define nodes, edges, and flow control


🧑‍💻 Author

Developed by Bilal Ahmed

Check out all my LangGraph learning projects here →
🔗 https://github.com/BilalAhmed7072