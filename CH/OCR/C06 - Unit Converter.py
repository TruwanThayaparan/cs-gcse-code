# Challenge 6 - Unit Converter

def temp():
  convert_from = None
  while convert_from not in ("fahrenheit", "celsius", "kelvin"):
    convert_from = input("What will you convert from (fahrenheit, celsius, kelvin)? ").strip().lower()

  convert_to = None
  while convert_to not in ("fahrenheit", "celsius", "kelvin"):
    convert_to = input("What will you convert to (fahrenheit, celsius, kelvin)? ").strip().lower()
    
    if convert_from == convert_to:
      print("Convert from must not equal convert to.")
      convert_to = None

  while True:
    try:
      value = float(input("Enter the value you will be converting: ").strip())
      break
    except ValueError:
      print("You must enter a number.")

  return convert_from, convert_to, value

def get_temp(cf, ct, v):
    if cf == "fahrenheit" and ct == "celsius":
        return (v - 32) * 5 / 9
    elif cf == "celsius" and ct == "fahrenheit":
        return (v * 9 / 5) + 32
    elif cf == "celsius" and ct == "kelvin":
        return v + 273.15
    elif cf == "kelvin" and ct == "celsius":
        return v - 273.15
    elif cf == "fahrenheit" and ct == "kelvin":
        return (v - 32) * 5 / 9 + 273.15
    elif cf == "kelvin" and ct == "fahrenheit":
        return (v - 273.15) * 9 / 5 + 32
    else:
        return "fail"  # fallback

def currency():
  convert_from = None
  while convert_from not in ("usd", "eur", "gbp"):
    convert_from = input("What will you convert from (USD, EUR, GBP)? ").strip().lower()

  convert_to = None
  while convert_to not in ("usd", "eur", "gbp"):
    convert_to = input("What will you convert to (USD, EUR, GBP)? ").strip().lower()
    
    if convert_from == convert_to:
      print("Convert from must not equal convert to.")
      convert_to = None

  while True:
    try:
      value = float(input("Enter the value you will be converting: ").strip())
      break
    except ValueError:
      print("You must enter a number.")

  return convert_from, convert_to, value

def get_currency(cf, ct, v):
    if cf == "usd" and ct == "eur":
        return (v * 0.93)
    elif cf == "usd" and ct == "gbp":
        return (v * 0.79)
    elif cf == "eur" and ct == "usd":
        return (v * 1.08)
    elif cf == "gbp" and ct == "usd":
        return (v * 1.26)
    elif cf == "eur" and ct == "gbp":
        return (v * 0.85)
    elif cf == "gbp" and ct == "eur":
        return (v * 1.18)
    else:
        return "fail"  # fallback
      
def volume():
  convert_from = None
  while convert_from not in ("litres", "gallons", "millilitres"):
    convert_from = input("What will you convert from (litres, gallons, millilitres)? ").strip().lower()

  convert_to = None
  while convert_to not in ("litres", "gallons", "millilitres"):
    convert_to = input("What will you convert to (litres, gallons, millilitres)? ").strip().lower()
    
    if convert_from == convert_to:
      print("Convert from must not equal convert to.")
      convert_to = None

  while True:
    try:
      value = float(input("Enter the value you will be converting: ").strip())
      break
    except ValueError:
      print("You must enter a number.")

  return convert_from, convert_to, value
  
def get_volume(cf, ct, v):
    if cf == "litres" and ct == "gallons":
        return v * 0.264172
    elif cf == "gallons" and ct == "litres":
        return v * 3.78541
    elif cf == "litres" and ct == "millilitres":
        return v * 1000
    elif cf == "millilitres" and ct == "litres":
        return v * 0.001
    elif cf == "gallons" and ct == "millilitres":
        return v * 3785.41
    elif cf == "millilitres" and ct == "gallons":
        return v * 0.000264172
    else:
        return "fail"  # fallback

print("Welcome to the UNIT CONVERTER!")
while True:
  response = None
  while response not in ("temp", "currency", "volume"):
    response = input("\nWhat do you want to convert with (temp/currency/volume)? ").strip().lower()

  if response == "temp":
    cf, ct, v = temp()
    converted = get_temp(cf, ct, v)
  elif response == "currency":
    cf, ct, v = currency()
    converted = get_currency(cf, ct, v)
  else:
    cf, ct, v = volume()
    converted = get_volume(cf, ct, v)

  if converted == "fail":
    print("An issue occurred whilst converting.")
  else:
    print(f"{v} {cf.upper()} converted to {ct.upper()} is {round(converted, 4)} {ct.upper()}.")

  keep_going = input("Want to convert again? (yes/no): ").strip().lower()
  if keep_going == "no": 
    break

