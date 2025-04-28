# Challenge 30 - Year Addition
# The wording was a bit unclear so...

year = 0
while 1000 > int(year) or int(year) > 9999:
    year = input("Enter a year that is 4 digits long (####): ")

total = 0
for i in range(4):
    total += int(year[i])

print("Sum of the digits is:", total)

attempts = 0
score = 0
guessed = set()

while attempts != 4:
    attempt = int(input("What integers can your year divide by? Guess: "))
    if attempt in guessed:
        print("You already guessed that number. Try a different one.")
        continue
    guessed.add(attempt)
    if int(year) % attempt == 0:
        score += 1
        print("That's correct!")
    else:
        attempts += 1
        print("Sorry, that's wrong. You have", 4 - attempts, "attempts left.")

print("You're out of attempts! Your score is:", score)
