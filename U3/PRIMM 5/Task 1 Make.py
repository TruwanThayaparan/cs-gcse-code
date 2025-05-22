# guessing game
import random
while True:
    random_number = random.randint(1,5)
    guesses = 0
    while guesses < 5:
        #print(random_number)
        while True:
          try:
            guess = int(input("Guess my number! It's between 0 and 10: "))
            if 0 <= guess <= 10:
              break
            else:
              print("NUMBER MUST BE BETWEEN 0 AND 10.")
          except ValueError:
            print("ENTER A NUMBER.")

        if guess == random_number:
          print("You guessed my number!")
          break
        elif guess > random_number:
          print("Lower...")
          guesses += 1
          print("Guesses left:", 5 - guesses)
        else:
          print("Higher...")
          guesses += 1
          print("Guesses left:", 5 - guesses)
          
    if guesses == 5:
        print("Oh no, you lost! My number was:",random_number)
      
    restart = input("Would you like to play again?")
    if restart == "yes":
      pass
    else:
      print("Goodbye!")
      break
    
