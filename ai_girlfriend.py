import openai
import pyttsx3
import speech_recognition as sr

# Set OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "I couldn't understand, please repeat."
    except sr.RequestError:
        return "Speech recognition is not available."

# Main Loop
while True:
    user_input = listen()
    if "exit" in user_input.lower():
        speak("Goodbye! See you later.")
        break
    
    response = chat_with_ai(user_input)
    print("AI Girlfriend:", response)
    speak(response)


import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("firebase-admin.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Save chat history
def save_chat(user, bot):
    doc_ref = db.collection("chat_history").document()
    doc_ref.set({"user": user, "bot": bot})

