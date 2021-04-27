from google.cloud import storage
import json
import os
import time
from pprint import pprint
import pickle
import sklearn
from my_app import *

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/siroh/Desktop/Entrada/python/learning/zkey/my_project.json"

storage_client = storage.Client()
bucket = storage_client.get_bucket("kshitiz_application")
obj1 = bucket.get_blob("recipe_training_dataset.json") 
obj2 = bucket.get_blob("cuisine_prediction.pkl") 
obj3 = bucket.get_blob("ingredients_list.pkl") 

dataset = json.loads(obj1.download_as_text())

with open('ml_model.pkl',"wb") as file2:
    storage_client.download_blob_to_file(obj2,file2)
file2.close()

with open('ingredients.pkl',"wb") as file2:
    storage_client.download_blob_to_file(obj3,file2)
file2.close()

file1 = open('ml_model.pkl', 'rb')
ml_model= pickle.load(file1)
file1.close()


file2 = open('ingredients.pkl', 'rb')
all_ingredients= pickle.load(file2)
file2.close()

def data():
    return dataset

@cache.memoize(20)
def ingredients():
    return all_ingredients

@cache.memoize(20)
def ml_model_function(lst):
    return ml_model.predict(['cooking oil green chilies grilled'])

#print(ml_model.predict(['cooking oil green chilies grilled']))