# Challenge 8 - Arithmetic test
import random
import json
import os

FILENAME = "scores.txt"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    else:
        return {"A": {}, "B": {}, "C": {}}

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f)

def add_score(class_data, class_name, student_name, score):
    if student_name not in class_data[class_name]:
        class_data[class_name][student_name] = []
    class_data[class_name][student_name].append(score)

    if len(class_data[class_name][student_name]) > 3:
        class_data[class_name][student_name].pop(0)

def print_results(class_data):
    print("\nTEST RESULTS:")
    for class_name in sorted(class_data.keys()):
        print(f"\nClass {class_name}:")
        for student_name in sorted(class_data[class_name].keys()):
            scores = class_data[class_name][student_name]
            highest = max(scores)
            print(f"{student_name}: Highest score in last 3 tests = {highest} (Scores: {scores})")

def run_test(student_name):
    operations = ["plus", "minus", "multiplied by", "divided by"]
    correct = 0

    for i in range(1, 11):
        operation = random.choice(operations)

        if operation == "divided by":  # exception
            num2 = random.randint(1, 9)
            answer = random.randint(0, 9)
            num1 = num2 * answer
            calc = answer
        else:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            if operation == "plus":
                calc = num1 + num2
            elif operation == "minus":
                calc = num1 - num2
            elif operation == "multiplied by":
                calc = num1 * num2

        question = f"Question {i}: What is {num1} {operation} {num2}? "
        while True:
            try:
                ans = int(input(question))
                break
            except ValueError:
                print("Please enter a valid integer.")

        if ans == calc:
            print("That's right!")
            correct += 1
        else:
            print(f"Sorry, that is the wrong answer. Answer: {calc}")

    print("Here's your score!")
    print(f"{correct}/10")
    return correct

def menu(class_data):
    print("Let's begin the Arithmetic test.")
    while True:
        student_class = input("Please enter your class (A, B, C): ").strip().upper()
        if student_class not in ("A", "B", "C"):
            print("Please enter a valid class.")
            continue
        break
    student_name = input("Please enter your name: ").strip()

    score = run_test(student_name)
    add_score(class_data, student_class, student_name, score)
    save_data(class_data)

    print_results(class_data)

if __name__ == "__main__":
    class_data = load_data()
    menu(class_data)
