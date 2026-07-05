print("=" * 50)
print("WELCOME TO THE QUIZ APP 📘📗📚")
print("=" * 50)


quiz = [
    {
        "question": "What keyword is used to display output in Python?",
        "options": ["A. display()", "B. print()", "C. echo()", "D. output()"],
        "answer": "B",
        "answer_text": "print()",
        "marks": 2,
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. input()", "B. scan()", "C. read()", "D. get()"],
        "answer": "A",
        "answer_text": "input()",
        "marks": 2,
    },
    {
        "question": "Which symbol is used to assign a value to a variable?",
        "options": ["A. ==", "B. =", "C. +=", "D. :="],
        "answer": "B",
        "answer_text": "=",
        "marks": 2,
    },
    {
        "question": "Which of these is a valid Python variable name?",
        "options": ["A. 2name", "B. first-name", "C. first_name", "D. class"],
        "answer": "C",
        "answer_text": "first_name",
        "marks": 3,
    },
    {
        "question": "Which data type stores whole numbers?",
        "options": ["A. float", "B. str", "C. int", "D. bool"],
        "answer": "C",
        "answer_text": "int",
        "marks": 3,
    },
    {
        "question": "Which data type stores decimal numbers?",
        "options": ["A. int", "B. float", "C. bool", "D. str"],
        "answer": "B",
        "answer_text": "float",
        "marks": 3,
    },
    {
        "question": "What is the correct way to create a string?",
        "options": ['A. "Hello"', "B. 100", "C. True", "D. 3.14"],
        "answer": "A",
        "answer_text": '"Hello"',
        "marks": 2,
    },
    {
        "question": "Which data type stores only True or False values?",
        "options": ["A. str", "B. bool", "C. list", "D. int"],
        "answer": "B",
        "answer_text": "bool",
        "marks": 3,
    },
    {
        "question": "Which operator is used for addition?",
        "options": ["A. *", "B. /", "C. +", "D. -"],
        "answer": "C",
        "answer_text": "+",
        "marks": 2,
    },
    {
        "question": "What is the result of 10 // 3?",
        "options": ["A. 3.33", "B. 3", "C. 4", "D. 1"],
        "answer": "B",
        "answer_text": "3",
        "marks": 5,
    },
]

score = 0
question_number = 1

#! Calculate total marks available
total_marks = sum(item["marks"] for item in quiz)

for question_number, item in enumerate(quiz, start=1):
    print(f"\nQuestion {question_number}")
    print("-" * 50)

    print(item["question"])

    for option in item["options"]:
        print(option)

    while True:
        user_answer = input("Your answer: (A-D) ").upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        print("❌ Please enter A, B, C, or D")

    if user_answer == item["answer"]:
        print(f"✅ Correct! (+{item["marks"]} marks)")
        score += item["marks"]
    else:
        print("❌ Wrong!")
        print(f"Correct Answer: {item['answer_text']}")

percentage = (score / total_marks) * 100

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
        message = "🌟 Excellent Work!"
    case "B":
        message = "👏 Very Good!"
    case "C":
        message = "👍 Good Job!"
    case "D":
        message = "📖 Keep Practicing!"
    case _:
        message = "💪 Try Again!"


print("\n" + "=" * 50)
print("QUIZ RESULTS")
print("=" * 50)

print(f"Marks :  {score}")
print(f"Total Marks : {total_marks}")
print(f"Your Percentage is: {percentage:.1f}%")
print(f"Your Grade is: {grade}")
print(f"Remark    : {message}")

print("=" * 50)
print("Thank you for taking the quiz!")
print("=" * 50)
