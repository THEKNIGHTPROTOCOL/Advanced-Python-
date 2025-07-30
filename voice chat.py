import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text): 
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "I didn't understand that."
    
while True:
    user_input = listen()
    if "exit" in user_input:
        break
    reply = chat_with_ai(user_input)
    print("AI GF:", reply)
    speak(reply)
