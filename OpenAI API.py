import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def chat_with_ai(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = chat_with_ai(user_input)
    print("AI GF:", reply)
