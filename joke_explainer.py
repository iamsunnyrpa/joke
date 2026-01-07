import os
from openai import OpenAI

# Initialize the client
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ.get("GITHUB_TOKEN"),
)

def explain_joke_openai(joke):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains jokes."},
                {"role": "user", "content": f"Explain this joke: {joke}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# --- USER INPUT SECTION ---

print("--- AI Joke Explainer ---")
print("Type 'quit' or 'exit' to stop.\n")

while True:
    # 1. Capture user input
    user_joke = input("Enter a joke you want explained: ")

    # 2. Check if the user wants to quit
    if user_joke.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break

    # 3. Process the input if it's not empty
    if user_joke.strip():
        print("\nThinking...")
        explanation = explain_joke_openai(user_joke)
        print(f"\nAI Explanation:\n{explanation}\n")
        print("-" * 30)
    else:
        print("Please enter a joke!")
