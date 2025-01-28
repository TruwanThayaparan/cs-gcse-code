definitions = ["a named location in memory that stores data that can be accessed throughout a program",
               "a variable that is set to never change the value",
               "the format in which data is stored in a variable",
               "when a decision is made within an algorithm based on a conditional statement",
               "when one programming construct is within another construct",
               "a programming construct that is a sequence of instructions that is repeated",
               "a ? is a data type used in programming that is used to represent text rather than numbers",
               "a ? is a sequence of characters and can contain letters, numbers, symbols and even spaces"]

correct = False
while not(correct):
    trigInput = input("Name a trigonometric function. ")

    for function in trigList:
        if trigInput == function or trigInput == function.lower():
            print("Yes, ",function," is a trigonometric function.")
            correct = True

    if not (correct):
        print("Sorry, that is not right.")
