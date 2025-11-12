# Challenge 3 - Email Validator (Stricter Version)

def check_email(email):
    email = email.strip()
    errors = []

    # Spaces
    if " " in email:
        errors.append("Email cannot contain spaces.")

    # Check for @ sign
    if "@" not in email:
        errors.append("Email must contain exactly one '@' symbol.")
    else:
        if email.count("@") > 1:
            errors.append("Email cannot contain more than one '@' symbol.")

        local_part, domain_part = email.split("@", 1)

        # Local/domain blank check
        if not local_part:
            errors.append("The part before '@' (local part) cannot be blank.")
        if not domain_part:
            errors.append("The part after '@' (domain part) cannot be blank.")

        # Consecutive dots
        if ".." in local_part or ".." in domain_part:
            errors.append("Email cannot have consecutive dots ('..') in local or domain part.")

        # Leading/trailing dots
        if local_part.startswith(".") or local_part.endswith("."):
            errors.append("Local part cannot start or end with a dot ('.').")
        if domain_part.startswith(".") or domain_part.endswith("."):
            errors.append("Domain part cannot start or end with a dot ('.').")

        # Dot immediately after @
        if domain_part.startswith("."):
            errors.append("Domain part cannot start with a dot ('.') immediately after '@'.")

        # Dot at the very end of domain
        if domain_part.endswith("."):
            errors.append("Domain part cannot end with a dot ('.').")

        # Ensure at least one dot in domain
        if "." not in domain_part:
            errors.append("Domain part must contain at least one dot ('.') to separate domain levels (e.g., 'example.com').")

    return None if not errors else errors


# Function to check a single email and print results
def run_through_list(email):
    errors = check_email(email)
    email = email.strip()
    if errors is None:
        print(f"{email} → Valid email.")
    else:
        print(f"{email} → FAIL! Errors:")
        for err in errors:
            print("  -", err)


# Main program

# Single email input
email_input = input("Enter an email: ")
run_through_list(email_input)

print("\nChecking emails from file...\n")
# Check emails from file
try:
    with open('emails.txt', 'r') as text_file:
        for line in text_file:
            run_through_list(line.strip())
except FileNotFoundError:
    print("Error: 'emails.txt' not found. Make sure the file exists in the same folder.")
