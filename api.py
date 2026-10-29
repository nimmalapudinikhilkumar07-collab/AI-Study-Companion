from fastapi import FastAPI,HTTPException
from  fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Literal
import os
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b",temperature=0.3)
class ChatMessage(BaseModel):
    role:Literal["user","assistant"]
    content:str

class QuestionRequest(BaseModel):
    question:str=Field(...,description="Enter the question you want to ask the Ai model",min_length=10,max_length=5000)
    difficulty:Literal["easy","medium","hard"]
    mode:Literal["explain","sumarize","quiz"]="explain"
    history:list[ChatMessage]=Field(default_factory=list)

app=FastAPI()

@app.post("/ask")

def ask_question(request:QuestionRequest):
    prompt=f""" Answer the following question at the requested difficulty level.
    if the mode is explain, provide a detailed explanation of the answer.
    If the mode is summarize, provide a concise summary of the answer. 
    If the mode is quiz, provide 5 to 7  multiple-choice questions with four options and indicate the correct answer. follow the instruction caefully and 
    provide the answer in a clear and concise mannner.And explain why the answer is correct and why the other options are incorrect.
    mode:{request.mode}
    difficulty:{request.difficulty}
    question:{request.question}
    
    Explain clearly and adjust your explanation to the specified difficulty. """
    print("Received history:",request.history)
    try:
        messages=[SystemMessage(content="you are an AI Study Comapanion." "Answer according to the requested mode"
                                "and difficulty level")]
        for i in request.history:
            if i.role=="user":
                messages.append(HumanMessage(content=i.content))
            elif i.role=="assistant":
                messages.append(AIMessage(content=i.content))
        messages.append(HumanMessage(content=prompt))

        response=model.invoke(messages)
        return {
            "question":request.question,
            "difficulty":request.difficulty,
            "answer":response.content
        }
    except Exception as e:
        print(f"AI service error:{type(e).__name__}: {e}")
        raise HTTPException(status_code=500,detail=" Our AI service is temporarily unavailable.Please try again shortly") from e
    



                        


    
