import pymongo # pymongo is a python library that allows us to connect to MongoDB
import uuid # uuid is a python library that allows us to generate unique IDs; i will use this to name the containers in the database

# going to use something like this data structure for the database:
container_id = uuid.uuid4().hex # generate a unique ID for the container, there will be multiple containers in the database and the container should be identified uniquely
database_structure = {
    container_id:
        {
            "item1": "value",
            "item2": "value",
            "item3": "value",
            "item4": "value"
        }
}

this_db_username = "admin" # this is the username for the database
this_db_password = "1LGpnOal2IB6Omh2" # this is the password for the database
client = pymongo.MongoClient(f"mongodb+srv://{this_db_username}:{this_db_password}@python-mongo-project.pksitq7.mongodb.net/") # this is the connection
db_name = client["py-mongo"] # this is the name of the database
collection_name = db_name["containers"] # this is the name of the collection (table) in the database

