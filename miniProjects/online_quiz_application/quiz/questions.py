import json
import random

def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)

def get_random_questions(questions, num=5):
    return random.sample(questions, min(num, len(questions)))
