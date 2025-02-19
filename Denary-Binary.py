# Denary-Binary Converter Challenge 2

'''
Denary and binary are two interchangeable number systems. Binary is used to represent denary numbers in computers. 
Binary uses only 2 digits (0 and 1), so is also called base-2, whereas denary is base-10. 
You should create a program that lets a user provide a denary integer and receive the binary equivalent. 
The program should also provide the option to do the reverse process - converting a binary integer to its denary equivalent. 
As an extension, you could also allow onversion between other bases, like hexadecimal or octal. 
Your code should perform these without the use of any built-in conversion functions. 
'''

# Denary to binary
def db(denary):
  digit = 0
  binary = ""
  magnitude = 1

  while (magnitude * 2) <= denary:
    magnitude *= 2

  remainder = denary

  while magnitude >= 1:
    ang = int(remainder / magnitude)
    binary += str(ang)
    remainder = remainder % magnitude
    magnitude = magnitude / 2

  return binary

def bd(binary):
    exponent = 0
    denary = 0

    binary = str(binary)
  
    for i in range(len(binary)-1,-1,-1):
      placeValue = 2 ** exponent

      denary += placeValue * int(binary[i])
      exponent += 1

    return denary

# Main program
def ask(quit):
    option = ""
    while option not in ["1", "DB", "2", "BD", "3", "Q"]:
      print("Choose an option:")
      print("1/DB = Denary to Binary")
      print("2/BD = Binary to Denary")
      print("3/Q = Quit the program")

      option = input()

      if option == "1" or option.upper() == "DB":
          denarynum = ""
          while denarynum.isdigit() == False:
            denarynum = input("Enter a denary number: ")
          denarynum = int(denarynum)
          result = db(denarynum)
          print(str(denarynum) + " in binary is " + str(result) + ". \n")
        
      elif option == "2" or option.upper() == "BD":
          error_out = True
          binarynum = ""
          while error_out:
            binarynum = input("Enter a binary number: ")
            error_out = False
            
            if binarynum.isdigit() == False: 
              print("ERROR: Number must be all digits!")
              error_out = True
              
            for digit in binarynum:
                if digit != "0" and digit != "1":
                    print("ERROR: Number must only use digits '0' and '1'!")
                    error_out = True
                    break         
          binarynum = int(binarynum)
          result = bd(binarynum)
          print(str(binarynum) + " in denary is " + str(result) + ". \n")
        
      elif option == "3" or option.upper() == "Q":
          print("Program quit!")
          exit()
        
      else:
          print("ERROR: NOT A VALID OPTION.")
   
   
while True:
  ask(quit)
