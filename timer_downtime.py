from time import sleep
from datetime import datetime
import tkinter as tk
# from win10toast import ToastNotifier
from tkinter import *
import winsound

# Keep the program running long enough for the sound to play

window=Tk()
window.geometry("400x400")
window.title("Downtime app")
Label(window,text="welcome to our app",font="bold",fg="blue" ).pack()

now=datetime.now()
time=now.strftime("%H:%M:%S")
Label(window,text="The current time",font="Media",fg="black" ).pack(pady=20)
Label(window,text=time,font="Typeface",fg="black" ).pack()

check=tk.BooleanVar()
hour=tk.IntVar()
minut=tk.IntVar()
second=tk.IntVar()

def downtime():
    h=hour.get()
    m=minut.get()
    s=second.get()
    t=h*3600+m*60+s
    while t!=0:
        m,n=divmod(t,60)
        m_time=f"{m}:{n}"
        sleep(1)
        window.update()
        Label(window,text=m_time,font="Serif",fg="black" ).pack()
        t-=1
    if check:
       winsound.Beep(440, 500)    
    Label(window,text="Time is over",font="bold",fg="black" ).place(x=150,y=250)
Checkbutton(window,text="Press me to get sound",variable=check,fg="black").pack()
Entry(window,width=20,textvariable=hour).pack()
Entry(window,width=20,textvariable=minut).pack()
Entry(window,width=20,textvariable=second).pack()
Button(window,command=downtime,fg="white",background="red",text="press me to start").pack()
window.update()
window.mainloop()