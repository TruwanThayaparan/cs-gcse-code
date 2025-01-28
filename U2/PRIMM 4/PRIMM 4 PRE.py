# Before the actual task

import time # so it's more like an actual countdown

counting = int(input("Countdown start number:"))

while counting != 0: # while counting > 0:
        print(counting)
        time.sleep(1)
        counting = counting - 1
    
print("BEGIN!") # equivalent of 0 
