# Challenge 6 - Max and min list

numbers = []
min_allowed = None
max_allowed = None

def set_bounds():
    global min_allowed, max_allowed
    while True:
        try:
            min_allowed = float(input("Enter minimum allowable value: "))
            max_allowed = float(input("Enter maximum allowable value: "))
            if min_allowed > max_allowed:
                print("Minimum cannot be greater than maximum. Try again.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers.")

def number_adder():
    while True:
        value = input("Enter a number (or 'STOP' to finish): ").strip()
        if value.lower() == 'stop':
            break
        try:
            num = float(value)
            if min_allowed is not None and max_allowed is not None:
                if num < min_allowed or num > max_allowed:
                    print(f"Number must be between {min_allowed} and {max_allowed}.")
                    continue
            numbers.append(num)
            print(f"Added {num}. Current max: {max(numbers)}, min: {min(numbers)}")
        except ValueError:
            print("Invalid number. Try again.")

def print_list():
    if not numbers:
        print("The list is empty.")
    else:
        print("Numbers in the list:", numbers)

def remove_number():
    if not numbers:
        print("The list is empty.")
        return
    try:
        index = int(input(f"Enter item number to remove (1-{len(numbers)}): "))
        removed = numbers.pop(index-1)
        print(f"Removed {removed} from the list.")
    except (ValueError, IndexError):
        print("Invalid index.")

def save_list():
    filename = input("Enter filename to save to: ").strip()
    with open(filename, "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")
    print(f"List saved to {filename}.")

def load_list():
    global numbers
    filename = input("Enter filename to load from: ").strip()
    try:
        with open(filename, "r") as f:
            loaded = []
            for line in f:
                try:
                    num = float(line.strip())
                    if min_allowed is not None and max_allowed is not None:
                        if min_allowed <= num <= max_allowed:
                            loaded.append(num)
                    else:
                        loaded.append(num)
                except ValueError:
                    continue
            numbers = loaded
        print(f"List loaded from {filename}.")
        if numbers:
            print(f"Current max: {max(numbers)}, min: {min(numbers)}")
        else:
            print("No numbers in list after applying bounds.")
    except FileNotFoundError:
        print("File not found.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Set allowable min/max values")
        print("2. Add numbers to the list")
        print("3. Print the list")
        print("4. Remove a number")
        print("5. Save list to file")
        print("6. Load list from file")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            set_bounds()
        elif choice == '2':
            number_adder()
        elif choice == '3':
            print_list()
        elif choice == '4':
            remove_number()
        elif choice == '5':
            save_list()
        elif choice == '6':
            load_list()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
menu()
