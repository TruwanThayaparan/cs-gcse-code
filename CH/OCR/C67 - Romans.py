# Challenge 67 - What have the Romans ever done for us?
def to_roman(num):
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    result = ""
    for (value, numeral) in roman_map:
        while num >= value:
            result += numeral
            num -= value
    return result

while True:
    while True:
        try:
            roman = int(input("Enter a number into the Roman Numeral converter: ").strip())
            if 1 <= roman <= 3999:
                break
            print("You must enter a number between 1 and 3999.")
        except ValueError:
            print("You must enter a number.")

    print(to_roman(roman))

    keep_going = input("Do you want to convert another number? ").strip().lower()
    if keep_going in ("no", "n"):
        print("Goodbye!")
        break
