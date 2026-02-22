import sys
from pathlib import Path

# Ajoute le chemin du projet au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from Chatbot.chatbot import Chatbot

def main():
    chatbot = Chatbot()
    print("Chatbot démarré. Tapez 'quit' pour sortir.")
    while True:
        user_input = input("Vous: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        response = chatbot.execute(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
