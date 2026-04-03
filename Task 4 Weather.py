from tkinter import *
from tkinter import ttk
import random

# Maharashtra cities
cities = ["Mumbai","Pune","Nagpur","Nashik","Aurangabad","Solapur","Kolhapur"]

# Fake weather data
weather_data = {
    "Mumbai": ("Sunny", 32, 70),
    "Pune": ("Cloudy", 28, 60),
    "Nagpur": ("Sunny", 35, 40),
    "Nashik": ("Rainy", 25, 80),
    "Aurangabad": ("Cloudy", 30, 55),
    "Solapur": ("Sunny", 34, 30),
    "Kolhapur": ("Rainy", 26, 85)
}

def get_weather():
    city = com.get()

    if city in weather_data:
        condition, temp, humidity = weather_data[city]
    else:
        condition = random.choice(["Sunny","Cloudy","Rainy"])
        temp = random.randint(25,35)
        humidity = random.randint(40,80)

    # Change background color based on weather
    if condition == "Sunny":
        bg_color = "#FFD54F"
    elif condition == "Cloudy":
        bg_color = "#B0BEC5"
    else:
        bg_color = "#90CAF9"

    card.config(bg=bg_color)

    result_label.config(
        text=f"City: {city}\n\nTemperature: {temp}°C\nCondition: {condition}\nHumidity: {humidity}%",
        bg=bg_color
    )

def on_key_release(event):
    value = event.widget.get()
    if value:
        matches = [c for c in cities if value.lower() in c.lower()]
        listbox_update(matches)
    else:
        listbox_update([])

def listbox_update(matches):
    listbox.delete(0, END)
    for m in matches:
        listbox.insert(END, m)

def on_select(event):
    com.set(listbox.get(ACTIVE))
    listbox_update([])

# GUI
win = Tk()
win.title("Smart Weather Simulator")
win.geometry("500x500")
win.config(bg="#E3F2FD")

Label(win, text="Weather App", font=("Helvetica", 24, "bold"), bg="#E3F2FD").pack(pady=10)

com = ttk.Combobox(win, values=cities)
com.pack(pady=5)
com.bind('<KeyRelease>', on_key_release)

listbox = Listbox(win)
listbox.pack()
listbox.bind('<<ListboxSelect>>', on_select)

Button(win, text="Check Weather", command=get_weather, bg="#2196F3", fg="white").pack(pady=10)

# Card style frame
card = Frame(win, bg="white", bd=3, relief=RIDGE)
card.pack(pady=20, padx=20, fill="both", expand=True)

result_label = Label(card, text="", font=("Helvetica", 14), bg="white", justify="center")
result_label.pack(pady=40)

win.mainloop()