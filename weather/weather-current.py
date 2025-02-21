import requests
import os
from datetime import datetime

class WeatherApp:
    """
    A class to fetch and display weather information based on zip code.
    Uses the OpenWeatherMap API to retrieve weather data.
    """
    
    def __init__(self, api_key):
        """
        Initialize WeatherApp with API key.
        
        Args:
            api_key (str): OpenWeatherMap API key
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, zip_code, country_code="us"):
        """
        Fetch weather data for a given zip code.
        
        Args:
            zip_code (str): The zip code to fetch weather for
            country_code (str): Two-letter country code (default: "us")
            
        Returns:
            dict: Formatted weather information
            
        Raises:
            requests.RequestException: If API request fails
            KeyError: If response format is unexpected
        """
        try:
            # Construct API URL with parameters
            params = {
                "zip": f"{zip_code},{country_code}",
                "appid": self.api_key,
                "units": "imperial"  # Use Fahrenheit for temperature
            }
            
            # Make API request
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Extract and format relevant weather information
            weather_info = {
                "location": data["name"],
                "temperature": f"{round(data['main']['temp'])}°F",
                "feels_like": f"{round(data['main']['feels_like'])}°F",
                "humidity": f"{data['main']['humidity']}%",
                "description": data["weather"][0]["description"].capitalize(),
                "wind_speed": f"{round(data['wind']['speed'])} mph",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return weather_info
            
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch weather data: {str(e)}")
        except KeyError as e:
            raise Exception(f"Invalid response format: {str(e)}")

def main():
    """
    Main function to run the weather application.
    Prompts user for zip code and displays weather information.
    """
    # You would need to replace this with your actual API key
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    
    if not API_KEY:
        print("Error: API key not found. Please set OPENWEATHER_API_KEY environment variable.")
        return
    
    # Initialize weather app
    weather_app = WeatherApp(API_KEY)
    
    while True:
        try:
            # Get zip code from user
            zip_code = input("\nEnter zip code (or 'q' to quit): ").strip()
            
            if zip_code.lower() == 'q':
                print("Goodbye!")
                break
            
            # Validate zip code format
            if not zip_code.isdigit() or len(zip_code) != 5:
                print("Invalid zip code. Please enter a 5-digit number.")
                continue
            
            # Get and display weather information
            weather_info = weather_app.get_weather(zip_code)
            
            print("\nCurrent Weather Conditions:")
            print(f"Location: {weather_info['location']}")
            print(f"Temperature: {weather_info['temperature']}")
            print(f"Feels Like: {weather_info['feels_like']}")
            print(f"Humidity: {weather_info['humidity']}")
            print(f"Conditions: {weather_info['description']}")
            print(f"Wind Speed: {weather_info['wind_speed']}")
            print(f"Last Updated: {weather_info['timestamp']}")
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
