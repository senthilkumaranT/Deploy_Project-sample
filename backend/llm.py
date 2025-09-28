import os
from dotenv import load_dotenv

load_dotenv()

try:
    from groq import Groq
    print("GROQ library imported successfully")
except ImportError as e:
    print(f"Error importing GROQ library: {e}")
    Groq = None

# Initialize GROQ client with error handling
if Groq is None:
    print("ERROR: GROQ library could not be imported")
    client = None
else:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your_groq_api_key_here":
        print("WARNING: GROQ_API_KEY environment variable is not set or is using default value")
        print("Please set your GROQ API key in the .env file or environment variables")
        print("Example: GROQ_API_KEY=your_actual_api_key_here")
        # Create a dummy client for now to prevent import errors
        client = None
    else:
        try:
            print(f"Initializing GROQ client with API key: {api_key[:10]}...")
            client = Groq(api_key=api_key)
            print("GROQ client initialized successfully")
        except Exception as e:
            print(f"Error initializing GROQ client: {e}")
            client = None

def llm_completion(question):
    if client is None:
        return "Error: GROQ API key is not configured. Please set the GROQ_API_KEY environment variable with your actual API key from https://console.groq.com/"
    
    try:
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
    except Exception as e:
        return f"Error calling GROQ API: {str(e)}"

if __name__ == "__main__":
    question = input("Enter your question: ")
    answer = llm_completion(question)
    print(answer)