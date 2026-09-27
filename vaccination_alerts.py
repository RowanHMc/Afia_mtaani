from storage import load_childeren
from vaccination_status import check_vaccination_status

def get_vaccination_alerts():
    children = load_childeren()

    print("\n===== VACCINATION ALERTS =====")
    print("Total children:", len(children))

    for child in children:
        status_results = check_vaccination_status(child)

        print(
            child["child_id"],
            "|",
            child["first_name"],
            child["last_name"]
        )