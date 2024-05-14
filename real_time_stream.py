import requests
import json 
from json import dumps
from datetime import datetime
from time import sleep
import random
from multiprocessing import Process
from urllib import response
import boto3
import json
import sqlalchemy
from sqlalchemy import text
import requests
from datetime import datetime 
random.seed(100)
from db_utils import AWSDBConnector

new_connector = AWSDBConnector()

def run_infinite_post_data_loop():
    
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        
        engine = new_connector.create_db_connector()
        
        with engine.connect() as connection:
        
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            for row in pin_selected_row:
               pin_result = dict(row._mapping)

            # Define the payload for pin result
            payload_pin = json.dumps({
            "StreamName": "streaming-121d2a86d1ab-pin",
            "Data":{"index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"], "poster_name": pin_result["poster_name"],"follower_count": pin_result["follower_count"],"tag_list": pin_result["tag_list"], "is_image_or_video": pin_result["is_image_or_video"], "image_src": pin_result["image_src"], "downloaded": pin_result["downloaded"], "save_location": pin_result["save_location"], "category": pin_result["category"]},
            "PartitionKey": "desired-name" 
            })
            
            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            for row in user_selected_row:
                user_result = dict(row._mapping) 
            
            # Define the payload for user result
            formatted_date_one= user_result["date_joined"].isoformat()
            
            payload_user = json.dumps({
            "StreamName": "streaming-121d2a86d1ab-user",
            "Data":{"ind": user_result["ind"], "first_name": user_result["first_name"] , "last_name": user_result["last_name"], "age": user_result["age"], "date_joined": formatted_date_one },
            "PartitionKey": "desired-name" 
            })

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            # Define the payload for geo result
            formatted_date = geo_result["timestamp"].isoformat()
            
            payload_geo = json.dumps({
            "StreamName": "streaming-121d2a86d1ab-geo",
             "Data":{"ind": geo_result["ind"],"timestamp": formatted_date,"latitude": geo_result["latitude"], "longitude": geo_result["longitude"],"country":geo_result ["country"]},# Use the transformed data here
             "PartitionKey": "desired-name" 
             })
            
            
            # Define the Kinesis Data Stream URL
            invoke_url_geo = "https://e1322drlib.execute-api.us-east-1.amazonaws.com/S1/streams/streaming-121d2a86d1ab-geo/record"
            invoke_url_user = "https://e1322drlib.execute-api.us-east-1.amazonaws.com/S1/streams/streaming-121d2a86d1ab-user/record"
            invoke_url_pin = "https://e1322drlib.execute-api.us-east-1.amazonaws.com/S1/streams/streaming-121d2a86d1ab-pin/record"

            
            # Send the request for pin
            headers = {'Content-Type': 'application/json'}
            
            pin_response = requests.request("PUT", invoke_url_pin ,headers=headers, data= payload_pin)
            print(pin_response.status_code)

            # Send the request for geo
            geo_response = requests.request("PUT", invoke_url_geo ,headers=headers, data= payload_geo)
            print(geo_response.status_code)

            # Send the request for user
            user_response = requests.request("PUT", invoke_url_user ,headers=headers, data= payload_user)
            print(user_response.status_code)
            
#calling the function
run_infinite_post_data_loop()

