# Challenge 2 - Speed Tracker
from datetime import datetime
import re

def check_number_plate(plate):
    # Regex pattern:
    # ^ - start of string
    # [A-Za-z]{2} - exactly 2 letters
    # \d{2} - exactly 2 digits
    # [A-Za-z]{3} - exactly 3 letters
    # $ - end of string
    pattern = r'^[A-Za-z]{2}\d{2}[A-Za-z]{3}$'

    if re.match(pattern, plate):
        return True
    else:
        return False


number_plate = "AB12XYZ"

initial_time = "06:50:40"
final_time = "06:55:30"

time_format = "%H:%M:%S"
start = datetime.strptime(initial_time, time_format)
end = datetime.strptime(final_time, time_format)

time_diff_seconds = (end - start).total_seconds()
speed_mph = 1 / (time_diff_seconds / 3600)

print(f"Speed: {speed_mph:.2f} miles per hour")

valid_number_plate = check_number_plate(number_plate)
if valid_number_plate:
  print(f"{number_plate} is a valid number plate.")
else:
  print(f"{number_plate} is NOT a valid number plate.")
