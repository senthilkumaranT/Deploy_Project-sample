from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Ensure the current directory is in the Python path for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm import llm_completion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend dev origins (adjust as needed for production)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.post("/llm", response_model=AnswerResponse)
def get_llm_answer(request: QuestionRequest):
    """
    Endpoint to get an answer from the LLM given a user's question.
    """
    try:
        answer = llm_completion(request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
