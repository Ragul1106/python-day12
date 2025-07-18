import json

def create_quiz():
    questions = []
    print("📝 Admin: Enter quiz questions")
    while True:
        q = input("Question: ")
        o1 = input("Option A: ")
        o2 = input("Option B: ")
        o3 = input("Option C: ")
        o4 = input("Option D: ")
        ans = input("Correct Answer: ")
        questions.append({
            "question": q,
            "options": [o1, o2, o3, o4],
            "answer": ans
        })
        more = input("Add more questions? (y/n): ")
        if more.lower() != 'y':
            break

    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    print("✅ Quiz saved to questions.json")
