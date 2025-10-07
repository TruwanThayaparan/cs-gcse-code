# guessing game
import random
while True:
    random_number = random.randint(0,10)
    guesses = 0
    while guesses < 5:
        #print(random_number)
        while True:
          try:
            guess = int(input("Guess my number! It's between 0 and 10: "))
            if 0 <= guess <= 10:
              break
            else:
              print("Number must be between 0 and 10.")
          except ValueError:
            print("You must enter a number.")

        if guess == random_number:
          print("You guessed my number!")
          break
        elif guess > random_number:
          print("Lower...")
          guesses += 1
          print(f"Guesses left: {5 - guesses}")
        else:
          print("Higher...")
          guesses += 1
          print(f"Guesses left: {5 - guesses}")
          
    if guesses == 5:
        print(f"Oh no, you lost! My number was {random_number}")
      
    restart = input("Would you like to play again? ")
    if restart == "yes":
      pass
    else:
      print("Goodbye!")
      break
    
