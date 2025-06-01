# Challenge 2 - Averages

def get_numbers():
    numbers = []
    while True:
        pro = input("Enter a number (enter 'stop' to stop): ")
        if pro.lower() == "stop":
            break
        try:
            pro = float(pro)
            numbers.append(pro)
        except ValueError:
            print("You must enter a valid number.")
    return numbers

def save_to_file(numbers, filename):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(f"{num}\n")
    print(f"List saved to '{filename}'.")

def load_from_file(filename):
    numbers = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    pass  # Skip invalid lines
        print(f"List loaded from '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return numbers

def calculate_and_display(averages):
    if not averages:
        print("No numbers to process.")
        return

    # Mean
    mean = sum(averages) / len(averages)
    print(f"\nThe mean of the numbers is {mean}.")

    # Median
    averages.sort()
    n = len(averages)
    if n % 2 == 1:
        median = averages[n // 2]
    else:
        median = (averages[n // 2 - 1] + averages[n // 2]) / 2
    print(f"The median is {median}.")

    # Mode
    frequency = {}
    for num in averages:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_freq]

    if len(modes) == 1:
        print(f"The mode is {modes[0]}.")
    else:
        print(f"The modes are: {modes}.")

averages = get_numbers()

while True:
    print("\nOptions:")
    print("1. Save numbers to a file")
    print("2. Load numbers from a file")
    print("3. Continue with calculations")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        filename = input("Enter filename to save to: ")
        save_to_file(averages, filename)
    elif choice == "2":
        filename = input("Enter filename to load from: ")
        averages = load_from_file(filename)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

calculate_and_display(averages)
