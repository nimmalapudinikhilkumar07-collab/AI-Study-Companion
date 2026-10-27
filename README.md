📚 AI Study Companion

An AI-powered learning assistant that helps students understand concepts, summarize notes, and generate quizzes at different difficulty levels.

✨ Features

- Explain: Get clear explanations of academic topics.
- Summarize: Convert notes and lengthy content into concise summaries.
- Quiz: Generate 5 multiple-choice questions with answers and explanations.
- Difficulty Selection: Choose Easy, Medium, or Hard.
- AI-Powered Responses: Uses a Groq-hosted language model through LangChain.
- Web Interface: Interact with the application using Streamlit.
- REST API: FastAPI handles requests between the frontend and the language model.

🛠️ Tech Stack

- Python
- Groq LLM
- LangChain
- FastAPI
- Streamlit
- Requests
- Python-dotenv

📁 Project Structure

AI_Study_Companion/
├── main.py
├── api.py
├── frontend.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation and Setup

1. Clone the Repository

git clone YOUR_REPOSITORY_URL
cd AI-Study-Companion

Replace "YOUR_REPOSITORY_URL" with your GitHub repository URL.

2. Create a Virtual Environment

python -m venv .venv

On Windows CMD, activate it using:

.venv\Scripts\activate.bat

3. Install Dependencies

python -m pip install -r requirements.txt

4. Configure Your API Key

Create a ".env" file in the project root and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

Replace the placeholder with your actual API key.

Security: Never upload your ".env" file or expose your API key publicly.

5. Start the FastAPI Backend

python -m uvicorn api:app --reload

The API will run at "http://127.0.0.1:8000".

Explore and test the endpoints at "http://127.0.0.1:8000/docs".

6. Start the Streamlit Frontend

Open a second terminal, activate the same virtual environment, and run:

python -m streamlit run frontend.py

Open the local URL displayed in the terminal to use the application.

🔄 How It Works

1. The user selects a study mode and difficulty.
2. Streamlit sends the request to the FastAPI backend.
3. FastAPI prepares the prompt and sends it to the Groq-hosted language model.
4. The model generates a response.
5. The response is returned to the frontend and displayed to the user.

🚀 Future Improvements

- Interactive quizzes with selectable answers.
- Automatic quiz scoring and feedback.
- Conversation history.
- Improved user interface.
- Persistent storage for saved study sessions.

This project was built to practise LLM integration, REST API development, and frontend-backend communication using Python.

It demonstrates how a language model can be integrated into a practical learning appli
