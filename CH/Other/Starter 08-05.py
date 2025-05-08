while True:
    try:
        secret_number = 42 # because 42 is everything
        attempted_num = int(input("Guess my secret number: "))
        if secret_number < attempted_num:
            print("Your guess is too MASSIVE... \n")
        elif secret_number > attempted_num:
            print("Your guess is too SMALL... \n")
        else:
            print("You guessed the secret number!")
            break
    except ValueError:
        print("You're supposed to enter a NUMBER. \n")
