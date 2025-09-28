from groq import Groq

import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def llm_completion(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Provide step by step instructions."
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    question = input("Enter your question: ")
    answer = llm_completion(question)
    print(answer)