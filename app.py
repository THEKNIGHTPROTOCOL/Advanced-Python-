from kivy.app import App
from kivy.uix.label import Label

class ChatbotApp(App):
    def build(self):
        return Label(text="Hello! I am your AI friend!")

ChatbotApp().run()
