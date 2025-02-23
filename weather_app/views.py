import datetime
import requests
import os 
from django.shortcuts import render

def index(request):
  
  filePath = os.getcwd() + "/Weather/API_KEY"
  API_KEY = open (filePath, "r").read() 
  current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
  forcast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
  
  
  if request.method == "POST" :
    city1 = request.POST["city1"]
    
    weather_data, daily_forecasts = fetch_weather_and_forecast(city1, current_weather_url, forcast_url, API_KEY)

    
    context = {
      "weather_data1" : weather_data,
      "daily_forecasts1" : daily_forecasts,
    }
    
    return render(request ,"index.html", context)
  else :
    return render(request ,"index.html")
  

def fetch_weather_and_forecast(city1, current_weather_url, forecast_url, api_key):
  response = requests.get(current_weather_url.format(city1, api_key)).json()
  response = requests.get(current_weather_url.format(city1, api_key)).json()    
  
  if "coord" not in response:
    raise ValueError(f"Error in current weather response: {response}")
    
  lat , lon = response['coord']['lat'], response['coord']['lon']
  forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
  
  weather_data = {
    "city" : city1,
    "temperature" : round(response['main']['temp'] - 273.15, 2),
    "description" : response['weather'][0]['description'],
    "icon" : response['weather'][0]['icon'], 
  }
  
  daily_forecasts = []
  if 'daily' in forecast_response : 
    for daily_data in forecast_response['daily'][:5]:
          daily_forecasts.append({
              'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
              'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
              'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
              'description': daily_data['weather'][0]['description'],
              'icon': daily_data['weather'][0]['icon'],
          })
  else :
    print("no daily key")
  return weather_data, daily_forecasts
    