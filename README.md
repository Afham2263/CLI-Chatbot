
# 🧠 CLI Chatbot — Local LLM on Hugging Face

A dead-simple, local command-line chatbot built in Python using Hugging Face models.

It remembers short conversations, runs fully offline, and doesn’t melt your GPU while you're gaming. Great for quick experiments, intro LLM work, or just asking dumb stuff like “what’s the capital of Spain” without it replying “potato.”

---

## 🚀 Features

- 🤖 Runs locally with `google/flan-t5-base` or other small Hugging Face models
- 🧠 Maintains memory of recent turns (sliding window)
- 🖥️ Clean CLI interface — just type and talk
- 🧼 Modular Python code: no spaghetti, no drama
- ✅ No GPU needed — runs fine on CPU
- 🛑 Graceful exit with `/exit`

---

## 📂 File Structure

  
  ```

CLI-Chatbot/
├── interface.py        # CLI loop & prompt formatting
├── model\_loader.py     # Loads Hugging Face model/tokenizer
├── chat\_memory.py      # Manages recent conversation turns
├── README.md           # You're lookin' at it

  ```


ddd

## 🛠️ Setup

1. Clone this repo or dump the files somewhere:
   ```bash
   git clone <this-repo>
   cd CLI-Chatbot


2. Install dependencies:

   ```bash
   pip install transformers torch
   ```

3. Run the chatbot:

   ```bash
   python interface.py
   ```

---

## 🧪 Example Chat

```
Welcome to CLI Chatbot! Type /exit to quit.

User: What is the capital of France?
Bot: Paris

User: And what about Italy?
Bot: Rome

User: What’s the capital of Spain?
Bot: Madrid

User: /exit
Exiting chatbot. Goodbye!
```

---

## 🔁 Commands

| Command                  | What it does            |
| ------------------------ | ----------------------- |
| `/exit`                  | Exit the chatbot safely |
| *(coming soon)* `/reset` | Clears memory buffer    |

---

## 🤓 Customize

Wanna try different models? Crack open `model_loader.py` and change this:

```python
def load_chatbot(model_name="google/flan-t5-base"):
```

Other decent Hugging Face models to try:

* `google/flan-t5-small` — 🐢 way dumber but smaller
* `microsoft/DialoGPT-small` — chattier, but less facty
* `tiiuae/falcon-rw-1b` — needs more RAM, smarter answers

---

## ⚠️ Disclaimer

This is for testing and learning. Some models may produce inaccurate, inappropriate, or just straight-up dumb responses. Use responsibly. Don't let it raise your kids.

---

## 🧠 Credits

Built by Afham 
