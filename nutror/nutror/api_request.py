
import requests
from .nutrients import importantNutrients

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
        
        filtered_nutrients = [
            {**importantNutrients[item['attr_id']], 'value': item['value']}
            for item in nut
                if item['attr_id'] in importantNutrients and item['value'] > importantNutrients[item['attr_id']]['minValue']
        ]
        
        extra_nutrients = [
            {**importantNutrients[item['attr_id']], 'value': item['value']}
            for item in nut
                if item['attr_id'] in importantNutrients and item['value'] < importantNutrients[item['attr_id']]['minValue']
        ]
        nutrients_data = {
            'f_name' : data['foods'][0]['food_name'],
            'f_weight' : data['foods'][0]["serving_weight_grams"],
            'f_calories' : data['foods'][0]["nf_calories"],
            'f_fat' : data['foods'][0]["nf_total_fat"],
            'f_protein' : data['foods'][0]["nf_protein"],
            'f_carb' : data['foods'][0]["nf_total_carbohydrate"],
            'benefits' : filtered_nutrients,
            'extra' : extra_nutrients
        }
        
        return nutrients_data
    else:
        return print("Error")
    

