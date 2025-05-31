# Challenge 22 - Simple Life Calculator

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("You must enter a number.")

def vat_calculator():
    print("VAT Calculator:")
    print("1. Calculate price after VAT")
    print("2. Calculate original price before VAT")
    print("3. Calculate VAT rate from prices")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        while True:
            try:
                original = float(input("Enter original price: "))
                break
            except ValueError:
                print("You must enter a number.")

        while True:
            try:
                rate = float(input("Enter VAT rate (in %): "))
                break
            except ValueError:
                print("You must enter a number.")
                
        price_after = original * (1 + rate / 100)
        rpa = round(price_after, 2)
        print("Price after VAT:", rpa)

    elif choice == "2":
        while True:
            try:
                price_after = float(input("Enter price after VAT: "))
                break
            except ValueError:
                print("You must enter a number.")

        while True:
            try:
                rate = float(input("Enter VAT rate (in %): "))
                break
            except ValueError:
                print("You must enter a number.")
                
        original = price_after / (1 + rate / 100)
        ro = round(original, 2)
        print("Original price before VAT:", ro)

    elif choice == "3":
        while True:
            try:
                original = float(input("Enter original price: "))
                break
            except ValueError:
                print("You must enter a number.")

        while True:
            try:
                price_after = float(input("Enter price after VAT: "))
                break
            except ValueError:
                print("You must enter a number.")

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
        while True:
            try:
                income = float(input("Enter original income: "))
                break
            except ValueError:
                print("You must enter a number.")

        while True:
            try:
                tax_rate = float(input("Enter tax rate (in %): "))
                break
            except ValueError:
                print("You must enter a number.")

        tax_amount = income * tax_rate / 100
        rta = round(tax_amount, 2)
        net_income = income - tax_amount
        rni = round(net_income, 2)
        print("Tax amount:",rta)
        print("Net income after tax:",rni)

    elif choice == "2":
        while True:
            try:
                original_income = float(input("Enter original income: "))
                break
            except ValueError:
                print("You must enter a number.")

        while True:
            try:
                after_tax_income = float(input("Enter after-tax income: "))
                break
            except ValueError:
                print("You must enter a number.")
                
        tax_rate = ((original_income - after_tax_income) / original_income) * 100
        rtr = round(tax_rate, 2)
        print("Tax rate:",rtr,"%")

    else:
        print("Invalid choice")

def times_table():
    print("Times Table Calculator:")
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("You must enter a number.")
            
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
        choice = input("Enter choice (1-4): ").strip().lower()

        if choice in ["1", "vat"]:
            vat_calculator()
        elif choice in ["2", "tax"]:
            tax_calculator()
        elif choice in ["3", "times", "table"]:
            times_table()
        elif choice in ["4", "exit", "quit", "stop"]:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main()
