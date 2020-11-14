from pymongo import MongoClient 
class Connection:
     def __init__(self,dbName,collectionName):
        self.database=dbName
        self.collection=collectionName
    def getDB(self):
        return self.database
    
    def getColletion(self):
        return self.collection
    
    def connection(self):
        try: 
            conn = MongoClient() 
            print("Connected successfully!!!") 
        except:   
            print("Could not connect to MongoDB")
        db = conn.self.database 
        col= db.self.collection
        return col