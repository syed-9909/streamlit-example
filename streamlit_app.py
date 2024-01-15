import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
#import streamlit as st
import sqlite3

# Function to get a response from the chatbot
def get_bot_response(user_input):
    # For simplicity, this example just echoes the user input as the bot response
    return user_input

# Streamlit app
def main():
    st.title("Simple Chatbot with SQLite")

    # Connect to SQLite database
    conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your database file
    cursor = conn.cursor()

    # Create chat_history table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            user_input TEXT,
            bot_response TEXT
        )
    ''')

    # Sidebar to show chat history
    st.sidebar.title("Chat History")
    chat_history = st.sidebar.empty()

    # Main chatbot interface
    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            # Save user input to the database
            cursor.execute("INSERT INTO chat_history (user_input, bot_response) VALUES (?, ?)", (user_input, get_bot_response(user_input)))
            conn.commit()

            # Display user input
            st.text(f"You: {user_input}")

            # Display bot response
            bot_response = get_bot_response(user_input)
            st.text(f"Bot: {bot_response}")

            # Update chat history in the sidebar
            chat_history.text(f"You: {user_input}\nBot: {bot_response}")

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
