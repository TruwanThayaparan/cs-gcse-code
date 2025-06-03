# Challenge 7 - Credit Card Validator

def validate_credit_card(cc_num: str) -> bool:
    cc_num = cc_num.strip()
    
    if not cc_num.isdigit() or len(cc_num) < 13 or len(cc_num) > 19:
        return False
    
    check_digit = int(cc_num[-1])
    digits_to_process = cc_num[:-1][::-1]
    
    total = 0
    for idx, ch in enumerate(digits_to_process):
        digit = int(ch)
        if idx % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    total += check_digit
    return total % 10 == 0


cc_input = input("Please enter a credit card number into the CC validator: ")

if validate_credit_card(cc_input):
    print("Card number is valid!")
else:
    print("Card number is invalid.")
