# Challenge 10 - Number Names
# note: there's a module called num2words which makes this 'redundant', but I think this makes more sense for the challenge

number_dict = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

def two_digit_to_words(n):
    if n in number_dict:
        return number_dict[n]
    else:
        tens = (n // 10) * 10
        ones = n % 10
        return number_dict[tens] + "-" + number_dict[ones]

def three_digit_to_words(n):
    if n < 100:
        return two_digit_to_words(n)
    hundreds = n // 100
    remainder = n % 100
    result = number_dict[hundreds] + " hundred"
    if remainder > 0:
        result += " and " + two_digit_to_words(remainder)
    return result

def number_to_words(n):
    if n == 1000000:
        return "one million"
    elif n >= 1000:
        thousands = n // 1000
        remainder = n % 1000
        result = ""
        if thousands < 100:
            result += two_digit_to_words(thousands)
        else:
            result += three_digit_to_words(thousands)
        result += " thousand"
        if remainder > 0:
            result += " "
            result += three_digit_to_words(remainder)
        return result
    else:
        return three_digit_to_words(n)

print("Welcome to the Number Name generator!")
while True:
    try:
        number = int(input("Enter a number (1 to 1,000,000): "))
        if 1 <= number <= 1000000:
            print(number_to_words(number))
        else:
            print("Number must be between 1 and 1,000,000.")
    except ValueError:
        print("You must enter a valid number.")
