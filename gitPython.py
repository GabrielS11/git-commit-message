from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def generate_commit_message(diff_text):
    """Generate a commit message using OpenAI API."""
    

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY não está definida. Verifica o teu .env")

    api_key = api_key.strip()
    
    client = OpenAI(api_key=api_key)

    prompt = (
        "Generate a concise and descriptive git commit message for the following code changes:\n\n"
        f"{diff_text}\n\nCommit message:"
    )

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"].strip()