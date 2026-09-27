from storage import load_childeren
from vaccination_status import check_vaccination_status

def get_vaccination_summary():
    children = load_childeren()

    print("\n===== VACCINATION SUMMARY =====")

    for child in children:
        status_results = check_vaccination_status(child)

        completed = 0
        upcoming = 0
        overdue = 0

        completed_vaccines = []

        for result in status_results:
            if result["status"] == "completed":
                completed += 1

                completed_vaccines.append({
                    "vaccine": result["vaccine"],
                    "dose": result["dose"]
                })

            elif result["status"] == "Upcoming":
                upcoming += 1
            elif result["status"] == "Overdue":
                overdue += 1

        total_scheduled = len(status_results)

        print("\nCompleted vaccinations:")

        for vaccination in completed_vaccines:
            print(
                "   -",
                vaccination["vaccine"],
                "Dose",
                vaccination["dose"]
            )

        print("\n" + child["child_id"], "|", child["first_name"], child["last_name"])
        print("Completed:", completed)
        print("Upcoming:", upcoming)
        print("Overdue:", overdue)
        print("Total scheduled:", total_scheduled)

get_vaccination_summary()


                

