def score_response(answer: str) -> float:
    """
    Naive scoring function that rewards longer, thoughtful responses.
    Replace with semantic similarity, factual accuracy, etc.
    """
    return min(len(answer.strip()) / 100.0, 1.0)
