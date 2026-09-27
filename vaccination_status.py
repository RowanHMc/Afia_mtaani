from datetime import datetime, timedelta
from vaccination_schedule import VACCINATION_SCHEDULE
from storage import load_children

def check_vaccination_status(child):
    child_dob = datetime.strptime(
        child["date_of_birth"],
        "%d-%m-%Y"
    ).date()

    today = datetime.today().date()

    if "Vaccinations" not in child:
        child["Vaccinations"] = []

    results = []

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

        if status != "completed":
            if expected_date < today:
                status = "Overdue"

        results.append({
            "vaccine": scheduled_vaccine["vaccine"],
            "dose": scheduled_vaccine["dose"],
            "expected_date": expected_date,
            "status": status
        })
    return results  

from storage import load_children

# check status
# children = load_children()

# if children:
#     child = children[1]

#     results = check_vaccination_status(child)

#     print("\n===== VACCINATION STATUS =====")
#     print("Child:", child["first_name"], child["last_name"])
#     print()

#     for result in results:
#         print(
#             result["vaccine"],
#             "Dose", result["dose"],
#             "| Expected:", result["expected_date"],
#             "| Status:", result["status"]
#         )
# else:
#     print("No children registered.")