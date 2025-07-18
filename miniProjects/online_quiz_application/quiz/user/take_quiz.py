import time
from quiz.questions import load_questions, get_random_questions
from quiz.evaluate import evaluate
from quiz.score import display_score

def take_quiz():
    print("🧠 Welcome to the Quiz!")
    questions = get_random_questions(load_questions())
    user_answers = []

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, opt in enumerate(q["options"], start=65):
            print(f"  {chr(idx)}. {opt}")
        ans = input("Your answer: ")
        user_answers.append(ans)
        time.sleep(0.5)

    score = evaluate(questions, user_answers)
    display_score(score, len(questions))
