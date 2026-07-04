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
    },
    {
        "question": "Who is the first man God Created?",
        "answer": "adam"
    },
    {
        "question": "What is 10 x 5",
        "answer": "50"
    }
]


score = 0
question_number = 1

for item in quiz:
    print(f"\nQuestion {question_number}")

    user_answer = input(item["question"] + " ")

    if user_answer.lower() == item["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print(f"Correct Answer: {item['answer'].capitalize()}")

    question_number += 1

percentage = (score / len(quiz)) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


match grade:
    case "A":
        message = "Excellent 😀"
    case "B":
        message = "Very Good 😋"
    case "C":
        message = "Good Job 👏"
    case "D":
        message = "Keep Practicing 😉"
    case _:
        message = "Try Again 🙁"


print("\n" + "=" * 40)
print("QUIZ RESULTS")
print("=" * 40)

print(f"Your score is {score} / {len(quiz)}")
print(f"Your Percentage is: {percentage:.1f}%")
print(f"Your Grade is: {grade}")
print(message)
