# Challenge 17 - Hangman
def hangman():
    while True:
        word = input("\nEnter the word to guess: ").lower()

        # Validate number of chances input
        while True:
            try:
                chances = int(input("Enter the number of chances: "))
                break
            except ValueError:
                print("You must enter a number.")

        word_letters = list(word)
        guessed_letters = []
        incorrect_letters = []
        current_guess = ['_' for _ in word_letters]

        while chances > 0 and '_' in current_guess:
            print("\nWord:", ' '.join(current_guess))
            print("Incorrect guesses:", ', '.join(incorrect_letters))
            print(f"Chances left: {chances}")

            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters or guess in incorrect_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
                continue

            if guess in word_letters:
                print(f"Good guess! '{guess}' is in the word.")
                guessed_letters.append(guess)
                for idx, letter in enumerate(word_letters):
                    if letter == guess:
                        current_guess[idx] = guess
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                incorrect_letters.append(guess)
                chances -= 1

        if '_' not in current_guess:
            print("\nCongratulations! You guessed the word:", word)
        else:
            print("\nGame over! You ran out of chances.")
            print(f"The word was: {word}")

        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay in ('no', 'n'):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    hangman()
