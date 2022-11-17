from pymongo import MongoClient
# conn = MongoClient()
import pymongo
import certifi
myclient = pymongo.MongoClient("mongodb+srv://gautamsinh:gau123123@cluster0.2c9i6px.mongodb.net/test",  tlsCAFile=certifi.where())

iisd_db = myclient["schooldb"]

conn = iisd_db["studenttb"] 
    # print(sample_e)
# except Exception as e:
#     print("Exception in Connecting the data",e)
    