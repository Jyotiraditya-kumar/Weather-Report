from tkinter import *
from tkinter import messagebox, scrolledtext
import random

import datetime
import requests
import sqlite3
import json
font = "arial 20 bold"
font1 = "arial 15 bold"
API_KEY = "30f6c106bcb8a07748abf4b73139abdb"
# img=requests.get("https://source.unsplash.com/1600x900/?city=mumbai")
def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&q={city}&units=metric"
        weather_data=requests.get(url).json()
        temp.set(weather_data['main']['temp'])
        wind.set(weather_data['wind']['speed'])
        desc.set(weather_data['weather'][0]['description'])
        lat.set(weather_data['coord']['lat'])
        long.set(weather_data['coord']['lon'])
        humidity.set(weather_data['main']['humidity'])
        l1.configure(text=f"Weather in {city}")
        l22.configure(text=temp.get())
        l32.configure(text=desc.get())
        l42.configure(text=wind.get())
        l52.configure(text=f"lat={lat.get()} long = {long.get()}")
        l62.configure(text=humidity.get())
        # l22.configure(text=temp.get())
    except:
        messagebox.showerror("Error", "Something Went Wrong \n Try again after sometime")
    
    
    
    
    
root = Tk()
cname = StringVar()
temp = StringVar()
wind = StringVar()
desc = StringVar()
lat = StringVar()
long = StringVar()
humidity = StringVar()

cname.set("")
temp.set("")
wind.set("")
desc.set("")
lat.set("")
long.set("")
humidity.set("")

root.title("WEATHER")
root.geometry("1920x1080")

cname.set("Mumbai")
container = Frame(root)
container.place(relwidth=1, relheight=1)
lab = Label(container, text="WEATHER", fg="red", font="arial 40 bold")
lab.place(relx=.45, rely=.05)
l1 = Label(container, text="City Name", fg="red", font=font)
l1.place(relx=.3, rely=.15)
e1 = Entry(container, textvariable=cname, width=30,font=font1, border=10, insertwidth=4)
e1.place(relx=.5, rely=.15)
bg = PhotoImage(file = "Photo.png")
  
# Create Canvas

frame = LabelFrame(container, text="Weather Report")
frame.place(relx=.2, rely=.3, relheight=.6, relwidth=.6)
canvas1 = Canvas( frame, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

l1 = Label(frame, text=f"Weather in "+cname.get(), fg="red", font=font)
l1.place(relx=.3, rely=.02)

l21 = Label(frame, text="Temperature", font=font)
l21.place(relx=.1, rely=.15)
l22 = Label(frame, text="--- C", font=font)
l22.place(relx=.5, rely=.15)

l31 = Label(frame, text="Description", font=font)
l31.place(relx=.1, rely=.30)
l32 = Label(frame, text="--- C", font=font)
l32.place(relx=.5, rely=.30)

l41 = Label(frame, text="Wind Spped", font=font)
l41.place(relx=.1, rely=.45)
l42 = Label(frame, text="--- C", font=font)
l42.place(relx=.5, rely=.45)

l51 = Label(frame, text="Coordinates", font=font)
l51.place(relx=.1, rely=.60)
l52 = Label(frame, text="--- C", font=font)
l52.place(relx=.5, rely=.60)

l61 = Label(frame, text="Humidity", font=font)
l61.place(relx=.1, rely=.75)
l62 = Label(frame, text="--- C", font=font)
l62.place(relx=.5, rely=.75)

b=Button(container, text="Search", font=font1, relief=GROOVE,command=lambda:fetch_weather(cname.get()))
b.place(relx=0.5, rely=0.25, relwidth=0.15)
# root.wm_attributes("-transparentcolor", 'grey')


root.mainloop()
