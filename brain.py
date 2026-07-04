from ollama import chat

def ask(prompt):
    response = chat(
        model="llama3:latest",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
    )
    return response.message.content