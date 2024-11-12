import datetime


def log_response(question, answer, score):
    timestamp = datetime.datetime.now().isoformat()
    with open("llama_responses.log", "a") as f:
        f.write(
            f"{timestamp} | Q: {question} | A: {answer.strip()} | Score: {score:.2f}\n"
        )
