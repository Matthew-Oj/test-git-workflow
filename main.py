# Import Streamlit
import streamlit as st

# Add a title to your app
st.title('Hello, Streamlit!')

# Ask the user for their name
user_name = st.text_input("What's your name?")

# Greet the user
if user_name:
  st.write(f'Hello, {user_name}! Welcome to your first Streamlit app!')