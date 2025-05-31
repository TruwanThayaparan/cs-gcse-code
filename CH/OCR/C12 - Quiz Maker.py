# Challenge 12 - Quiz Maker
# note: the file is embedded here

import random

quiz = [
    {
        "question": "What is the purpose of a loop in programming?",
        "options": ["A. To store data", "B. To repeat a set of instructions", "C. To declare a variable", "D. To define a function"],
        "answer": "B"
    },
    {
        "question": "What does the following Python code print?\n\nx = 3\ny = 5\nprint(x + y)",
        "options": ["A. 8", "B. 35", "C. 3 + 5", "D. Error"],
        "answer": "A"
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": ["A. 2ndValue", "B. my-value", "C. first_name", "D. class"],
        "answer": "C"
    },
    {
        "question": "What is the output of this code?\n\nfor i in range(3):\n    print(\"Hello\")",
        "options": ["A. Hello", "B. Hello Hello Hello", "C. Hello (3 times on new lines)", "D. Error"],
        "answer": "C"
    },
    {
        "question": "What is the correct syntax to define a function in Python?",
        "options": ["A. function myFunction():", "B. def myFunction():", "C. func myFunction()", "D. define myFunction()"],
        "answer": "B"
    },
    {
        "question": "Which data type would be most appropriate to store a person's age?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "B"
    },
    {
        "question": "What is the purpose of an if statement in programming?",
        "options": ["A. To create a loop", "B. To define a function", "C. To make decisions", "D. To end a program"],
        "answer": "C"
    },
    {
        "question": "What does the len() function do in Python?",
        "options": ["A. Calculates the sum of numbers", "B. Returns the length of an object", "C. Converts a string to lowercase", "D. Finds the largest number"],
        "answer": "B"
    },
    {
        "question": "What value is returned by the expression 5 % 2 in Python?",
        "options": ["A. 2", "B. 2.5", "C. 1", "D. 0"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a boolean value?",
        "options": ["A. \"True\"", "B. yes", "C. 1", "D. False"],
        "answer": "D"
    }
]

print("Let's start the CS quiz!")
selected_questions = random.sample(quiz, 5)
user_answers = []
correct = 0

for i, q in enumerate(selected_questions, 1):
    print(f"Q{i}: {q['question']}")
    for option in q['options']:
        print(option)
    print()  # blank line

    while True:
        ans = input("Your answer (A, B, C, D): ").strip().upper()
        if ans not in ["A", "B", "C", "D"]:
            print("You must enter A, B, C, or D.")
        else:
            break

    user_answers.append(ans)
    if ans == q['answer']:
        correct += 1

print(f"\nYou got {correct} out of 5 correct!\n")

print("Review:")
for i, (q, user_ans) in enumerate(zip(selected_questions, user_answers), 1):
    correct_ans = q['answer']
    print(f"Q{i}: {q['question']}")
    print(f"Your answer: {user_ans}")
    print(f"Correct answer: {correct_ans}")
    if user_ans == correct_ans:
        print("Result: Correct!\n")
    else:
        print("Result: Incorrect.\n")
