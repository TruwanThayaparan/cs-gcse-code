# rock, paper, scissors! AUTOMATED
import random
choices = ["rock", "paper", "scissors"]

total_plays = 0
c1_wins = 0
c2_wins = 0
draws = 0

while total_plays < 200:
    comp_choice = choices[random.randint(0,2)]
    comp_choice2 = choices[random.randint(0,2)]

    if comp_choice == comp_choice2:
        print("Draw!")
        draws += 1
      
    elif comp_choice == "rock" and comp_choice2 == "paper":
        print("C1 wins!")
        c1_wins += 1
      
    elif comp_choice == "rock" and comp_choice2 == "scissors":
        print("C2 wins!")
        c2_wins += 1
      
    elif comp_choice == "paper" and comp_choice2 == "scissors":
        print("C1 wins!")
        c1_wins += 1
      
    elif comp_choice == "paper" and comp_choice2 == "rock":
        print("C2 wins!")
        c2_wins += 1
      
    elif comp_choice == "scissors" and comp_choice2 == "rock":
        print("C1 wins!")
        c1_wins += 1
    else:
#elif comp_choice == "scissors" and comp_choice2 == "paper":
        print("C2 wins!")
        c2_wins += 1

    print(f"C1 choice: {comp_choice} \nC1 Wins: {c1_wins} \nC2 choice: {comp_choice2} \nC2 Wins: {c2_wins} \n")
    total_plays += 1

print(f"C1 wins: {c1_wins} \nC2 wins: {c2_wins} \nDraws: {draws} \nTotal plays: {total_plays}")
    
