# Challenge 22 - Simple Life Calculator

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("You must enter a number.")

def vat_calculator():
    print("\nVAT Calculator:")
    print("1. Calculate price after VAT")
    print("2. Calculate original price before VAT")
    print("3. Calculate VAT rate from prices")

    while True:
        choice = input("Choose an option (1-3): ").strip()
        if choice not in ("1", "2", "3"):
            print("Invalid choice chosen, try again.")
            continue
        break

    if choice == "1":
        original = get_float("Enter original price: ")
        rate = get_float("Enter VAT rate (in %): ")
        price_after = original * (1 + rate / 100)
        print("Price after VAT:", round(price_after, 2))

    elif choice == "2":
        price_after = get_float("Enter price after VAT: ")
        rate = get_float("Enter VAT rate (in %): ")
        original = price_after / (1 + rate / 100)
        print("Original price before VAT:", round(original, 2))

    else:
        original = get_float("Enter original price: ")
        price_after = get_float("Enter price after VAT: ")
        vat_rate = ((price_after - original) / original) * 100
        print("VAT rate:", round(vat_rate, 2), "%")

def tax_calculator():
    print("\nTax Calculator:")
    print("1. Calculate tax amount and net income (given income and tax rate)")
    print("2. Calculate tax rate (given original income and after-tax income)")
    
    while True:
        choice = input("Choose an option (1-2): ").strip()
        if choice not in ("1", "2"):
            print("Invalid choice chosen, try again.")
            continue
        break

    if choice == "1":
        income = get_float("Enter original income: ")
        tax_rate = get_float("Enter tax rate (in %): ")
        
        tax_amount = income * tax_rate / 100
        net_income = income - tax_amount
        
        print("Tax amount:", round(tax_amount, 2))
        print("Net income after tax:", round(net_income, 2))

    else:
        original_income = get_float("Enter original income: ")
        after_tax_income = get_float("Enter after-tax income: ")
        
        tax_rate = ((original_income - after_tax_income) / original_income) * 100
        print("Tax rate:", round(tax_rate, 2), "%")

def times_table():
    print("\nTimes Table Calculator:")
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
