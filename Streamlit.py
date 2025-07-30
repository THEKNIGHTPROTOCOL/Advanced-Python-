import streamlit as st
 
st.title("AI Girlfriend Chatbot ❤️")

user_input = st.text_input("You:")
if st.button("Send"):
    reply = chat_with_ai(user_input)
    st.write("AI GF: " + reply)
