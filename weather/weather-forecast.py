import requests
from datetime import datetime
import os
from typing import Dict, Optional

class WeatherForecast:
    """
    A class to handle weather forecast requests using OpenWeatherMap API.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize WeatherForecast with OpenWeatherMap API key.
        
        Args:
            api_key (str): OpenWeatherMap API key
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, zip_code: str, country_code: str = "us") -> Optional[Dict]:
        """
        Get current weather data for a given zip code.
        
        Args:
            zip_code (str): The zip code to get weather for
            country_code (str): Two-letter country code (default: "us")
            
        Returns:
            dict: Weather data if successful, None if request fails
        """
        try:
            # Construct the API URL with parameters
            params = {
                "zip": f"{zip_code},{country_code}",
                "appid": self.api_key,
                "units": "imperial"  # Use Fahrenheit for temperature
            }
            
            # Make the API request
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise exception for bad status codes
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def format_weather_data(self, weather_data: Dict) -> str:
        """
        Format the weather data into a readable string.
        
        Args:
            weather_data (dict): Weather data from API
            
        Returns:
            str: Formatted weather information
        """
        if not weather_data:
            return "Unable to fetch weather data."
        
        # Extract relevant information
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        city = weather_data["name"]
        
        # Format the weather information
        forecast = f"""
Weather Forecast for {city}:
-------------------------
Temperature: {temp}°F
Feels like: {feels_like}°F
Humidity: {humidity}%
Conditions: {description.capitalize()}
Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
        return forecast

def main():
    """
    Main function to run the weather forecast program.
    """
    # You should replace this with your actual API key
    API_KEY = "YOUR_API_KEY_HERE"
    
    # Create WeatherForecast instance
    weather = WeatherForecast(API_KEY)
    
    while True:
        # Get zip code from user
        zip_code = input("\nEnter zip code (or 'q' to quit): ").strip()
        
        if zip_code.lower() == 'q':
            print("Goodbye!")
            break
        
        # Validate zip code format (basic check)
        if not zip_code.isdigit() or len(zip_code) != 5:
            print("Please enter a valid 5-digit zip code.")
            continue
        
        # Get and display weather forecast
        weather_data = weather.get_weather(zip_code)
        print(weather.format_weather_data(weather_data))

if __name__ == "__main__":
    main()