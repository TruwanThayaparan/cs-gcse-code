# Challenge 52 - Is this card valid?

credit_card_number = input("Please enter a credit card number into the CC validator: ").strip()

# credit_card_number = "79927398713"
check_digit = int(credit_card_number[-1])
new_ccn = credit_card_number[:-1]

# print(check_digit)
# print(new_ccn)
# print(list(new_ccn))

new_ccn_reversed = new_ccn[::-1]

processed_digits = []
x = 1
for i in new_ccn_reversed:
    i = int(i)
    if x % 2 == 1:
        i *= 2
        if i > 9:
            i -= 9
    processed_digits.append(i)
    x += 1

z = sum(processed_digits)
# print(z)

z += check_digit
if z % 10 == 0:
    print("Card number is valid!")
else:
    print("Card number is invalid.")
