from tkinter import *
import tkinter as tk
import datetime
import requests

def weather():
    api_key='6e7a076df75eaeacc1d9ace016a758ab'
    city=text.get()
    weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    weather=weather_data.json()['weather'][0]['main']
    temp=weather_data.json()['main']['temp']
    humidity=weather_data.json()['main']['humidity']
    pressure=weather_data.json()['main']['pressure']
    feel=weather_data.json()['main']['feels_like']
    wind=weather_data.json()['wind']['speed']

    
    temperature.config(text=(temp,"°","F"))
    feels_like.config(text=("FEELS","LIKE" ,feel ,'°',"F"))
    
    weather_info.config(text=weather)
    humidity_info.config(text=(humidity,'%'))
    wind_info.config(text=(wind,'km/h'))
    pressure_info.config(text=(pressure,'mBar'))
    
    weather=weather.lower()
    
    if weather in ['sunny']:
        root.configure(bg='#FFD700')
    elif weather in ['smoky','haze']:
        root.configure(bg='#B9BBB6')
    elif weather in ['clouds']:
        root.configure(bg='#373737')
    elif weather in ['rain']:
        root.configure(bg='#0496C7')
    elif weather in ['thunder','tornado','storm']:
        root.configure(bg='#363636')
    elif weather in ['clear']:
        root.configure(bg='#84E4F7')
    else:
        root.configure(bg='white')
        
        
        
    
    


root=Tk()
root.geometry('800x800')
root.title('Weather app')

#search box
search_image=PhotoImage(file='search.png')
s_image=Label(image=search_image)
s_image.place(x=20,y=20)
text=tk.Entry(root,justify='center',width=18,font=('helvetica',25,'bold'),bg='#666996',fg='white',border=0)
text.place(x=100,y=25)
text.focus()

#search icon
search_icon=PhotoImage(file='search_icon.png')
image_icon=Button(image=search_icon,borderwidth=0,bg='#666996',cursor='hand2',command=weather)
image_icon.place(x=650,y=22)


#weather image
weather_image=PhotoImage(file='logo.png')
w_image=Label(image=weather_image)
w_image.place(x=50,y=150)


#Bottom 
b_image=PhotoImage(file='box1.png')
bottom_image=Label(image=b_image)
bottom_image.pack(padx=25,pady=25,side=BOTTOM)


#label
label1=Label(root,text='WEATHER',font=('Helvetica',15,'bold'),fg='White',bg='#AD6378')
label1.place(x=100,y=600)

label2=Label(root,text='HUMIDITY',font=('Helvetica',15,'bold'),fg='White',bg='#AD6378')
label2.place(x=250,y=600)


label3=Label(root,text='WIND SPEED',font=('Helvetica',15,'bold'),fg='White',bg='#AD6378')
label3.place(x=430,y=600)


label4=Label(root,text='PRESSURE',font=('Helvetica',15,'bold'),fg='White',bg='#AD6378')
label4.place(x=600,y=600)

#info
temperature=Label(font=('arial',50,'bold'),fg='red')
temperature.place(x=400,y=150)
feels_like=Label(font=('arial',15,'bold'))
feels_like.place(x=400,y=250)



weather_info=Label(font=('arial',20,'bold'),bg='#AD6378')
weather_info.place(x=100,y=630)

humidity_info=Label(font=('arial',20,'bold'),bg='#AD6378')
humidity_info.place(x=250,y=630)

wind_info=Label(font=('arial',20,'bold'),bg='#AD6378')
wind_info.place(x=430,y=630)

pressure_info=Label(font=('arial',20,'bold'),bg='#AD6378')
pressure_info.place(x=600,y=630)


root.mainloop()



