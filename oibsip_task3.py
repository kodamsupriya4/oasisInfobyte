import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit.
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        return temperature, humidity, weather_description
    else:
        print("Error fetching weather data. Please check your city name and API key.")
        return None, None, None

def main():
    api_key = "caf7e265780888c72c4fa967edae22cb"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    temperature, humidity, weather_description = get_weather(api_key, city)

    if temperature is not None:
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description}")

if __name__ == "__main__":
    main()
