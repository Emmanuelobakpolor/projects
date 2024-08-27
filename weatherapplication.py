import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url  = "https://weather.com/en-NG/weather/today/l/1d50ec8b93e0394b20ee9bf6990fef845565ade147c5cd5ee9f7381a930b28d9"

window = Tk()
window.title = ("Weather App")
window.config(bg="white")

img= Image.open("Weather-PNG-Background.png")
img=img.resize((150, 150))
img= ImageTk.PhotoImage(img)

def weather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    location = soup.find("h1", class_="CurrentConditions--location--1YWj_").text
    temp = soup.find("span", class_="CurrentConditions--tempValue--MHmYY").text
    pred = soup.find("div",class_="CurrentConditions--phraseValue--mZC_p" ).text
    

    labellocation.config(text =location)
    labeltemp.config(text=temp)
    labelpred.config(text=pred)

    labeltemp.after(60000, weather)
    window.update()

labellocation = Label(window, font=("Arial", 20), bg="white")
labellocation.grid(row=0, sticky="N", padx=100)
labeltemp = Label(window, font=("Arial", 70), bg="white")
labeltemp.grid(row=1, sticky="W", padx=40)
Label(window, image=img, bg="white").grid(row=1, sticky="E")
labelpred = Label(window, font=("Arial", 20), bg="white")
labelpred.grid(row=2, sticky="W", padx=40)
weather()

window.mainloop()