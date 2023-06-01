import pymongo
import uuid
import json

BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
PURPLE = '\033[95m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[37m'
RESET = '\033[0m'

container_id = uuid.uuid4().hex # will use this to generate the container ids as the containers are created

database_structure = { # just visualizing the database structure; not used
    container_id:
        {
            "item1": "value",
            "item2": "value",
            "item3": "value",
            "item4": "value"
        }
}

this_db_username = "admin"
this_db_password = "1LGpnOal2IB6Omh2"
client = pymongo.MongoClient(f"mongodb+srv://{this_db_username}:{this_db_password}@python-mongo-project.pksitq7.mongodb.net/") # this is the atlas cloud cluster connection
db_name = client["py-mongo"] # this is the database name
collection_name = db_name["containers"] # this is the collection name

def create_container():
    container_id = uuid.uuid4().hex # generate a new container id when this function is called
    container = {container_id: {}} # create a new container with the generated id that has an empty dictionary as its value initially
    print(f"\nCreating container with ID: {GREEN}{container_id}{RESET}") # print the container id to the console has been created
    
    while True:
        item = input("Enter the name of the item being stored, OR type 'q' to finish: ").lower() # ask for the value of items being stored in the container, or type 'q' to finish
        if item == "q":
            break

        quantity = input(f"Enter the quantity of {item}: ") # when an item is entered, ask for the quantity of that item
        container[container_id][item] = int(quantity) # add the item and quantity to the container dictionary with the quantity as an integer type

    print("\nNew container created successfully!")
    print(f"{GREEN}{container_id}{RESET} contents:")
    print(json.dumps(container[container_id], indent=4))

    collection_name.insert_one(container) # standard mongo insert function to insert the container into the collection

def read_container():
    pass

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

        if choice in options: #trying to improve my DRY execution by using a dictionary to call the functions
            options[choice]()
        else:
            print("\nInvalid choice. Please try again.")

        # if choice == "1":
        #     create_container()
        # elif choice == "2":
        #     read_container()
        # elif choice == "3":
        #     update_container()
        # elif choice == "4":
        #     delete_container()
        # elif choice == "5":
        #     print("\nThank you for using Py-Mongo!")
        #     break
        # else:
        #     print("\nInvalid choice. Please try again.")



py_storage() # call the main function to run the program