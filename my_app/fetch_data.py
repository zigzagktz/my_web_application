from google.cloud import storage
import json
import os
import time
from pprint import pprint

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/siroh/Desktop/Entrada/python/learning/zkey/my_project.json"

storage_client = storage.Client()
bucket = storage_client.get_bucket("kshitiz_application")
obj = bucket.get_blob("recipe_training_dataset.json") 

dataset = json.loads(obj.download_as_text())

def data():
    time.sleep(5)
    return dataset
