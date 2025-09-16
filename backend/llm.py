from groq import Groq

client = Groq(api_key="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")

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