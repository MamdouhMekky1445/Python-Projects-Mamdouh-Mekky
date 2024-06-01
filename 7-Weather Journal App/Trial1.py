import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "082eed4598c4b7cc2f84a57bad6921d6"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    weather = response.json()
    print(response.status_code)
    print(weather)

    if weather.get("cod") != 200:
        weather_info.config(text="City not found")
        return

    temperature = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]
    pressure = weather["main"]["pressure"]
    precipitation = weather.get("rain", {}).get("1h", 0)

    weather_info.config(
        text=f"Temperature: {temperature}°C\n"
             f"Humidity: {humidity}%\n"
             f"Wind Speed: {wind_speed} km/h\n"
             f"Pressure: {pressure} hPa\n"
             f"Precipitation: {precipitation} mm"
    )

# Set up the main application window
root = tk.Tk()
root.title("Weather Forecast")

# Location label and entry
location_label = tk.Label(root, text="Location:")
location_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

# Search button
search_button = tk.Button(root, text="Search", command=get_weather)
search_button.pack()

# Weather information label
weather_info = tk.Label(root, text="")
weather_info.pack()

# Run the application
root.mainloop()
