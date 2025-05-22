# rock, paper, scissors!
import random
choices = ["rock", "paper", "scissors"]

while True:
    comp_choice = choices[random.randint(0,2)]
    while True:
        hum_choice = input("Rock Paper Scissors! What do you pick? ").lower()
        if hum_choice in ["rock", "paper", "scissors", "end"]:
            if hum_choice == "end":
                print("Bye!")
            break
        else:
            print("THAT'S NOT A VALID CHOICE.")

    if hum_choice == "end": break

    if comp_choice == hum_choice:
        print("Draw!")
    elif comp_choice == "rock" and hum_choice == "paper":
        print("You win!")
    elif comp_choice == "rock" and hum_choice == "scissors":
        print("You lose!")
    elif comp_choice == "paper" and hum_choice == "scissors":
        print("You win!")
    elif comp_choice == "paper" and hum_choice == "rock":
        print("You lose!")
    elif comp_choice == "scissors" and hum_choice == "rock":
        print("You win!")
    else:
#elif comp_choice == "scissors" and hum_choice == "paper":
        print("You lose!")
    
    print(f"Computer choice: {comp_choice} \nYour choice: {hum_choice} \n")
