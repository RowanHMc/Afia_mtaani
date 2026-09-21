def register_child():
    print("\n===== REGISTER CHILD =====")

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    date_of_birth = input("Enter date of birth:DD-MM-YYYY: ")
    guardian_name = input("Enter guardian Name: ")
    guardian_contact = input("Enter Guardian phone number: ")
    location = input("Enter location: ")

    child = {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "guardian_name": guardian_name,
        "guardian_contact": guardian_contact,
        "location": location
    }

    return child