from datetime import datetime, timedelta
from vaccination_schedule import VACCINATION_SCHEDULE

def calc_vaccination_dates(date_of_birth): 
    date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").date()

    expected_dates = []

    for vaccine in VACCINATION_SCHEDULE:
        expected_date = date_of_birth + timedelta(weeks=vaccine["age_weeks"]) # adding weeks to the birthdate time 
        # creates dict to store 
        expected_dates.append({
            "vaccine" : vaccine["vaccine"],
            "dose" : vaccine["dose"],
            "expected_date" : expected_date
        })

    return expected_dates  

results = calc_vaccination_dates("01-01-2026")
for vaccine in results:
    print(
        vaccine["vaccine"],
        "Dose", vaccine["dose"],
        "Expected:", vaccine["expected_date"]
    )