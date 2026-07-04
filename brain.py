from ollama import chat

def ask(prompt):
    response = chat(
        model="llama3:latest",
        message=[]