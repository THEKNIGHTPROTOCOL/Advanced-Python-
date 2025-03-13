from textblob import TextBlob
import emoji

def add_emotion(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0.5:
        return text + " 😊❤️"
    elif sentiment < -0.5:
        return text + " 😢💔"
    else:
        return text + " 😐"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = chat_with_ai(user_input)
    reply_with_emoji = add_emotion(reply)
    print("AI GF:", reply_with_emoji)
