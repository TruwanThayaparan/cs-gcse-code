# Challenge 4 - Password Reset
filename = "users.txt"

# Load users from file
users = {}
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        username, old_pw = line.split()
        users[username] = old_pw

def check_password(pw):
    errors = []
    score = 0

    # Basic validity checks
    if len(pw) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in pw):
        errors.append("Password must contain an upper-case letter.")
    if not any(char.islower() for char in pw):
        errors.append("Password must contain a lower-case letter.")

    # Strength scoring
    if len(pw) >= 12:
        score += 1
    if any(char in "!@#$%^&*()-_+=" for char in pw):
        score += 1

    # Convert score to string
    if score == 0:
        strength = "Weak"
    elif score == 1:
        strength = "Medium"
    else:
        strength = "Strong"

    return (None, strength) if not errors else (errors, None)

def reset_pw(username):
    # Password input loop
    while True:
        pw = input("Enter a password: ")
        errors, strength = check_password(pw)

        if errors is None:
            print(f"{pw} → Valid password.")
            print(f"Strength: {strength}")
            break
        else:
            print(f"{pw} → FAIL! Errors:")
            for err in errors:
                print("  -", err)

    # Confirm password
    while True:
        repw = input("Re-enter password: ")
        if repw != pw:
            print("Re-entered password does not match password previously entered.")
            continue
        break

    print("Password successfully set!")

    # Update user password in memory
    users[username] = pw
    # Save back to file
    with open(filename, "w") as file:
        for user, password in users.items():
            file.write(f"{user} {password}\n")

# Ask for username
username = input("Enter your username: ")

if username not in users:
    print("Username not found.")
else:
    # Ask for old password
    old_pw_input = input("Enter your old password: ")
    if old_pw_input != users[username]:
        print("Old password incorrect. Cannot reset password.")
    else:
        print("Old password verified! You can now set a new password.")
        reset_pw(username)
