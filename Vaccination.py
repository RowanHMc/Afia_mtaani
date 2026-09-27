from datetime import datetime
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
    
    
    # date of administration
    while True:
        date_administered = input("\nEnter date vaccine was given(DD-MM-YYYY):").strip()
        if date_administered == "":
            print("Date cannot be empty")
            continue
        try:
            administered_date = datetime.strptime(
                date_administered,
                "%d-%m-%Y"
            ).date()

            child_dob = datetime.strptime(
                child["date_of_birth"],
                "%d-%m-%Y"
            ).date()

            today = datetime.today().date()

            if administered_date > today:
                print("Future dates invalid")
                continue
            if administered_date < child_dob:
                print("Vaccination cannot be before child's date of birth")
            break
        except ValueError:
            print("Please enter a valid date. DD-MM-YYYY")

    print("\nVaccination details:")
    print("Vaccine:", selected_vaccine["vaccine"])
    print("Dose:", selected_vaccine["dose"])
    print("Date Administered:", date_administered)


        # add vaccination to child record
    if "Vaccinations" not in child:
        child["Vaccinations"] = []

    # to check if vaccine is already recorded to avoin duplications
    for existing_vaccination in child["Vaccinations"]:
        if(
            existing_vaccination["vaccine"] == selected_vaccine["vaccine"]
            and existing_vaccination["dose"] == selected_vaccine["dose"]
        ):
            print("\nThis vaccine has already been administered")
            return


    vaccination = {
        "vaccine": selected_vaccine["vaccine"],
        "dose": selected_vaccine["dose"],
        "date_administered": date_administered
        } 
    child["Vaccinations"].append(vaccination)

    save_children(children)

    print("\nVaccination recorded successfully.")    


if __name__ == "__main__":
    record_vaccination()      