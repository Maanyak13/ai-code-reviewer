import requests
from .prompt_template import generate_review_prompt

def review_code(code, language):
    prompt = generate_review_prompt(code, language)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "deepseek-coder",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"]
