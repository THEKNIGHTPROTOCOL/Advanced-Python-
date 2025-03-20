from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

class AIGirlfriendApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Talk to me!", font_size=20)
        self.layout.add_widget(self.label)

        self.text_input = TextInput(hint_text="Type your message here", multiline=False)
        self.layout.add_widget(self.text_input)

        self.button = Button(text="Send", on_press=self.get_response)
        self.layout.add_widget(self.button)

        return self.layout

    def get_response(self, instance):
        user_text = self.text_input.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        ai_text = response["choices"][0]["message"]["content"]
        self.label.text = ai_text
        self.text_input.text = ""

if __name__ == "__main__":
    AIGirlfriendApp().run()
