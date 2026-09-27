from datetime import datetime
from storage import load_childeren
from vaccination_status import check_vaccination_status

def get_vaccination_alerts():
    children = load_childeren()

    overdue = []
    upcoming =[]

    print("\n===== VACCINATION ALERTS =====")
    print("Total children:", len(children))

    for child in children:
        status_results = check_vaccination_status(child)

        for result in status_results:
            if result["status"] == "Overdue":
                overdue.append({
                    "child_id": child["child_id"],
                    "name": child["first_name"] + " " + child["last_name"],
                    "vaccine": result["vaccine"],
                    "dose": result["dose"],
                    "expected_date": result["expected_date"]
                })

            elif result["status"] == "upcoming":
                today = datetime.today().date()

                days_till_due = (result["expected_date"] - today).days
                if days_till_due <= 7:
                    upcoming.append({
                        "child_id": child["child_id"],
                        "name": child["first_name"] + " " + child["last_name"],
                        "vaccine": result["vaccine"],
                        "dose": result["dose"],
                        "expected_date": result["expected_date"],
                        "days_til_due": days_till_due
                    })    

    print("\n===== OVERDUE VACCINATIONS =====")
    print("Total overdue vaccinations:", len(overdue))

    for alert in overdue:
        print(
            alert["child_id"],
            "|",
            alert["name"],
            "|",
            alert["vaccine"],
            "Dose", alert["dose"],
            "| Expected:", alert["expected_date"]
        )

    print("\n===== UPCOMING VACCINATIONS =====")

    print("Total upcoming vaccinations:", len(upcoming))

    for alert in upcoming:
        print(
            alert["child_id"],
            "|",
            alert["name"],
            "|",
            alert["vaccine"],
            "Dose", alert["dose"],
            "| Due:", alert["expected_date"],
            "| Due in:", alert["days_til_due"], "days"
        )               

get_vaccination_alerts()