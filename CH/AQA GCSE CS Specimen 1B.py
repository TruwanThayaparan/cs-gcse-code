# Solution for last question of AQA GCSE CS Specimen Paper 1B

while True:
    try: 
        gokartSpeed = int(input("Enter the go-karts's speed (10 - 50 kilometres per hour/kph): "))
        if 10 <= gokartSpeed <= 50:
            break
        print("Sorry, that speed is out of bounds.")
    except ValueError:
        print("Input must be a numerical value.")

breakingDistance = gokartSpeed / 5

while True:
    wetGround = input("Is the ground wet? ").lower()
    if wetGround in ["yes", "no"]:
        break
    print("Input must be yes or no.")

if wetGround == "yes":
    breakingDistance *= 1.5

print("The breaking distance for the go-kart is", breakingDistance , "kph.")
