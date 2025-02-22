# Snowman Game
# Challenge 1

'''
Snowman is an alternate version of the 'hangman'. In the game a word is selected and those playing the game guess letters that could be in the word. 
When a player guesses a correct letter the position(s) of this letter in the word are revealed. When a player guesses wrongly, a 'try' is used.

Your game should work as follows:
1. The program chooses a random word from the 'dictionary' provided. In EASY mode, this should be 5 letters or less. In MEDIUM mode, this should be between 6 and 10 letters (inclusive). In DIFFICULT mode, the word selected is 11 or more letters.
2. Once the word is selected - the user is shown the number of letters in underscore form. For example, if 'snowball' is selected, the user would see _ _ _ _ _ _ _ _.
3. The user keeps guessing letters or, if they're feeling brave, the whole word. If they guess a single letter and they were correct, reveal where that letter is within the word. For example, if the user guesses l then the display would be _ _ _ _ _ _ ll.
4. If they guess more than one letter, treat this as a guess of the word itself. Either they are totally correct or totally wrong.
5. The case of the guesses doesn't matter (so 'l' is the same as 'L').
6. Each time a user guesses a letter wrong, display the previously incorrect letters alongside the hidden word. Don't let them guess this letter again. 
For either a wrong letter or a word word guess, show that a try has been used by displaying the following stages of a snowman being built using ASCII art: bottom snowball, middle snowball, head snowball, face, branches and buttons, top hat
7. After the top hat has been added, it's game over for the user. They win if they guess correctly before all stages of the snowman build are complete.

Dictionary (this is in python, you will need to change it if you are using another programming language):
dictionary = [
    'Adventure', 'Journey', 'Swim', 'Freedom', 'Silence', 'Opportunity', 'Star', 
    'Holiday', 'Jump', 'Destination', 'Mystery', 'Frog', 'Enthusiastic', 'Book', 
    'Tree', 'Balloon', 'Constellation', 'Ocean', 'Revolution', 'Rain', 'Cat', 
    'Celebration', 'Sun', 'Rainbow', 'Guitar', 'Imagination', 'Blue', 'Sunrise', 
    'Extravagant', 'Unbelievable'
]

ASCII ART: Here's an example of the snowman ASCII art in Python.
  if guesses >= 1:
    bottomSnowball = "  (       )" + "\n" +"   \'-----\'" 
    snowman.append(bottomSnowball)

  if guesses >= 2:
    middleSnowball = "   (     )"
    snowman.insert(0,middleSnowball)
          
  if guesses >= 3:
    headSnowball = "    (   )"
    snowman.insert(0,headSnowball)

  if guesses >= 4:
    snowman[0] = "    ('v')"

  if guesses >= 5:
    snowman[1] = "--<(  .  )>--"
    snowman[2] = "  (   .   )" + "\n" + "   \'-----\'"

  if guesses >= 6:
    topHat = "     ___" + "\n" + "   _|___|_"
    snowman.insert(0,topHat)
    
'''

# Snowman Game
import random

# dictionary of the words used in the game
dictionary = [
    'Adventure', 'Journey', 'Swim', 'Freedom', 'Silence', 'Opportunity', 'Star', 
    'Holiday', 'Jump', 'Destination', 'Mystery', 'Frog', 'Enthusiastic', 'Book', 
    'Tree', 'Balloon', 'Constellation', 'Ocean', 'Revolution', 'Rain', 'Cat', 
    'Celebration', 'Sun', 'Rainbow', 'Guitar', 'Imagination', 'Blue', 'Sunrise', 
    'Extravagant', 'Unbelievable'
]

# choose the mode/difficulty
def chooseMode():
    mode = ""
    while mode.upper() not in ["E", "Easy", "M", "Medium", "H", "Hard"]:
        mode = input("Choose the mode of the word you want to guess. Easy = E, Medium = M, Hard = H: ")
        if mode.upper() in ["E", "Easy", "M", "Medium", "H", "Hard"]:
            print("Your mode has been set. Choosing the word... \n")
            break
        else:
            print("Error! Make sure the mode is valid. Try again.")

    mode = mode.upper()
    if mode == "Easy": mode = "E"
    if mode == "Medium": mode = "M"
    if mode == "Hard": mode = "H"
    return mode

# choose a random word based off off the word
def chooseWord(mode):
    while True:
        randomItem = random.randint(0, len(dictionary) - 1)
        choice = dictionary[randomItem].strip().lower()

        if mode == "E" and len(choice) <= 5:
            break
        elif mode == "M" and len(choice) <= 10 and len(choice) > 5:
            break
        elif mode == "H" and len(choice) >= 11:
            break
    return choice

# show the letters
def showLetters(word, revealedLetters, guessedLetters):
  unk = ""

  for letter in word:
    if letter in revealedLetters:
      unk += (letter + " ")
    else:
      unk += "_ "

  guessedAlready = " ".join(guessedLetters)

  if len(guessedAlready) == 0:
    return unk + "\n"
  else:
    return unk + "\t Already guessed: " + guessedAlready + "\n"

# create the snowman
def makeSnowman(guesses):
  snowman = []
  if guesses >= 1:
    bottomSnowball = "  (       )" + "\n" +"   \'-----\'" 
    snowman.append(bottomSnowball)

  if guesses >= 2:
    middleSnowball = "   (     )"
    snowman.insert(0,middleSnowball)
          
  if guesses >= 3:
    headSnowball = "    (   )"
    snowman.insert(0,headSnowball)

  if guesses >= 4:
    snowman[0] = "    ('v')"

  if guesses >= 5:
    snowman[1] = "--<(  .  )>--"
    snowman[2] = "  (   .   )" + "\n" + "   \'-----\'"

  if guesses >= 6:
    topHat = "     ___" + "\n" + "   _|___|_"
    snowman.insert(0,topHat)
  return "\n".join(snowman)

# main program
def snowmanGame():
  print("Welcome to Snowball, a ripoff of Hangman! \n")
  mode = chooseMode()
  word = chooseWord(mode)

  print("Let's begin... \n")
  print(showLetters(word, "", []))

  attempts = 0
  incorrectGuesses = []
  correctGuesses = []
  while attempts < 6:
    guess = input("Make a guess: ")

    while (guess.lower() in incorrectGuesses or guess.lower() in correctGuesses) or (guess.isalpha() == False):
      if (guess.lower() in incorrectGuesses or guess.lower() in correctGuesses):
        guess = input("You guessed that before. Make another guess: ")
      else:
        guess = input("Your input must be a letter or word. Make another guess: ")

    guess = guess.lower()
    if guess not in word:
      incorrectGuesses.append(guess)
      attempts += 1
      print("Incorrect! You have " + str(6 - attempts) + " guesses left! \n")
    else:
      if guess == word:
          print("You've guessed the word! It's " + word + "! \n")
          break
      else:
          correctGuesses.append(guess)

    showAttempt = showLetters(word, correctGuesses, incorrectGuesses)

    if "_" not in showAttempt:
      print(showAttempt)
      print("You've guessed the word! It's " + word + "! \n")
      break
    else:
      print(showAttempt)
      print(makeSnowman(attempts))

  else:
        print("You're out of guesses. The word was " + word + ". \n")

  print("That ends our game of Snowball. Bye!")

snowmanGame()
