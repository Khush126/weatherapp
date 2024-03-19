import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return None
    return response.json()

def main():
    api_key = 'b73ccdf70dc313701f870f0f028a4aee'
    city = input("Enter the name of a city: ")
    weather_data = get_weather(api_key, city)
    if weather_data is None:
        print("Error: Unable to retrieve weather data. Please check the city name and your API key.")
    else:
        print(f"Current weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()