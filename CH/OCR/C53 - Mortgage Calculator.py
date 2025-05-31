# Challenge 53 - Mortgage Calculator
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("You must enter a valid number.")

def get_compounding_interval():
    options = {
        "1": ("Monthly", 12),
        "2": ("Weekly", 52),
        "3": ("Daily", 365),
        "4": ("Continuous", None)
    }
    while True:
        print("\nSelect compounding interval:")
        for k, v in options.items():
            print(f"{k}: {v[0]}")
        choice = input("Enter your choice (1-4): ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice. Please try again.")
      
def workout_payment(P, apr, years, compounding):
    name, periods_per_year = compounding
    n = years * (periods_per_year if periods_per_year else 1)  
    
    if name == "Continuous":
        r = apr / 100
        from math import exp
        if r == 0:
            return P / n  
        payment = P * r / (1 - exp(-r * years))
        return payment

    r = (apr / 100) / periods_per_year
    
    if r == 0:
        return P / n
    
    payment = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return payment
  
principal = get_positive_float("Total mortgage amount (principal): ")
apr = get_positive_float("Annual interest rate (APR) as a percentage: ")
years = get_positive_float("Term of the loan (years): ")
compounding = get_compounding_interval()

id = workout_payment(principal, apr, years, compounding)
print(f"Your payment is: ${id:.2f}")

