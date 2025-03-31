ip_address = input()
split_it_up = ip_address.split(".")
validIP = True

if len(split_it_up) == 4:
    for i in range(len(split_it_up)):
        if not split_it_up[i].isdigit() or not 0 <= int(split_it_up[i]) <= 255:
            validIP = False
            break
else:
    validIP = False

if validIP:
    print("Valid IP address")
else:
    print("Invalid IP address")
