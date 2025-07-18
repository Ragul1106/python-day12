# main.py
from textutils.analyze import summary
from textutils.utils import to_upper
from textutils.sanitize import remove_numbers

if __name__ == "__main__":
    print("🛠️ Text Utility Toolkit")
    user_input = input("Enter your text:\n")

    print("\n📊 Summary:")
    report = summary(user_input)
    for key, value in report.items():
        print(f"{key.capitalize()}: {value}")

    print("\n🔠 Upper Case Text:")
    print(to_upper(user_input))

    print("\n🔢 Text without numbers:")
    print(remove_numbers(user_input))
