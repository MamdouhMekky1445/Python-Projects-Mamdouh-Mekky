import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "City name cannot be empty!")
        return
    
    api_key = "082eed4598c4b7cc2f84a57bad6921d6"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        if weather_data["cod"] != 200:
            messagebox.showerror("Error", weather_data["message"])
            return
        
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        
        result_text = (f"Weather in {city}:\n"
                       f"Temperature: {temp}°C\n"
                       f"Description: {description}\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} m/s")
        
        result_label.config(text=result_text)
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))

# Setting up the GUI
app = tk.Tk()
app.title("Weather Journal")
app.geometry("400x300")

# Configuring the grid
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=3)

tk.Label(app, text="Enter City:", font=("Helvetica", 14)).grid(column=0, row=0, padx=10, pady=10, sticky="e")

city_entry = tk.Entry(app, font=("Helvetica", 14))
city_entry.grid(column=1, row=0, padx=10, pady=10, sticky="w")

tk.Button(app, text="Get Weather", command=get_weather, font=("Helvetica", 14)).grid(column=0, row=1, columnspan=2, pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 14), justify="left")
result_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

app.mainloop()
