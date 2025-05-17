import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a nice AI bot.")
    ]
if "messages_display" not in st.session_state:
    st.session_state.messages_display = []

# Streamlit UI
st.title("🤖 Gemini Chatbot")

# Display previous messages
for msg in st.session_state.messages_display:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Add human message to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.messages_display.append({"role": "user", "content": user_input})

    # Get AI response
    response = llm.invoke(user_input)

    # Add AI response to history
    st.session_state.chat_history.append(AIMessage(content=response.content))
    st.session_state.messages_display.append({"role": "assistant", "content": response.content})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)
