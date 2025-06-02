# Challenge 63 - I like Pi

# Chudnovsky
from decimal import Decimal, getcontext
from math import factorial

def chudnovsky_pi(terms):
    getcontext().prec += 2  # extra digits for intermediate steps
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    for i in range(1, terms):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    getcontext().prec -= 2
    return +pi  # unary plus applies the precision

getcontext().prec = 50  # digits of precision
terms = 10

print(chudnovsky_pi(terms))

'''
# WARNING: Nilakantha Series IS NOT PRECISE
from decimal import Decimal, getcontext

getcontext().prec = 35 # precision (higher than 30)

def calculate_pi(terms):
    pi = Decimal(3)
    sign = 1
    for k in range(1, terms + 1):
        numerator = Decimal(4)
        denominator = Decimal((2*k) * (2*k + 1) * (2*k + 2))
        term = numerator / denominator
        if sign:
            pi += term
        else:
            pi -= term
        sign = 1 - sign # flip
    return pi

terms = 20000 # increase for more decimals

pi = calculate_pi(terms)
print(f"Pi calculated to 30 decimal places:\n{pi:.30f}")
'''

'''
while True:
    try:
        diameter = float(input("Enter the diameter: "))
        if diameter <= 0:
            print("You must enter a positive number.")
            continue
        break
    except ValueError:
        print("You must enter a number.")

while True:
    try:
        circumference = float(input("Enter the circumference: "))
        if circumference <= 0:
            print("You must enter a positive number.")
            continue
        break
    except ValueError:
        print("You must enter a number.")

pi = circumference / diameter
print(pi)
'''
