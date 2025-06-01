# Challenge 70 - Of mice and men
import random

def generate_number():
    return str(random.randint(0, 9999)).zfill(4)

def get_guess():
    while True:
        guess = input("Guess the 4-digit number: ").strip()
        if len(guess) == 4 and guess.isdigit():
            return guess
        print("Invalid input. Please enter exactly 4 digits.")

def count_mice_and_men(secret, guess):
    mice = 0
    men = 0

    secret_used = [False] * 4
    guess_used = [False] * 4

    for i in range(4):
        if guess[i] == secret[i]:
            mice += 1
            secret_used[i] = True
            guess_used[i] = True

    for i in range(4):
        if not guess_used[i]:
            for j in range(4):
                if not secret_used[j] and guess[i] == secret[j]:
                    men += 1
                    secret_used[j] = True
                    break

    return mice, men

def play_game():
    secret = generate_number()
    guesses = 0

    print("Welcome to the 'Mice and Men' game!")
    print("Guess the 4-digit number. For every digit:\n")
    print("Mouse = correct digit in the correct place")
    print("Man   = correct digit in the wrong place\n")

    while True:
        guess = get_guess()
        guesses += 1

        mice, men = count_mice_and_men(secret, guess)
        print(f"Mice: {mice}, Men: {men}")

        if mice == 4:
            print(f"\nCongratulations! You guessed the number ({secret}) in {guesses} guesses.")
            break

if __name__ == "__main__":
    play_game()
