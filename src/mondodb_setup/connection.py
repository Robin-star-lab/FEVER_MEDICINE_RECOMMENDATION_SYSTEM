
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pathlib import Path
from pymongo.errors import ConnectionFailure

# Assuming Exception.py is in the same directory or a properly configured path
from Exception import CustomException  # Make sure the path is correct
import sys
import pandas as pd
import os  # For path manipulation

database_name = "Fever_Medication"
collection_name = "Medication_Data"


uri = "mongodb+srv://alumarobin:ScJJ20VL3V9FoDEP@cluster0.nnizo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class MongoDBConnection:
    def __init__(self, uri=uri, database_name=None):
        self.uri = uri
        self.database_name = database_name
        self.client = None
        self.db = None  

    def connect(self):
        try:
            self.client = MongoClient(self.uri,server_api=ServerApi('1'))
            self.client.admin.command('ismaster')
            
            try:
                if self.database_name:
                  self.db = self.client[self.database_name]
                  return True
            except ConnectionFailure as e:
                
                print(f"Connection failed: {e}")
                return False
        except Exception as e: 
            print(f"An error occurred during connection: {e}")
            return False

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None  # Reset db when disconnecting
            print("Disconnected from MongoDB.")

    def get_database(self):
      if self.db:
        return self.db
      else:
        print("No database selected. Please specify a database name during initialization or connection.")
        return None





class DataManager:  
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.db = self.db_connection.get_database() # Get the database object

    def insert_data(self, collection_name, data):
        if self.db:
            collection = self.db[collection_name]
            try:
                result = collection.insert_many(data)
                return result.inserted_id
            except Exception as e:
                print(f"Error inserting data: {e}")
                return None
        return None

    def find_data(self, collection_name, query):
       if self.db:
           collection = self.db[collection_name]
           try:
               results = collection.find(query)
               return list(results) # Convert cursor to a list
           except Exception as e:
               print(f"Error finding data: {e}")
               return None
       return None


mongo_conn = MongoDBConnection(database_name=database_name) 

if mongo_conn.connect():
    data_manager = DataManager(mongo_conn) # Pass the connection to DataManager

    
    data = pd.read_csv(r'C:\Users\Robin Aluma\Desktop\fever_medicines\medication_data\enhanced_fever_medicine_recommendation.csv')
    new_data = data.to_dict('records')  
    inserted_id = data_manager.insert_data(new_data)
    if inserted_id:
      print(f"Inserted data with ID: {inserted_id}")

    
    found_users = data_manager.find_data()
    if found_users:
        for user in found_users:
            print(user)

    mongo_conn.disconnect() 
else:
    print("Failed to establish a connection.")