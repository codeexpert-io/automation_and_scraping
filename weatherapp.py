#WEATHER APP
import requests
from tkinter import Label
from tkinter import Tk
import tkinter as tk
from PIL import ImageTk, Image

def main():
    master.mainloop()

#create display window
master = Tk()
master.geometry("800x500")
master.title("Weather App")
master.config(bg="white")

#open and display image in window
img = Image.open("C:\\Users\\wcalm\\OneDrive\\Desktop\\weather-2021-12-07.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

#updates GUI when button is clicked
def get_city():
    city1 = myentry.get()
    if city1 != "":
        getWeather()

#create button
myentry = tk.Entry(master)
myentry.grid(row=3, padx=180)
button = tk.Button(master, text="SUBMIT", command=get_city)
button.grid(row=4, padx=180)

#scrapes weather info from API
def getWeather():
    url = "http://api.openweathermap.org/data/2.5/weather?"
    api = "cba34d55f9976b4813f7a08f1b3b2374"
    city = myentry.get()
    main_url = url + "appid=" + api + "&q=" + myentry.get()

    page = requests.get(main_url).json()
    location = city
    temperature = str(round(page["main"]["temp"] - 273)) + "°C"
    weatherPrediction = page["weather"][0]["description"]

    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)

    temperatureLabel.after(60000, getWeather)
    master.update()

#displays weather info
locationLabel = Label(master, font=("Calibri bold", 20), bg="white")
locationLabel.grid(row=0, sticky="N", padx=100)
temperatureLabel = Label(master, font=("Calibri bold", 70), bg="white")
temperatureLabel.grid(row=1, sticky="W", padx=180)
Label(master, image=img, bg='white').grid(row=1, sticky="E")
weatherPredictionLabel = Label(master, font=("Calibri bold", 15), bg="white")
weatherPredictionLabel.grid(row=2, sticky="W", padx=180)



if __name__=='__main__':
    main()
