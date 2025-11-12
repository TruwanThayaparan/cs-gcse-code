# challenge 3 - email validator


def check_email(email):
    email = email.strip()
    errors = []

    # Spaces
    if " " in email:
        errors.append("Spaces cannot be in your email!")

    # check for @ sign
    if "@" not in email:
        errors.append("You must have an at sign (@) in your email.")
    else:
        # 
        if email.count("@") > 1:
            errors.append("You can only have one at sign (@) in your email.")

        local_part, domain_part = email.split("@", 1)
        if not local_part:
            errors.append("The part before the @ cannot be blank!")
        if not domain_part:
            errors.append("The part after the @ cannot be blank!")

        # Consecutive dots in local or domain
        if ".." in local_part or ".." in domain_part:
            errors.append("Multiple dots (.) cannot be next to each other.")

        # Leading or trailing dots
        if local_part.startswith(".") or local_part.endswith("."):
            errors.append("Local part cannot start or end with a dot (.)")
        if domain_part.startswith(".") or domain_part.endswith("."):
            errors.append("Domain part cannot start or end with a dot (.)")

        # Ensure at least one dot in domain
        if "." not in domain_part:
            errors.append("Domain part must contain a dot (.)")

    # return success/fail
    return None if not errors else errors

    
email = input("Enter an email: ")
errors = check_email(email)

if errors == None:
    print("Valid email.")
else:
    print("FAIL! Errors:")
    for i in errors:
        print(i)

def run_through_list(em):
    errors = check_email(em)

    if errors == None:
        print(em)
        print("Valid email.")
    else:
        print(em)
        print("FAIL! Errors:")
        for i in errors:
            print(i)


with open('emails.txt', 'r') as text_file:
    for line in text_file:
        run_through_list(line.strip())
