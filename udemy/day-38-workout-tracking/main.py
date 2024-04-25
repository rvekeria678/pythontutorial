from config import APP_ID, API_KEY, NN_HOST, NN_NLE_EP, SHEETY_WORKOUT_EP, BEARER_TOKEN
from datetime import datetime
import requests

def get_exercise_data():
    parameters = {"query": input("Tell me which exercises you did: ")}
    header = {
        'x-app-id':APP_ID,
        'x-app-key':API_KEY
    }
    nle_endpoint = f"{NN_HOST}{NN_NLE_EP}"
    response = requests.post(url=nle_endpoint,json=parameters,headers=header)
    response.raise_for_status()
    return response.json()

def upload_to_google_sheets(data):
    headers = {
        "Authorization":f"Bearer {BEARER_TOKEN}"
    }
    for exercise in data:
        json_data = {
            "workout": {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().isoformat(),
                "exercise": exercise['name'],
                "duration": str(exercise['duration_min']),
                "calories": str(exercise['nf_calories'])
            }
        }

        response = requests.post(url=SHEETY_WORKOUT_EP, json=json_data, headers=headers)
        response.raise_for_status()


data = get_exercise_data()

if data['exercises']:
    upload_to_google_sheets(data['exercises'])

