# Challenge 22 - Simple Life Calculator
# The wording was unclear so this may be wrong.

def vat_calculator():
    print("VAT Calculator:")
    print("1. Calculate price after VAT")
    print("2. Calculate original price before VAT")
    print("3. Calculate VAT rate from prices")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        original = float(input("Enter original price: "))
        rate = float(input("Enter VAT rate (in %): "))
        price_after = original * (1 + rate / 100)
        rpa = round(price_after, 2)
        print("Price after VAT:", rpa)

    elif choice == "2":
        price_after = float(input("Enter price after VAT: "))
        rate = float(input("Enter VAT rate (in %): "))
        original = price_after / (1 + rate / 100)
        ro = round(original, 2)
        print("Original price before VAT:", ro)

    elif choice == "3":
        original = float(input("Enter original price: "))
        price_after = float(input("Enter price after VAT: "))
        vat_rate = ((price_after - original) / original) * 100
        rvr = round(vat_rate, 2)
        print("VAT rate:",rvr,"%")

    else:
        print("Invalid choice")

def tax_calculator():
    print("Tax Calculator:")
    print("1. Calculate tax amount and net income (given income and tax rate)")
    print("2. Calculate tax rate (given original income and after-tax income)")
    choice = input("Choose an option (1-2): ")

    if choice == "1":
        income = float(input("Enter original income: "))
        tax_rate = float(input("Enter tax rate (in %): "))
        tax_amount = income * tax_rate / 100
        rta = round(tax_amount, 2)
        net_income = income - tax_amount
        rni = round(net_income, 2)
        print("Tax amount:",rta)
        print("Net income after tax:",rni)

    elif choice == "2":
        original_income = float(input("Enter original income: "))
        after_tax_income = float(input("Enter after-tax income: "))
        tax_rate = ((original_income - after_tax_income) / original_income) * 100
        rtr = round(tax_rate, 2)
        print("Tax rate:",rtr,"%")

    else:
        print("Invalid choice")

def times_table():
    print("Times Table Calculator:")
    num = int(input("Enter a number: "))
    for i in range(1, 13):
        ans = num * i
        print(num, "x", i, "=", ans)

def main():
    while True:
        print("\nChoose a calculator:")
        print("1. VAT Calculator")
        print("2. Tax Calculator")
        print("3. Times Table")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1" or choice == "VAT" or choice == "vat":
            vat_calculator()
        elif choice == "2" or choice == "TAX" or choice == "tax":
            tax_calculator()
        elif choice == "3":
            times_table()
        elif choice == "4" or choice == "Exit" or choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
