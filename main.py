from registration import register_child
from search import search_child
from Vaccination import record_vaccination
from vaccination_summary import get_vaccination_summary
from vaccination_alerts import get_vaccination_alerts

MENU = """
===== CHILD VACCINATION TRACKER =====
1. Register a child
2. Search for a child
3. Record a vaccination
4. View vaccination summary (all children)
5. View vaccination alerts (overdue / upcoming)
6. Exit
"""

def main():
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()

        if choice == "1":
            register_child()
        elif choice == "2":
            search_child()
        elif choice == "3":
            record_vaccination()
        elif choice == "4":
            get_vaccination_summary()
        elif choice == "5":
            get_vaccination_alerts()
        elif choice == "6":
            print("\nGoogbye")
            break
        else:
            print("\nInvalid Option. Enter number from 1 to 6")

if __name__ == "__main__":
    main()
