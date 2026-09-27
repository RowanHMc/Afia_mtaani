from datetime import datetime, timedelta
from vaccination_schedule import VACCINATION_SCHEDULE

def check_vaccination_status(child):
    child_dob = datetime.strptime(
        child["date_of_birth"],
        "%d-%m-%Y"
    ).date()

    today = datetime.today().date()

    if "Vaccinations" not in child:
        child["Vaccinations"] = []

    result = []

    for scheduled_vaccine in VACCINATION_SCHEDULE:
        expected_date = child_dob + timedelta(
            weeks=scheduled_vaccine["age_weeks"]
        )   

        status = "upcoming" 

    for vaccination in child["Vaccinations"]:
        if(
            vaccination["vaccine"] == scheduled_vaccine["vaccine"]
            and vaccination["dose"] == scheduled_vaccine["dose"]
        ):
            status = "completed"
            break
    
            