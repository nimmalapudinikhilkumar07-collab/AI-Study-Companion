import streamlit as st
import requests

st.set_page_config(page_title="AI Study Companion",layout="centered")

st.title("AI Study Companion")
st.write("Your personal AI-powered learning assistant. Ask questions, get explanations, summaries, and quizzes tailored to your learning needs.")
st.divider()

st.subheader("what would you like to study today?")

mode=st.selectbox("choose the study mode",["explain","summarize","quiz"])

difficulty=st.selectbox("choose the difficulty level",["easy","medium","hard"])

question=st.text_area("Enter your question here",placeholder="Type your question here...",height=150)   

if st.button("Generate", type="primary"):
    if not question.strip():
        st.warning("Please enter a question or some notes.")
    else:
        payload = {
            "question": question,
            "mode": mode.lower(),
            "difficulty": difficulty.lower()
        }

        try:
            with st.spinner("Your AI Study Companion is thinking..."):
                response = requests.post(
                    "https://ai-study-companion-9sly.onrender.com/ask",
                    json=payload,
                    timeout=60
                )

            if response.status_code == 200:
                result = response.json()
                st.subheader("📚 AI Response")
                st.write(result["answer"])
            else:
                st.error(f"API error: {response.status_code}")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to FastAPI. "
                "Make sure your backend server is running."
            )
        except requests.exceptions.Timeout:
            st.error("The request took too long. Please try again.")
