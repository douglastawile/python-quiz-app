print("=" * 40)
print("WELCOME TO THE QUIZ APP 📘📗📚")
print("=" * 40)


quiz = [
    {
        "question": "What is the capital of Ghana?",
        "answer": "accra"
    },
    {
        "question": "What is 5 + 5?",
        "answer": "10"
    },
    {
        "question": "What color is the sky?",
        "answer": "blue"
    }
]


score = 0
question_number = 1

for item in quiz:
    print(f"\nQuestion {question_number}")

    user_answer = input(item["question"] + " ")

    question_number += 1

    if user_answer.lower() == item["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print(f"Correct Answer: {item['answer'].capitalize()}")

print("\nQuiz Completed!")
print(f"Your score is {score} / {len(quiz)}")
