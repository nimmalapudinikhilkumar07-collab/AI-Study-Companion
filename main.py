from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b",temperature=0.3)

chat_history=[]
print("Enter exit if you want to quit the program")
while True:
    question=input("enter your question: ")
    
    if question.lower()=="exit":
            print("Exiting the program bye bye!...")
            break
    chat_history.append(HumanMessage(content=question))
    response=model.invoke(chat_history)

    ai_response=response.content
    chat_history.append(AIMessage(content=ai_response))
    print("AI: ",ai_response)

    
