import pymongo # pymongo is a python library that allows us to connect to MongoDB
import uuid # uuid is a python library that allows us to generate unique IDs; i will use this to name the containers in the database



#! from docs
# connect to the database
client = pymongo.MongoClient("<mongodb_connection_string>") # need to replace <mongodb_connection_string> with the connection string for MongoDB database

db_name = client["<database_name>"] # need to replace <database_name> with the name of the database

# create a collection
collection_name = db_name["<collection_name>"] # need to replace <collection_name> with the name of the collection