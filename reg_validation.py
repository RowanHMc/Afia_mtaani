import re
from datetime import datetime

# Name validation
def validate_name(prompt):
    while True:
        name = input(prompt).strip()

        if name == "":
            print ("name cannot be empty")
            continue
        if not re.fullmatch(r"[A-Za-z\s]+", name):
            print("Invalid Input, must be letters Only")
            continue

        return name 
    
# Date of Birth Validation
def validate_dob(prompt):
    while True:
        date = input(prompt).strip()

        if date == "":
            print("Date of Birth cannot be empty")
            continue
        try:
            dob = datetime.strptime(date, "%d-%m-%Y").date()
            if dob > datetime.today().date():
                print("Date of Birth cannot be in the future")
                continue
            return date
        except ValueError:
            print("Please enter a valid date in DD-MM-YYYY format")
