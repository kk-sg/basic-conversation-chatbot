"""
OpenAI-powered Simple AI Chatbot Application using Streamlit

This script creates a Streamlit web application that interacts with OpenAI's GPT-3.5-turbo model
to provide question-answering capabilities. It maintains a chat history and displays responses
in a user-friendly interface.
"""

from typing import List, Tuple, Optional
import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load environment variables
load_dotenv()

# Configure OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_openai_response(question: str) -> str:
    """
    Send a question to OpenAI's GPT-3.5-turbo model and return the response.

    Args:
        question (str): The user's input question.

    Returns:
        str: The model's response or an error message if an exception occurs.
    """
    try:
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
    """
    Add a new entry to the chat history.

    Args:
        role (str): The role of the speaker (e.g., "You" or "Bot").
        content (str): The content of the message.
    """
    st.session_state['chat_history'].append((role, content))


def display_chat_history() -> None:
    """Display the entire chat history."""
    st.subheader("Chat History")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")


def main() -> None:
    """Main function to set up and run the Streamlit application."""
    st.set_page_config(page_title="Simple AI Chatbot")
    st.header("OpenAI LLM Application")

    initialize_chat_history()

    user_input = st.text_input("Input:", key="input")
    submit_button = st.button("Ask the question")

    if submit_button and user_input:
        response = get_openai_response(user_input)

        add_to_chat_history("You", user_input)

        st.subheader("Response")
        st.write(response)

        add_to_chat_history("Bot", response)

    display_chat_history()


if __name__ == "__main__":
    main()
