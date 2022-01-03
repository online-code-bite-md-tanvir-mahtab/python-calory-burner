import os
import requests
from datetime import datetime

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
AUTH_NAME = os.environ["name"]
AUTH_TOKEN = os.environ['pass']
message = input("Enter your workout:")
gender = input("Enter your gender :")

EXERCISE_ENDPOINT =  "https://trackapi.nutritionix.com/v2/natural/exercise"
shety_enpoint = 'https://api.sheety.co/e78e679bf4063c1cfa9e4f16869c45b0/workoutTracker/workouts'
head = {
    'x-app-id':API_ID,
    'x-app-key':API_KEY,
}
EXERCISE_PARAMS = {
    'query':message,
    'gender':gender,
    'weight_kg':75,
    'height_cm':160,
    'age':22,
}


# now i am going to request 
response = requests.post(url=EXERCISE_ENDPOINT,json=EXERCISE_PARAMS,headers=head)
data = response.json()['exercises']
for workouts in data:
    wordouts = {
        'workout':{
        'date':datetime.now().strftime("%d/%m/%Y"),
        'time':datetime.now().strftime("%H:%M:%S"),
        'exercise':workouts['name'].title(),
        'duration':workouts['duration_min'],
        'calories':workouts['nf_calories']
        }
    }
    post_request = requests.post(url=shety_enpoint,json=wordouts,auth=(
        AUTH_NAME,
        AUTH_TOKEN,
    ))
    print(post_request.text)