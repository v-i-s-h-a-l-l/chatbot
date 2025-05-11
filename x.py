from openai import OpenAI

# Initialize the client
client = OpenAI(
    api_key="API Key is not pasted here for security reasons",
)


def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
