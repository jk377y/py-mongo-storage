import pymongo
import uuid
import json

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
    print(f"\nCreating container with ID: {container_id}\n") # print the container id to the console has been created
    
    while True:
        item = input("Enter the name of the item being stored, OR type 'q' to finish: ").lower() # ask for the value of items being stored in the container, or type 'q' to finish
        if item == "q":
            break

        quantity = input(f"Enter the quantity of {item}: ") # when an item is entered, ask for the quantity of that item
        container[container_id][item] = int(quantity) # add the item and quantity to the container dictionary with the quantity as an integer type

    print("\nNew container created successfully!\n")
    print(f"Container ID: {container_id}")
    print("Container contents:")
    print(json.dumps(container[container_id], indent=4))

    collection_name.insert_one(container) # standard mongo insert function to insert the container into the collection

create_container()