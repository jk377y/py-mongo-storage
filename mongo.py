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


#! from docs
# connect to the database
client = pymongo.MongoClient("<mongodb_connection_string>") # need to replace <mongodb_connection_string> with the connection string for MongoDB database

db_name = client["<database_name>"] # need to replace <database_name> with the name of the database

# create a collection
collection_name = db_name["<collection_name>"] # need to replace <collection_name> with the name of the collection