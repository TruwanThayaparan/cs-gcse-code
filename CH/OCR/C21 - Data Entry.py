# Challenge 21 - Data Entry
from texttable import Texttable

members = []

def register_member():
    print("\nYou've chosen to register a new member. Please enter their details below:")
    first_name = input("First Name: ").strip().title()
    last_name = input("Last Name: ").strip().title()
    climbing_centre = input("Climbing Centre: ").strip().title()
    return [first_name, last_name, climbing_centre]

def display_members():
    if not members:
        print("\nNo members registered yet.")
        return

    t = Texttable()
    t.header(["First Name", "Last Name", "Centre Name"])
    for member in members:
        t.add_row(member)
    print("\nMember List:")
    print(t.draw())

def search_member():
    if not members:
        print("\nNo members to search.")
        return
    
    search_last = input("Enter the last name of the member to search: ").strip().title()
    found = [member for member in members if member[1] == search_last]

    if found:
        t = Texttable()
        t.header(["First Name", "Last Name", "Centre Name"])
        for member in found:
            t.add_row(member)
        print("\nSearch Results:")
        print(t.draw())
    else:
        print(f"No members found with last name '{search_last}'.")

def menu():
    print("\n\tWelcome to the Rock Climbing Program")
    while True:
        print("\nPlease select from one of the following options:")
        print("1 - Register new members")
        print("2 - Search for a user's details")
        print("3 - View all members")
        print("4 - Exit")
        
        try:
            choice = int(input("Please select an option (1–4): "))
            if choice == 1:
                try:
                    num_of_members = int(input("Enter the number of new members: "))
                    for _ in range(num_of_members):
                        new_member = register_member()
                        members.append(new_member)
                    print("\nMembers registered successfully!")
                except ValueError:
                    print("You must enter a number.")
            elif choice == 2:
                search_member()
            elif choice == 3:
                display_members()
            elif choice == 4:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Please select 1–4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

menu()
