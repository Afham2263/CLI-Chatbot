from model_loader import load_chatbot
from chat_memory import ChatMemory

def main():
    print("Welcome to CLI Chatbot! Type /exit to quit.\n")

    chatbot = load_chatbot()
    memory = ChatMemory(max_turns=3)

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        context = memory.get_context()
        full_prompt = f"{context}User: {user_input}\nBot:"

        result = chatbot(full_prompt, max_new_tokens=100)[0]['generated_text']
        # Only grab bot response AFTER the last "Bot:" to avoid repeating context
        bot_reply = result.split("Bot:")[-1].strip()

        print("Bot:", bot_reply)
        memory.add_turn(user_input, bot_reply)

if __name__ == "__main__":
    main()
