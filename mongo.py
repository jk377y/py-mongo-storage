import pymongo # this is the python driver for MongoDB
import json # this is used to print the container contents in a pretty format and manipulate the containers' dictionaries
import uuid # this is used to generate a unique ID for each container

# these ANSI values are used to colorize the output to the terminal
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

# I used MongoDB Atlas for this project, so I needed to create a database and collection in Atlas (lies... I used Compass and linked it to Atlas)
this_db_username = "admin"
this_db_password = "1LGpnOal2IB6Omh2"
client = pymongo.MongoClient(f"mongodb+srv://{this_db_username}:{this_db_password}@python-mongo-project.pksitq7.mongodb.net/") # atlas db connection string
db = client["py-mongo"] # this is the database name
collection = db["containers"] # this is the collection name


# this function starts by creating a blank dictionary to store the container contents
# the user is prompted to enter the name of the item to store, and the quantity of that item
# multiple items can be added until the user breaks the loop
# once the loop is broken, a new UUID is generated for the container ID, and the container is inserted into the database
# the _id key is removed from the container dictionary, and the contents are printed
def create_container():
    container = {}
    print(f"\nCreating container...")
    while True:
        item = input("Enter the name of the item being stored, OR type 'f' to finish: ").lower()
        if item == "f":
            break
        quantity = input(f"Enter the quantity of {item}: ")
        container[item] = int(quantity)
    print("\nNew container created successfully!")
    container_id = str(uuid.uuid4())  # Generate a new UUID for the container ID
    container["_id"] = container_id
    collection.insert_one(container)
    container.pop("_id", None)
    print(f"Container ID: {GREEN}{container_id}{RESET}")
    print("Container Contents:")
    print(json.dumps(container, indent=4))


# this function starts by doing a find all of the containers in the database, and if there are none, it prints a message and returns
# if there are containers, it creates a copy of the containers and poping the _id key from the copy, then it prints the copy so the user can see all of the containers
def read_container():
    containers = collection.find()
    if collection.count_documents({}) == 0:
        print("\nNo containers found.")
        return
    print(f"\n{YELLOW}All Containers:{RESET}")
    for container in containers:
        container_id = container["_id"]
        container.pop("_id")
        print(f"\nContainer ID: {GREEN}{container_id}{RESET}")
        print("Container Contents:")
        print(json.dumps(container, indent=4))


# this function starts by creatin a copy of the containers and poping the _id key from the copy, then it prints the copy so the user can see all of the containers
# input is requested to use the _id to find the container to update
# if the container is found, the user is prompted to enter the name of the item to update, and then the new quantity for that item
# the update_one method is used to update the container in the database, then the updated container is printed
def update_container():
    containers = collection.find()
    if collection.count_documents({}) == 0:
        print("\nNo containers found.")
        return
    print(f"\n{YELLOW}All Containers:{RESET}")
    container_list = []
    for container in containers:
        container_id = container["_id"]
        container_list.append(container)
        container_copy = container.copy()
        container_copy.pop("_id", None)
        print(f"\nContainer ID: {GREEN}{container_id}{RESET}")
        print("Container Contents:")
        print(json.dumps(container_copy, indent=4))
    container_id = input("\nEnter the ID of the container you wish to update: ")
    container_to_update = None
    for container in container_list:
        if container["_id"] == container_id:
            container_to_update = container
            break
    if container_to_update:
        print(f"\nUpdating container {GREEN}{container_id}{RESET}:")
        while True:
            item = input("Enter the name of the item to update, or press 'f' to finish: ").lower()
            if item == "f":
                break
            quantity = input(f"Enter the quantity for {item}: ")
            container_to_update[item] = int(quantity)
        collection.update_one({"_id": container_id}, {"$set": container_to_update})
        container_to_update.pop("_id", None)
        print(f"\nUpdated container {GREEN}{container_id}{RESET}:")
        print(json.dumps(container_to_update, indent=4))
    else:
        print(f"\nContainer {GREEN}{container_id}{RESET} not found.")


# this function starts by creatin a copy of the containers and poping the _id key from the copy, then it prints the copy so the user can see all of the containers
# input is requested to use the _id to find the container to delete
# if the container is found, the user is prompted to confirm the deletion
# if the user confirms, the delete_one method is used to delete the container from the database
def delete_container():
    containers = collection.find()
    if collection.count_documents({}) == 0:
        print("\nNo containers found.")
        return
    print(f"\n{YELLOW}All Containers:{RESET}")
    container_list = []
    for container in containers:
        container_id = container["_id"]
        container_list.append(container)
        container_copy = container.copy() #needed a copy to remove the _id key from the dictionary for display, but need to preserve the original for deletion
        container_copy.pop("_id", None)  # remove the _id key from the container_copy
        print(f"\nContainer ID: {GREEN}{container_id}{RESET}")
        print("Container Contents:")
        print(json.dumps(container_copy, indent=4))
    container_id = input("\nEnter the ID of the container you wish to delete: ")
    container_to_delete = None
    for container in container_list:
        if container["_id"] == container_id:
            container_to_delete = container
            break
    if container_to_delete:
        confirmation = input(f"\n{RED}Are you sure you want to delete container{RESET} {GREEN}{container_id}{RESET}? {YELLOW}(yes/no):{RESET} ")
        if confirmation.lower() == "yes":
            collection.delete_one({"_id": container_id})
            print(f"\nContainer {GREEN}{container_id}{RESET} has been {RED}deleted{RESET} successfully.")
        else:
            print(f"\nDeletion of container {GREEN}{container_id}{RESET} has been canceled.")
    else:
        print(f"\nContainer {GREEN}{container_id}{RESET} not found.")


# this function is the main function that is called when the program is run
# it prints the menu and prompts the user for input
# if the input is valid, the corresponding function is called
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
        print(f"2. {YELLOW}Read{RESET} all containers")
        print(f"3. {CYAN}Update{RESET} a container")
        print(f"4. {RED}Delete{RESET} a container")
        print(f"5. {PURPLE}Exit{RESET}")
        choice = input("\nEnter your choice: \n")
        if choice in options:
            options[choice]()
        else:
            print("\nInvalid choice. Please try again.")

py_storage()