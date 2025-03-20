import random

responses = [
    "Hey love! 😊 How’s your day going?",
    "I was thinking about you! 💖",
    "Tell me something exciting! 😍",
    "You always make me smile! 😊",
    "I love chatting with you! 💕",
    "You’re the best! 🥰",
    "I miss you already! ❤️",
]

def chatbot():
    print("AI Girlfriend 🤖: Hello darling! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("AI Girlfriend 🤖: Bye bye, take care! 😘")
            break
        print("AI Girlfriend 🤖:", random.choice(responses))

if __name__ == "__main__":
    chatbot()
