"""
OpenAI-powered Simple Chatbot Application using Streamlit

This script creates a Streamlit web application that interacts with OpenAI's GPT-3.5-turbo model
to provide question-answering capabilities. It maintains a chat history and displays responses
in a user-friendly interface with an improved layout.
"""

from typing import List, Tuple, Optional
import streamlit as st
from openai import OpenAI

def get_openai_response(question: str, api_key: str) -> str:
    """Send a question to OpenAI's GPT-3.5-turbo model and return the response."""
    try:

        # Initialize OpenAI client with the API key
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Please respond in full sentences."},
                {"role": "user", "content": question}
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


def initialize_chat_history() -> None:
    """Initialize the chat history in the session state if it doesn't exist."""
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []


def add_to_chat_history(role: str, content: str) -> None:
    """Add a new entry to the chat history."""
    st.session_state['chat_history'].append((role, content))


def display_chat_history() -> None:
    """Display the chat history with an improved layout."""
    st.subheader("Chat History")
    for i, (role, text) in enumerate(st.session_state['chat_history']):
        message(text, is_user=(role == "You"), key=f"{i}_{role.lower()}")


def message(text: str, is_user: bool, key: str) -> None:
    """Display a message in the chat interface."""
    message_alignment = 'left' if is_user else 'right'
    avatar_image = 'https://api.dicebear.com/9.x/thumbs/svg?seed=Felix' if is_user else 'https://api.dicebear.com/9.x/thumbs/svg?seed=Buddy'
    background_color = '#0d0d0c' if is_user else '#04066e'

    with st.container():
        col1, col2 = st.columns([1, 12])
        with col1:
            st.image(avatar_image, width=50)
        with col2:
            st.markdown(
                f"<div style='text-align: {message_alignment}; padding: 10px; border-radius: 10px; background-color: {background_color};'>"
                f"<p style='margin: 0;'>{text}</p>"
                "</div>",
                unsafe_allow_html=True
            )


def get_api_key() -> str:
    """Get the OpenAI API key from the user."""
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    if api_key:
        st.success(
            "API key entered successfully. Your key is kept private and not stored.")
    return api_key


def main() -> None:
    """Main function to set up and run the Streamlit application."""
    st.set_page_config(page_title="Simple AI Chatbot", layout="wide")
    st.header("OpenAI LLM Application: Simple AI Chatbot")

    initialize_chat_history()

    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("Enter API Key")
        api_key = get_api_key()

        st.subheader("Ask a Question")
        with st.form(key='input_form'):
            user_input = st.text_input("Input:", key="user_input")
            submit_button = st.form_submit_button("Ask")

        if submit_button:
            if not api_key:
                st.error("Please enter your OpenAI API key to use the chatbot.")
            elif user_input:
                response = get_openai_response(user_input, api_key)
                add_to_chat_history("You", user_input)
                add_to_chat_history("Bot", response)

    with col2:
        display_chat_history()


if __name__ == "__main__":
    main()
