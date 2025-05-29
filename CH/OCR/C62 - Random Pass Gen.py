# Challenge 62 - R@nd0m P@ssw0rd generator

import random
import string

passwords = []

def generate_password(length):
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!£$%^&*@")

    all_chars = string.ascii_letters + string.digits + "!£$%^&*@"
    others = random.choices(all_chars, k=length - 4)

    password_list = [lowercase, uppercase, digit, special] + others
    random.shuffle(password_list)

    return ''.join(password_list)

print("Welcome to the strong password generator.")

while True:
    length = 0
    while True:
        try:
            length = int(input("\nEnter a length for the password (minimum 8): "))
            if length < 8:
                print("Password length must be 8 characters or more.")
            else:
                break
        except ValueError:
            print("Password length must be a number.")

    passw = generate_password(length)
    print("Generated password is:", passw)
    passwords.append(passw)

    keep_going = input("Want to generate another password (yes/no)? ").strip()
    if keep_going.lower() in ["no", "n"]:
        break

with open("passwords.txt", "wt") as p:
    for pw in passwords:
        p.write(f"{pw}\n")
