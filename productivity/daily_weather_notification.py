import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        print(f"The current weather in {city} is {temp}°C with {weather}.")
    else:
        print("City not found!")

# Example usage
get_weather("New York")