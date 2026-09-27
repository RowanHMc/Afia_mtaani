from storage import load_children


def search_child():
    children = load_children()

    child_id = input("Enter child ID: ").strip()

    for child in children:

        if child["child_id"] == child_id:

            print("\n===== CHILD FOUND =====")

            print("Child ID:", child["child_id"])
            print("Name:", child["first_name"], child["last_name"])
            print("Date of birth:", child["date_of_birth"])
            print("Guardian:", child["guardian_name"])
            print("Guardian contact:", child["guardian_contact"])
            print("Location:", child["location"])

            return child

    print("\nChild not found")
    return None


if __name__ == "__main__":
    search_child()