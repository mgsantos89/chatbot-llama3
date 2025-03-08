from chatbot import Chatbot

def main():
    bot = Chatbot()
    print("🤖 Chatbot Llama3.2 via Ollama - Digite 'sair' para encerrar.")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        response = bot.ask(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
