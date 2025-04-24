from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the .env file
if load_dotenv(dotenv_path="./api_key.env"):
    print(".env file loaded successfully")
else:
    print("Failed to load .env file")

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")



client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

print(completion.choices[0].message.content)
