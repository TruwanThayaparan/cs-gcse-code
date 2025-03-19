# Solution for RL Challenge 2
# Note: This is an answer to an altered version of the final question of AQA GCSE CS Specimen Paper 1B

while True:
    try: 
        hoverBikeSpeed = int(input("Enter the hover-bike's speed (20 - 100 kilometres per hour/kph): "))
        if 20 <= hoverBikeSpeed <= 100:
            break
        print("Sorry, that speed is out of bounds.")
    except ValueError:
        print("Input must be a numerical value.")

stoppingDistance = (hoverBikeSpeed ^ 2) / 150

while True:
    atmosphericConditions = input("What are the atmospheric conditions (dust storm, clear, foggy)? ").lower()
    if atmosphericConditions in ["dust storm", "clear", "foggy"]:
        break
    print("Sorry, that's not a valid atmospheric condition.")

if atmosphericConditions == "dust storm":
    stoppingDistance *= 2
elif atmosphericConditions == "foggy":
    stoppingDistance *= 1.5

while True:
        stabilisersActive = input("Are the hover-bike's anti-gravity stabilisers active (yes or no)? ").lower()
        if stabilisersActive in ["yes", "no"]:
            break
        print("Sorry, that's not a valid response.")

if stabilisersActive == "no":
    stoppingDistance *= 1.25

print("The stopping distance for the hover-bike is", round(stoppingDistance, 2) , "kph.")
