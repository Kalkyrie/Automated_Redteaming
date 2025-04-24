from dotenv import load_dotenv
import os

# Load the .env file
if load_dotenv(dotenv_path="./api_key.env"):
    print(".env file loaded successfully")
else:
    print("Failed to load .env file")

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

print(api_key)