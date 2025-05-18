import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize this legal document."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def extract_key_info(text):
    prompt = "Extract key clauses, parties involved, and dates from this legal document."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()