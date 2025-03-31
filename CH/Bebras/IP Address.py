# bebras is wrong again
ip_address = input()
split_it_up = ip_address.split(".")
validIP = True
print(split_it_up)
print(len(split_it_up))
if len(split_it_up) == 4:
    for i in range(len(split_it_up)):
        if not 0 <= int(split_it_up[i]) <= 255:
            validIP = False
            print("Invalid IP address"); break
else:
    validIP = False
    print("Invalid IP address")

if validIP:
    print("Valid IP address")
