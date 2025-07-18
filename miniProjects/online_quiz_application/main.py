from quiz.admin.create_quiz import create_quiz
from quiz.user.take_quiz import take_quiz

if __name__ == "__main__":
    print("🎓 Online Quiz Application")
    role = input("Are you an Admin or User? (a/u): ").strip().lower()

    if role == 'a':
        create_quiz()
    elif role == 'u':
        take_quiz()
    else:
        print("❌ Invalid choice.")
