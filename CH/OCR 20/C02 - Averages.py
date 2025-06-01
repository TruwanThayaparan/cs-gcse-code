# Challenge 2 - Averages

averages = []

# Input loop
while True:
    pro = input("Enter a number (enter 'stop' to stop): ")
    if pro.lower() == "stop":
        break
    try:
        pro = float(pro)
        averages.append(pro)
    except ValueError:
        print("You must enter a valid number.")

# Mean
if averages:
    mean = sum(averages) / len(averages)
    print(f"\nThe mean of the numbers you entered is {mean}.")
    
    # Median
    averages.sort()
    n = len(averages)
    if n % 2 == 1:
        median = averages[n // 2]
    else:
        mid1 = averages[n // 2 - 1]
        mid2 = averages[n // 2]
        median = (mid1 + mid2) / 2
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
else:
    print("No numbers were entered.")
