# Challenge 58 - Text based game
def start_game():
    name = input("Welcome, adventurer! What is your name? ")
    print(f"\nGreetings, {name}. Your quest begins now...\n")
    room_start(name)

def room_start(name):
    print("\nYou stand at a crossroads in a mystical land.")
    print("To your left is a dark forest. To your right, a towering castle.")
    choice = input("Do you go to the forest or the castle? ").strip().lower()

    if choice == "forest":
        room_forest(name)
    elif choice == "castle":
        room_castle(name)
    else:
        print("That's not a valid choice. You must enter 'forest' or 'castle'.")
        room_start(name)

def room_forest(name):
    print(f"\n{name}, you enter the forest. The trees whisper ancient secrets.")
    print("Ahead, you see a glowing cave and a giant tree with a ladder.")
    choice = input("Do you enter the cave or climb the tree? ").strip().lower()

    if choice == "cave":
        room_cave(name)
    elif choice == "tree":
        print(f"\n{name}, you climb the tree and find a hidden treehouse filled with treasure.")
        print("You win! 🏆")
    else:
        print("That's not a valid choice. You must enter 'cave' or 'tree'.")
        room_forest(name)

def room_cave(name):
    print(f"\n{name}, you step into the glowing cave.")
    print("A sleeping dragon lies curled around a pile of gold.")
    choice = input("Do you sneak past the dragon or run back? ").strip().lower()

    if choice == "sneak":
        print(f"\n{name}, the dragon wakes up and roasts you like a marshmallow. Game over!")
    elif choice == "run":
        print(f"\nYou escape back to the forest, heart pounding.")
        room_forest(name)
    else:
        print("That's not a valid choice. You must enter 'sneak' or 'run'.")
        room_cave(name)

def room_castle(name):
    print(f"\n{name}, you approach the ancient castle gates.")
    print("Two guards block your path.")
    choice = input("Do you try to fight them or sneak through a side entrance? ").strip().lower()

    if choice == "fight":
        print(f"\n{name}, you bravely fight but are quickly overwhelmed. Game over!")
    elif choice == "sneak":
        print(f"\n{name}, you slip in through a secret tunnel and find the throne room.")
        print("The crown lies unguarded. You are now the ruler of the realm!")
        print("You win!")
    else:
        print("That's not a valid choice. You must enter 'fight' or 'sneak'.")
        room_castle(name)

start_game()
