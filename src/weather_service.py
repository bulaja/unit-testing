import requests

def get_weather(city):
    url = f"https://api.example.com/weather?city={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def generate_weather_report(city):
    weather_data = get_weather(city)
    if weather_data:
        temperature = weather_data.get("temperature")
        condition = weather_data.get("condition")
        return f"The weather in {city} is {condition} with a temperature of {temperature}°C."
    else:
        return f"Could not fetch weather data for {city}."