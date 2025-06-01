# Challenge 40 - Base of Numbers 
def denary_to_hexadecimal(num):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    
    result = ""
    n = num
    while n > 0:
        remainder = n % 16
        result = digits[remainder] + result
        n = n // 16
    return result

def hexadecimal_to_denary(hex_str):
    digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    result = 0
    power = 0
    for char in reversed(hex_str):
        if char not in digits:
            raise ValueError(f"Invalid hex digit: {char}")
        value = digits.index(char)
        result += value * (16 ** power)
        power += 1
    return result

def menu():
    while True:
        print("\nDenary-Hexadecimal Converter:")
        print("Denary to hexadecimal: 1")
        print("Hexadecimal to denary: 2")
        print("Exit: 3")

        option = input("Enter your option: ").strip()
        if option not in ("1", "2", "3"):
            print("You must enter 1, 2, or 3.")
            continue

        if option == "3":
            print("Goodbye!")
            break

        if option == "1":
            while True:
                try:
                    old_number = int(input("Enter a denary number: "))
                    if old_number < 0:
                        print("Please enter a non-negative integer.")
                        continue
                    break
                except ValueError:
                    print("You must enter a valid integer.")
            new_number = denary_to_hexadecimal(old_number)
            print(f"Hexadecimal equivalent: {new_number}")

        elif option == "2":
            while True:
                old_number = input("Enter a hexadecimal number: ").strip()
                try:
                    new_number = hexadecimal_to_denary(old_number)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid hexadecimal number.")
            print(f"Denary equivalent: {new_number}")

menu()
