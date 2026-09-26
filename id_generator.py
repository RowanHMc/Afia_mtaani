import json

COUNTER_FILE = "id_counter.json"

def generate_id():
    with open(COUNTER_FILE, "r") as file:
        counter = json.load(file) #read file to get get last id

    counter["last_id"] += 1 #adds 1 to previous id to get new id

    with open(COUNTER_FILE, "w") as file:
        json.dump(counter,file, indent=4)

    return f"CH-{counter["last_id"]:04d}"          
        