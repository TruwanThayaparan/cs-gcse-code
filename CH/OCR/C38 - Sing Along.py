# Challenge 38 - Sing Along
def bottle_text(n): # function here makes the code look nicer
    if n == 0:
        return "no green bottles"
    elif n == 1:
        return "1 green bottle"
    else:
        return f"{n} green bottles"

while True:
    try:
        start = int(input("Where should we start singing '10 Green Bottles' from? "))
        break
    except ValueError:
        print("You need to enter a number!")

for i in range(start, 0, -1):
    print(f"{bottle_text(i)} hanging on the wall,")
    print(f"{bottle_text(i)} hanging on the wall,")
    print("And if one green bottle should accidentally fall,")
    print(f"There'll be {bottle_text(i-1)} hanging on the wall.\n") # spacing
