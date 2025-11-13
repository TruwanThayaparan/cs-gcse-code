# C80 - Happy Hopper
def is_happy_hopper(seq):
    n = len(seq)
    if n == 1:
        return True
    differences = set(abs(seq[i+1] - seq[i]) for i in range(n-1))
    required = set(range(1, n))
    return differences == required

def main():
    print("Enter numbers one by one for a sequence.")
    print("Type 'NEW SEQUENCE' to check and start a new sequence.")
    print("Type 'QUIT' to exit the program.")
    
    sequence = []
    
    while True:
        user_input = input("Enter number (or command): ").strip()
        
        if user_input.upper() == "QUIT":
            print("Goodbye!")
            break
        
        elif user_input.upper() == "NEW SEQUENCE":
            if not sequence:
                print("No numbers entered for current sequence.")
            else:
                if is_happy_hopper(sequence):
                    print(f"Sequence {sequence} is a Happy Hopper!")
                else:
                    print(f"Sequence {sequence} is NOT a Happy Hopper.")
                sequence = []
                
        else:
            try:
                num = int(user_input)
                sequence.append(num)
            except ValueError:
                print("Invalid input. Please enter an integer, 'NEW SEQUENCE', or 'QUIT'.")

main()
