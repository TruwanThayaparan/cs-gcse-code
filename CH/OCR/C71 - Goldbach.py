# Challenge 71 - Goldbach
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)
    return None

while True:
    try:
        n = int(input("Enter a positive even number greater than 2: "))
        if n <= 2:
            print(f"{n} is not greater than 2!")
            continue
        if n % 2 != 0:
            print(f"{n} is not an even number!")
            continue
        break
    except ValueError:
        print("Invalid input. You must enter a whole number.")

pair = goldbach(n)
if pair:
    print(f"{n} = {pair[0]} + {pair[1]}")
else:
    print("No valid prime pair found.")
