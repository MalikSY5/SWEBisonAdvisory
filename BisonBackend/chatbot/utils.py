import openai
import os
import sys

openai.api_key = os.getenv("OPENAI_API_KEY"); #Replace with your environment variable name

def ask_openai(prompt):
    response = openai.Completion.create(
        model="text-davinci-004",  # Replace with appropriate model
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
