# Challenge 35 - Game Of Chance
import random

print("WELCOME TO THE GAME OF CHANCE! MAKE SURE TO READ ABOUT GAMBLEAWARE FIRST.")
money = 100

while True:
    tries = []
    bets = 1

    while True:
        print(f"YOUR BALANCE: {money}")

        while True:
            try:
                guess = int(input("Guess a number between 0 and 30: "))
                if 0 <= guess <= 30:
                    break
                print("Number must be between 0 and 30. \n")
            except ValueError:
                print("You must enter a number. \n")

        if money == 0:
            print("You have no more money, continuing...")
            break

        if money < 10:
            print(f"You can bet up to {money} units.")
        else:
            print(f"You can bet up to 10 units.")

        try:
            print(f"Bet {bets}")
            bet = int(input("How many units will you bet: "))
            if 1 <= bet <= 10 and 0 <= (money - bet):
                tries.append((guess, bet))  # Store both guess and bet
                money -= bet
                bets += 1
            else:
                if bet > money:
                    print(f"TOO HIGH! Maximum bet: {money} \n")
                else:
                    print("Number must be between 1 and 10. \n")
        except ValueError:
            print("You must enter a number. \n")

        keep_going = None
        while keep_going not in ("yes", "no"):
            keep_going = input("Bet again (yes/no)? ").lower()

        if keep_going == "no":
            break

    # After betting is done, roll the random number
    random_number = random.randint(0, 30)
    print(f"\n The random number is: {random_number}")

    for guess, bet in tries:
        if guess == random_number:
            multiplier = 1
            if random_number % 2 == 0:
                multiplier *= 2
            if random_number % 10 == 0:
                multiplier *= 3
            if random_number > 1:
                is_prime = True
                for j in range(2, int(random_number**0.5) + 1):
                    if random_number % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    multiplier *= 5
            if random_number < 5:
                multiplier *= 2

            winnings = bet * multiplier
            money += winnings
            print(f"You guessed {guess} correctly! Multiplier: x{multiplier}, Winnings: {winnings}")
        else:
            print(f"You guessed {guess}. No win.")

    if money <= 0:
        print("OH NO, YOU RAN OUT OF MONEY!")
        break
