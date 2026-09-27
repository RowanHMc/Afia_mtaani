from storage import load_childeren
from vaccination_status import check_vaccination_status

def get_vaccination_alerts():
    children = load_childeren()

    overdue = []

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

get_vaccination_alerts()