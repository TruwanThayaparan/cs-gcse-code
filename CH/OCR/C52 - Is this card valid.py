# Challenge 52 - Is this card valid?

credit_card_number = input("Please enter a credit card number into the CC validator: ").strip()

check_digit = int(credit_card_number[-1])
new_ccn = credit_card_number[:-1]

new_ccn_reversed = new_ccn[::-1]

processed_digits = []
for idx, digit_char in enumerate(new_ccn_reversed):
    digit = int(digit_char)
    if idx % 2 == 0:
        digit *= 2
        if digit > 9:
            digit -= 9
    processed_digits.append(digit)

z = sum(processed_digits) + check_digit

if z % 10 == 0:
    print("Card number is valid!")
else:
    print("Card number is invalid.")
