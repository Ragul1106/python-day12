from questions import quiz
from evaluate import evaluate

score = 0
for q in quiz:
    ans = input(q["q"] + " ")
    if evaluate(ans, q["a"]):
        score += 1

print(f"You scored {score}/{len(quiz)}")
