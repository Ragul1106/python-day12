def evaluate(questions, answers):
    score = 0
    for q, a in zip(questions, answers):
        if q["answer"].strip().lower() == a.strip().lower():
            score += 1
    return score
