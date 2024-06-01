import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(event=None):
    """
    Fetches the weather information for the entered city and displays it in the GUI.

    Parameters:
    event (tkinter.Event): The event object, not used here but needed for key binding.

    Returns:
    None
    """
    city = city_entry.get()
    
    # Validation for numeric value
    if city.isnumeric():
        messagebox.showerror("Invalid Input", "Please enter a valid city name")
        return
    
    api_key = "082eed4598c4b7cc2f84a57bad6921d6" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    # Check for valid response
    if response.status_code != 200:
        messagebox.showerror("Error", "City not found or an issue occurred, please try again later")
        return
    
    weather = response.json()
    
    temperature = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]
    pressure = weather["main"]["pressure"]
    
    # Handle rain data
    if "rain" in weather:
        precipitation = weather["rain"].get("1h", 0)  # Get precipitation for the last hour if available
    else:
        precipitation = 0  # Default to 0 if no rain data is available
    
    temperature_label.config(text=f"Temperature: {temperature}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
    pressure_label.config(text=f"Pressure: {pressure} hPa")
    precipitation_label.config(text=f"Precipitation: {precipitation} %")

# Set up the main application window
root = tk.Tk()
root.title("Weather Forecast")

# Configure grid layout with minimum sizes
root.rowconfigure([0, 1, 2, 3, 4, 5], minsize=100)
root.columnconfigure([0, 2], minsize=100)
root.columnconfigure(1, minsize=800)

# Location label and entry
location_label = tk.Label(root, text="Location:")
location_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=5, sticky='we')
city_entry.bind('<Return>', get_weather)  # Bind Enter key to the get_weather function

# Search button
search_button = tk.Button(root, text="Search", command=get_weather)
search_button.grid(row=0, column=2, padx=10, pady=5, sticky='w')

# Weather information labels
temperature_label = tk.Label(root, text="Temperature: ")
temperature_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')

humidity_label = tk.Label(root, text="Humidity: ")
humidity_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='w')

wind_speed_label = tk.Label(root, text="Wind Speed: ")
wind_speed_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='w')

pressure_label = tk.Label(root, text="Pressure: ")
pressure_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='w')

precipitation_label = tk.Label(root, text="Precipitation: ")
precipitation_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky='w')

# Run the application
root.mainloop()
