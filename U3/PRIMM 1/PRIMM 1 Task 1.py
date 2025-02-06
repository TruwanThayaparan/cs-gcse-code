# Task 1 Make
fruits = ["apples", "bananas", "pears"]
print(fruits[2])

# Task 1 Modify
fruits = ["apples", "bananas", "pears"]
fruits.append("oranges")
print(fruits[2])

# Task 1 Make
GCSEs = ["Mathematics", "English Literature", "English Language", "Biology",
         "Chemistry", "Physics", "Languages"]
print(GCSEs)

while True:
    newsubject = input("Enter an option subject...")
    if newsubject == "Exit":
        break
    else:
        GCSEs.append(newsubject)

print(len(GCSEs))
print(GCSEs)
