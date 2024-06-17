
import requests


def kelvin_to_celcius(kelvin):
  return kelvin - 273.15

def get_weather(city):
  api_key = "ef8842e274771f9052419ec6c963dcc0"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = f"{base_url}q={city}&appid={api_key}"
  response = requests.get(complete_url)
  data = response.json()

  if data["cod"] != "404":
    main = data["main"]
    temperature = main["temp"]
    temperature_celcius = kelvin_to_celcius(temperature)
    humidity = main["humidity"]
    weather_desc = data["weather"][0]=["description"]
    return temperature_celcius, humidity, weather_desc

  else:
    return "City not found!"

city = input("enter the City name: ")
temperature_celcius, humidity, weather_desc = get_weather(city)

print(f"Weather in {city}: ")
print(f"Temperature: {temperature_celcius} celcius")
print(f"Humidity: {humidity}%")
print(f"Description: {weather_desc}")
      
