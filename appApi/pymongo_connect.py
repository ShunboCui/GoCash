from appApi.utils import app
def get_database():
    from pymongo import MongoClient
    import pymongo
    import certifi

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = app.config.get("MONGO")

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

    print(client.list_database_names())

    # Create the database for our example (we will use the same database throughout the tutorial
    # return client['sample_mflix'] 
    return client['test']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()