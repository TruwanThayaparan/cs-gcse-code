# Challenge 13 - Logic Gate
print("Welcome to the Logic Gate checker.")

def menu():
    while True:
        while True:
            logic_gate = input("\nEnter logic gate (OR/AND/XOR/NAND/NOR): ").upper()
            if logic_gate not in ("OR", "AND", "XOR", "NAND", "NOR"):
                print("Please enter a valid logic gate.")
                continue
            break

        while True:
            input1 = input("Enter first input (0 or 1): ")
            if input1 not in ("0", "1"):
                print("Please enter '0' or '1'.")
                continue
            break

        while True:
            input2 = input("Enter second input (0 or 1): ")
            if input2 not in ("0", "1"):
                print("Please enter '0' or '1'.")
                continue
            break

        result = check_lg(logic_gate, input1, input2)
        if result is not None:
            print(f"\nResult: {result}")
        else:
            print("\nAn error occurred. Please try again.")

        keep_going = input("Do you want to check another logic gate? (yes/no): ")
        if keep_going.strip().lower() in ("no", "n"):
            print("Script ended.")
            break

def check_lg(logic_gate, input1, input2):
    input1 = int(input1)
    input2 = int(input2)
    if logic_gate == "OR":
        return input1 | input2
    elif logic_gate == "AND":
        return input1 & input2
    elif logic_gate == "XOR":
        return input1 ^ input2
    elif logic_gate == "NAND":
        return int(not (input1 & input2))
    elif logic_gate == "NOR":
        return int(not (input1 | input2))
    else:
        return None

menu()
