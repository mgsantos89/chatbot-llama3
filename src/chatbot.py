import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")

class Chatbot:
    def __init__(self):
        self.messages = [{"role": "system", "content": "Você é um assistente útil."}]
    
    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": "llama3.2:1b",
                "messages": self.messages
            }
        )
        if response.status_code == 200:
            answer = response.json().get("choices")[0]["message"]["content"]
            self.messages.append({"role": "assistant", "content": answer})
            return answer
        else:
            return "Erro ao se comunicar com o modelo Llama via Ollama."
