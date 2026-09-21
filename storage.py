import json

DATA_FILE = "children.json"

def load_childeren():
    with open(DATA_FILE, "r") as file:
        children = json.load(file)
    return children 

def save_children(children):
    with open(DATA_FILE, "w") as file:
        json.dump(children, file, indent=4)


# test =  {
#     "child_id": "CH-0001",
#     "first_name": "Brian",
#     "last_name": "Kamau",
#     "date_of_birth": "2025-03-15",
#     "guardian_name": "Mary Kamau",
#     "location": "Kiamuri"
# }
# children = load_childeren()
# children.append(test)
# save_children(children)
# print("Saved Successfully")