from datetime import datetime
from storage import load_childeren
from vaccination_status import check_vaccination_status

def get_vaccination_alerts():

    children = load_childeren()

    overdue = []
    upcoming =[]

    overdue_children = set()
    upcoming_children = set()

    print("\n===== VACCINATION ALERTS =====")
    print("Total children:", len(children))

    for child in children:
        status_results = check_vaccination_status(child)

        for result in status_results:
            if result["status"] == "Overdue":
                today = datetime.today().date()
                days_overdue = (
                    today - result["expected_date"]
                ).days
                overdue.append({
                    "child_id": child["child_id"],
                    "name": child["first_name"] + " " + child["last_name"],
                    "vaccine": result["vaccine"],
                    "dose": result["dose"],
                    "expected_date": result["expected_date"],
                    "days_overdue": days_overdue
                })
                overdue_children.add(child["child_id"]) 

            elif result["status"] == "Upcoming":
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

                    upcoming_children.add(child["child_id"])    

    upcoming.sort(key=lambda alert: alert["expected_date"])

    # Grouping the alerts
    grouped_overdue = {}
    grouped_upcoming ={}

    #overdue grouped
    for alert in overdue:
        child_id = alert["child_id"]
        if child_id not in grouped_overdue:
            grouped_overdue[child_id] = []

        grouped_overdue[child_id].append(alert)   

    # upcoming grouped
    for alert in upcoming:
        child_id = alert["child_id"]
        if child_id not in grouped_upcoming:
            grouped_upcoming[child_id] = []

        grouped_upcoming[child_id].append(alert)   

    

    print("\n===== OVERDUE VACCINATIONS =====")
    print("Total overdue vaccinations:", len(overdue))
    print("Children affected:", len(overdue_children))

    for child_id, alerts in grouped_overdue.items():
        print(
            child_id,
            "|",
            alerts[0]["name"]
        )
        for alert in alerts:
            print(
                "   -",
                alert["vaccine"],
                "Dose", alert["dose"],
                "| Expected:", alert["expected_date"],
                "| Overdue by:", alert["days_overdue"],
                "days"
            )


    print("\n===== UPCOMING VACCINATIONS =====")

    print("Total upcoming vaccinations:", len(upcoming))
    print("Children affected:", len(upcoming_children))

    for child_id, alerts in grouped_upcoming.items():
        print(
            child_id,
            "|",
            alerts[0]["name"],   
        )
        for alert in alerts:
            print(
                "   -",
                alert["vaccine"],
                "Dose", alert["dose"],
                "| Due:", alert["expected_date"],
                "| Due in:", alert["days_til_due"],
                "days"
            )
            

    

                      

get_vaccination_alerts()