from id_generator import generate_id
from storage import load_childeren, save_children
from reg_validation import validate_name, validate_dob, validate_location, validate_phone

def register_child():
    print("\n===== REGISTER CHILD =====")
    first_name = validate_name("Enter First Name: ")
    last_name = validate_name("Enter Last Name: ")
    date_of_birth = validate_dob("Enter date of birth:DD-MM-YYYY: ")
    guardian_name = validate_name("Enter guardian Name: ")
    guardian_contact = validate_phone("Enter Guardian phone number: ")
    location = validate_location("Enter location: ")
    child_id = generate_id()

    child = {
        "child_id": child_id,
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "guardian_name": guardian_name,
        "guardian_contact": guardian_contact,
        "location": location
    }

    children = load_childeren() #load existing 
    children.append(child) # add new to existing
    save_children(children) # save list again    
    return child


if __name__ == "__main__":
    child =register_child()
    print("\nRegistered child: ")
    print(child)
