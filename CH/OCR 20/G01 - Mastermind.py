# Challenge 01 - Mastermind

import random

scores = []

def show_high_score():
    if not scores:
        print("No high scores yet. Be the first to set one!")
        return
    best_score = min(scores, key=lambda x: x[1])
    print(f"Current high score: {best_score[0]} with {best_score[1]} guesses.")
  
print("Welcome to Mastermind. Can you get the high score (least amount of guesses)?")

def check_numbers(mode, guess, number):
    if guess == number:
        return "jackpot"
    
    if mode == "easy":
        positions = []
        for i in range(len(number)):
            positions.append(guess[i] == number[i])
        pos_str = ", ".join(f"Pos {i+1}: {'Correct' if correct else 'Wrong'}" 
                            for i, correct in enumerate(positions))
        return f"Positions you got correct: {pos_str}"
    
    elif mode in ["medium", "hard"]:
        count = 0
        guess_counts = {}
        number_counts = {}

        for d in guess:
            guess_counts[d] = guess_counts.get(d, 0) + 1
        for d in number:
            number_counts[d] = number_counts.get(d, 0) + 1
        
        for digit in guess_counts:
            if digit in number_counts:
                count += min(guess_counts[digit], number_counts[digit])
        
        return f"Numbers you got right: {count}"

def get_valid_guess(length):
    while True:
        guess = input(f"Guess the {length}-digit number: ")
        if len(guess) != length or not guess.isdigit():
            print(f"Invalid input. Please enter exactly {length} digits.")
        else:
            return guess

def game():
    while True:
        show_high_score()
        print("\nStarting a new game...")
        
        while True:
            mode = input("Please enter the difficulty (easy/medium/hard): ").strip().lower()
            if mode in ("easy", "medium", "hard"):
                break
            print("Please choose a valid mode: easy, medium, or hard.")

        length = 5 if mode == "hard" else 4
        number = str(random.randint(0, 10**length - 1)).zfill(length)

        guesses = 0
        while True:
            guess = get_valid_guess(length)
            guesses += 1
            result = check_numbers(mode, guess, number)
            if result == "jackpot":
                print(f"Congratulations! You guessed the number {number}!")
                print(f"It took you {guesses} guesses.")
                break
            else:
                print(result)

        name = input("Let's save your score. Enter your name: ") # let's say a new person comes in like an arcade game.
        scores.append((name, guesses))

        keep_playing = input("Would you like to play again? (yes/no): ").strip().lower()
        if keep_playing not in ("yes", "y"):
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    game()
