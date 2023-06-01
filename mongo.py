import pymongo
import uuid
import json

container_id = uuid.uuid4().hex
database_structure = {
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
client = pymongo.MongoClient(f"mongodb+srv://{this_db_username}:{this_db_password}@python-mongo-project.pksitq7.mongodb.net/")
db_name = client["py-mongo"]
collection_name = db_name["containers"]

def create_container():
    container_id = uuid.uuid4().hex
    container = {container_id: {}}
    print(f"\nCreating container with ID: {container_id}\n")
    
    while True:
        item = input("Enter the name of the item being stored, OR type 'q' to finish: ").lower()
        if item == "q":
            break

        quantity = input(f"Enter the quantity of {item}: ")
        container[container_id][item] = int(quantity)

    print("\nNew container created successfully!\n")
    print(f"Container ID: {container_id}")
    print("Container contents:")
    print(json.dumps(container[container_id], indent=4))

    collection_name.insert_one(container)

create_container()