import pandas as pd
from pymongo.mongo_client import MongoClient
import json
uri="mongodb+srv://bhavyateja6:bhavyateja@cluster0.llotm0e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"
df= pd.read_csv("D:\projects\proje1\notebooks\wafer_23012020_041211.csv")
json_record = list(json.loads(df.T.to_json()).values()) 
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record) 