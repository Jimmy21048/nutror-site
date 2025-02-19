
import requests
from .nutrients import nutrientsList

APP_ID='b0a423b6'
API_KEY='c6559b12403f0d771dc4cdf16409dd67'

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

def nutApi(q):
    payload = {
        "query": q,
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        nut = data['foods'][0]['full_nutrients']
        
        # filtered_nutrients = [
        #     {**nutrientsList[item['attr_id']], 'value': item['value']}
        #     for item in nut
        #         if item['attr_id'] in nutrientsList and item['value'] > nutrientsList[item['attr_id']]['minValue']
        # ]
        return nut
    else:
        return print("Error")
    

