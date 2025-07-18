import requests as req
import json

API_KEY = "043c51d5d245a75d77720a6c99b19452"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = req.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"City not found: {city}"}
    except req.RequestException:
        return {"error": "Failed to connect to weather service."}
