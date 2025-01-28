trigList = ["Sine", "Cosine", "Tangent", "Cotangent", "Secant", "Cosecant"]

correct = False
while not(correct):
    trigInput = input("Name a trigonometric function. ")

    for function in trigList:
        if trigInput == function or trigInput == function.lower():
            print("Yes, ",function," is a trigonometric function.")
            correct = True

    if not (correct):
        print("Sorry, that is not right.")
