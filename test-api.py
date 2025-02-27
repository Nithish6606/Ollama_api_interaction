import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def generate_response(prompt:str):
    # Ensure the API key is available
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    # Construct the URL
    url = f"http://127.0.0.1:8000/generate?prompt='{prompt}'"

    # Set headers
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers)

        # Check for HTTP errors
        response.raise_for_status()

        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    prompt:str = input("Enter the prompt:")
    result = generate_response(prompt)
    if result:
        print(result)
