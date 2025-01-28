trigList = ["Sine", "Cosine", "Tangent", "Cotangent", "Secant", "Cosecant"]

trigInput = input("Name a trigonometric function. ")

correct = False

for function in trigList:
    if trigInput == function or trigInput == function.lower():
        print("Yes, ",function," is a trigonometric function.")
        correct = True

if not (correct):
    print("Sorry, that is not right.")
