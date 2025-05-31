# Challenge 30 - Year Addition
# The wording was a bit unclear so...

year = 0
while True:
    try:
        year = int(input("Enter a year that is 4 digits long (####): "))
        if 1000 <= year <= 9999:
            break
        else:
            print("Year must be exactly 4 digits.")
    except ValueError:
        print("You must enter a number.")

total = sum(int(digit) for digit in str(year))
print(f"Sum of the digits is: {total}.")

attempts = 0
score = 0
guessed = set()

while attempts != 4:
    while True:
        try:
            attempt = int(input("What integers can your year divide by? Guess: "))
            break
        except ValueError:
            print("You must enter a number.")
            
    if attempt in guessed:
        print("You have already guessed that number. Try a different one.")
        continue
    guessed.add(attempt)
    if int(year) % attempt == 0:
        score += 1
        print("That's correct!")
    else:
        attempts += 1
        print(f"Sorry, that's wrong. You have {4 - attempts} attempts left.")

print(f"You're out of attempts! Your score is: {score}.")
