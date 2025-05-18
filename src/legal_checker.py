import openai
import os

openai.api_key = os.getenv("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")

def check_legal_compliance(text):
    prompt = "Check if this legal document contains any clauses that may violate common business laws or pose a risk. List them clearly."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )
    issues = response.choices[0].message.content.strip()
    return issues.split("\n") if issues else []
