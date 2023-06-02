import pymongo
import json

# Color codes for terminal output
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

this_db_username = "admin"
this_db_password = "1LGpnOal2IB6Omh2"
client = pymongo.MongoClient(f"mongodb+srv://{this_db_username}:{this_db_password}@python-mongo-project.pksitq7.mongodb.net/") # atlas db connection string
db = client["py-mongo"] # this is the database name
collection = db["containers"] # this is the collection name


def create_container():
    container = {}
    print(f"\nCreating container...") 
    while True:
        item = input("Enter the name of the item being stored, OR type 'q' to finish: ").lower()
        if item == "q":
            break
        quantity = input(f"Enter the quantity of {item}: ")
        container[item] = int(quantity)
    print("\nNew container created successfully!")
    container_id = collection.insert_one(container).inserted_id # inserted_id is the ObjectId of the newly created container
    container["_id"] = str(container_id) # convert the ObjectId to a string for serialization
    container.pop("_id", None)  # remove the _id field from the container dictionary for display purposes in the terminal
    print(f"Container ID: {GREEN}{container_id}{RESET}")
    print("Container Contents:")
    print(json.dumps(container, indent=4))


def read_container():
    containers = collection.find()
    if collection.count_documents({}) == 0:
        print("\nNo containers found.")
        return
    print("\nAll Containers:")
    for container in containers:
        container_id = container["_id"]
        container.pop("_id")  # Remove the _id key from the container_data dictionary
        print(f"\nContainer ID: {GREEN}{container_id}{RESET}")
        print("Container Contents:")
        print(json.dumps(container, indent=4)) # bson.json_util.dumps() is used to convert the ObjectId to a string for serialization


def update_container():
    pass

def delete_container():
    pass

def py_storage():
    options = {
        "1": create_container,
        "2": read_container,
        "3": update_container,
        "4": delete_container,
        "5": exit
    }
    while True:
        print(f"\n{BLUE}Welcome to Py-Mongo!{RESET}\n")
        print(f"1. {GREEN}Create{RESET} a container")
        print(f"2. {YELLOW}Read{RESET}   a container")
        print(f"3. {CYAN}Update{RESET} a container")
        print(f"4. {RED}Delete{RESET} a container")
        print(f"5. {PURPLE}Exit{RESET}")
        choice = input("\nEnter your choice: \n")
        if choice in options:
            options[choice]()
        else:
            print("\nInvalid choice. Please try again.")

py_storage()