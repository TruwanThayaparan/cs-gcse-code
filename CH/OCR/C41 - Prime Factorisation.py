# Challenge 41 - Prime Factorisation
def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break

    return factors

while True:
  try:
    fact = int(input("Enter a number into the Prime Factor Finder: ").strip())
  except ValueError:
    print("You must enter a number.")

  print(f"The prime factors of {fact} are:")
  print(prime_factors(fact))
  
  keep_going = input("Do you want to check another number? ").strip().lower()
  if keep_going in ('no', 'n'):
      print("Goodbye!")
      break
