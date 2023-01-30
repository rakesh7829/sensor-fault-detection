import pymongo
from sensor.constants.Database import DATABASE_NAME
import certifi
ca=certifi.where()


class MongoDBClient():
    client=None
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url="mongodb+srv://Rakesh:Rakesh123@cluster0.cjpuftt.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client=pymongo.MongoClient(mongodb_url,tlsCAFile=ca)
                self.client=MongoDBClient.client
                self.database=self.client[database_name]
                self.database_name=database_name
        except Exception as e:
            raise e





