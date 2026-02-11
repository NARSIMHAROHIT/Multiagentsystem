import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000" #backend url
 
st.set_page_config(
    page_title = "✈️ AI Trip Planner",
    page_icon = "✈️",
    layout = "centered",
    initial_sidebar_state = "expanded"
)

st.title("✈️ Travel planner Agent")

#initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [] 

st.header("Explore the world with our AI Trip Planner! 🌍. See the World Store the Memories✈️")
with st.form(key = "query_form",clear_on_submit=True):
    user_input = st.text_input("Ask me anything about your travel plans! 🧳🌐",placeholder="Where should I go for my next vacation? Or What is the weather like in Paris next week?")
    submit_button=st.form_submit_button("Submit")
if submit_button and user_input:
    try:
        #show user message
        #Show thinking  spinner while processing the request
        with st.spinner("Planning the perfect trip ..."):
            payload = {"query":user_input}
            response = requests.post(f"{BASE_URL}/query",json=payload)
            if response.status_code == 200:
                answer = response.json().get("answer","Sorry, I couldn't fetch the answer.")
                markdown_content = f"""#:blue[AI Trip Planner's Response] \n\n 
                -------
                {answer}
                -------
                ** This trip was planned by AI . Please verify all details before making any bookings.**"""
                st.markdown(markdown_content)
            else:
                st.error(f"Sorry, there was an error processing your request. Please try again later. Error: {response.text}")
    except Exception as e:
        raise f"An error occurred while connecting to the backend: {str(e)}"