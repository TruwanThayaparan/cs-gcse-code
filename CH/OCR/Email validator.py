# challenge 3 - email validator


def check_email(email):
    errors = []
    # Spaces
    if " " in email:
        errors.append("Spaces cannot be in your email!")

    # check for @ sign
    if "@" not in email:
        errors.append("You must have an at sign (@) in your email.")
    else:
          if email.count("@") > 1:
              errors.append("You can only have one at sign (@) in your email.")
  
          local_part, domain_part = email.split("@", 1)
          if not local_part:
              errors.append("The part before the @ cannot be blank!")
          if not domain_part:
              errors.append("The part after the @ cannot be blank!")
  
      # check for . sign
     if "@" in email and domain_part:
          if "." not in domain_part:
              errors.append("You must have a dot (.) in the domain part of your email.")
          else:
              for i in range(len(email) - 1):
                  if (email[i] == email[i+1]) and (email[i] == "."):
                      errors.append("Multiple dots (.) cannot be next to each other.")
                      break

    # return success/fail
    if not errors:
        return None
    else:
        return errors

    
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
