# Challenge 5 - Basic Lists
names = []

def name_adder():
    while True:
        name = input("Enter a name. Enter 'STOP' to finish: ").strip()
        if name.lower() == 'stop':
            break
        names.append(name)

def print_list():
    if not names:
        print("The list is empty.")
        return
    order = input("Print in original order or reverse? (o/r): ").strip().lower()
    if order == 'r':
        print(names[::-1])
    else:
        print(names)

def choose_item():
    if not names:
        print("The list is empty.")
        return
    try:
        index = int(input(f"Enter item number (1-{len(names)}): "))
        print(names[index-1])
    except (ValueError, IndexError):
        print("Invalid index.")

def slice_list():
    if not names:
        print("The list is empty.")
        return
    try:
        start = int(input("Enter start index (1-based): ")) - 1
        end = int(input("Enter end index (1-based, inclusive): "))
        print(names[start:end])
    except (ValueError, IndexError):
        print("Invalid indices.")

def remove_item():
    if not names:
        print("The list is empty.")
        return
    try:
        index = int(input(f"Enter item number to remove (1-{len(names)}): "))
        removed = names.pop(index-1)
        print(f"Removed '{removed}' from the list.")
    except (ValueError, IndexError):
        print("Invalid index.")

def save_list():
    filename = input("Enter filename to save to: ").strip()
    with open(filename, "w") as f:
        for name in names:
            f.write(name + "\n")
    print(f"List saved to {filename}.")

def load_list():
    global names
    filename = input("Enter filename to load from: ").strip()
    try:
        with open(filename, "r") as f:
            names = [line.strip() for line in f.readlines()]
        print(f"List loaded from {filename}.")
    except FileNotFoundError:
        print("File not found.")

def clean_list():
    global names
    names = [name.lower() for name in names]
    print("All names converted to lowercase.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Add names to the list")
        print("2. Print the whole list")
        print("3. Choose an item to print")
        print("4. Slice the list")
        print("5. Remove items from the list")
        print("6. Save list to file")
        print("7. Load list from file")
        print("8. Clean list (make all lowercase)")
        print("9. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name_adder()
        elif choice == '2':
            print_list()
        elif choice == '3':
            choose_item()
        elif choice == '4':
            slice_list()
        elif choice == '5':
            remove_item()
        elif choice == '6':
            save_list()
        elif choice == '7':
            load_list()
        elif choice == '8':
            clean_list()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
menu()
