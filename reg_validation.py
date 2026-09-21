import re

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