import streamlit as st
import requests

# FastAPI backend URL
API_URL = "https://ai-study-companion-9sly.onrender.com/ask"

# Page configuration
st.set_page_config(
    page_title="AI Study Companion",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Companion")
st.write("Your personal AI assistant for learning!")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Select AI mode
mode = st.selectbox(
    "Choose a mode",
    ["Explain", "Summarize", "Quiz"]
)

# Select difficulty
difficulty = st.selectbox(
    "Choose the difficulty level",
    ["easy", "medium", "hard"]
)

# Display previous conversation messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input for a new question
question = st.chat_input("Ask your question here...")

if question:
    # Display the user's question
    with st.chat_message("user"):
        st.write(question)

    # Save the user's question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    # Prepare the API request
    payload = {
        "question": question,
        "mode": mode.lower(),
        "difficulty": difficulty.lower(),
        "history": st.session_state.messages[:-1]
    }

    try:
        with st.spinner("Your AI Study Companion is thinking..."):
            response = requests.post(
                API_URL,
                json=payload,
                timeout=60
            )

        if response.status_code == 200:
            result = response.json()
            answer = result["answer"]

            # Display the AI response
            with st.chat_message("assistant"):
                st.write(answer)

            # Save the AI response
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        else:
            st.error(f"API error: {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to FastAPI. "
            "Please try again later."
        )

    except requests.exceptions.Timeout:
        st.error("The request took too long. Please try again.")

    except requests.exceptions.RequestException as e:
        st.error(f"An unexpected network error occurred: {e}")

# Clear conversation button
if st.session_state.messages:
    if st.button("🗑️ Clear conversation"):
        st.session_state.messages = []
        st.rerun()
