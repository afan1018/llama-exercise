import openai
from utils.logger import log_response
from utils.scorer import score_response
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def load_prompt(filename: str, question: str) -> str:
    with open(f"prompts/{filename}", "r") as file:
        template = file.read()
    return template.replace("{{question}}", question)


def run_llm_prompt(prompt_name="template1.txt", temperature=0.7):
    question = "What is the meaning of life?"
    prompt = load_prompt(prompt_name, question)

    print("Running prompt...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

    answer = response["choices"][0]["message"]["content"]
    score = score_response(answer)
    log_response(question, answer, score)

    print(f"\n Answer: {answer}\n Score: {score}")
