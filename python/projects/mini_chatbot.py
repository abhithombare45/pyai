import openai

openai.api_key = "your_openai_api_key"  # Replace with your API key

def chatbot():
    print("🤖 AI Chatbot (Type 'exit' to stop)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Chatbot:", response["choices"][0]["message"]["content"])

chatbot()
