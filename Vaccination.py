from storage import load_childeren, save_children
from vaccination_schedule import VACCINATION_SCHEDULE


def record_vaccination():
    # find child record
    print("\n===== RECORD VACCINATION =====")
    child_id = input("Enter child ID: ").strip()

    children = load_childeren()
    child = None

    for current_child in children:
        if current_child["child_id"] == child_id:
            child = current_child
            break

    if child is None:
        print("child not found")
        return

    print("\nChild found")
    print("Name:", child["first_name"], child["last_name"]) 
    print("Date of birth:", child["date_of_birth"])
    print("Child ID:", child["child_id"]) 

    # to show options on vaccines
    print("\nAvailable Vaccinations:")

    for index, vaccine in enumerate(VACCINATION_SCHEDULE, start=1):
        print(
            index,
            "-",
            vaccine["vaccine"],
            "Dose", vaccine["dose"]
        )

    # vaccine selection
    while True:
        try:
            selection = int(input("\nSelect vaccine:"))
            if 1 <= selection <= len(VACCINATION_SCHEDULE):
                break
            print("Invalid. Choose a number from the list")
        except ValueError:
            print("Please enter a Number.")
    # get the selected vaccine         
    selected_vaccine = VACCINATION_SCHEDULE[selection - 1]

    print("\nSelect Vaccination:")
    print("Vaacine:", selected_vaccine["vaccine"])
    print("Dose:", selected_vaccine["dose"])






record_vaccination()      