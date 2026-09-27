import json

DATA_FILE = "children.json"

def load_children():
    with open(DATA_FILE, "r") as file:
        children = json.load(file)
    return children 

def save_children(children):
    with open(DATA_FILE, "w") as file:
        json.dump(children, file, indent=4)



# children = load_childeren()
# children.append(test)
# save_children(children)
# print("Saved Successfully")