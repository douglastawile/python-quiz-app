print("=" * 30)
print("WELCOME TO THE QUIZ APP 📘📗📚")
print("=" * 30)

questions = [
    "What is the capital of Ghana?",
    "What is 5 + 5?",
    "What color is the sky?"
]

answers = [
    "accra",
    "10",
    "blue"
]

score = 0

for question in range(len(questions)):
    print(f"\nQuestion {question + 1}")

    user_answer = input(questions[question] + " ")

    if user_answer.lower() == answers[question]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print("\nQuiz Completed!")
print(f"Your Score is: {score}/{len(questions)}")
