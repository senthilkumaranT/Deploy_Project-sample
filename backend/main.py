from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Ensure the current directory is in the Python path for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm import llm_completion

app = FastAPI()

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
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
