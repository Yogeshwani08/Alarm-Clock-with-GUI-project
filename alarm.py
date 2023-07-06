from tkinter import *
from tkinter import messagebox
import time, sys
from pygame import mixer
from PIL import Image, ImageTk

def alarm():
    alarm_time=user_input.get()
    if alarm_time=="":
        messagebox.askretrycancel("Error Message","Please Enter Value")
    else:
        while True:
            time.sleep(1)
            if (alarm_time==time.strftime("%H:%M")):
                playmusic()
def playmusic():
    mixer.init()
    mixer.music.load("Tone.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()



root = Tk()
root.title("Alarm Clock")
root.geometry("1595x895")
canvas=Canvas(root,width=1595,height=895)
image=ImageTk.PhotoImage(Image.open("bgimg.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
header=Frame(root)

box1=Frame(root)
box1.place(x=550,y=300)
box2=Frame(root)
box2.place(x=550,y=380)

#Time taken by User as Input
user_input=Entry(box1,font=('Arial Narrow',20),width=9)
user_input.grid(row=0,column=2)

#Set Alarm Button
start_button = Button(box2,text="Set Alarm",font=('Alarm Narrow',16,'bold'),command=alarm)
start_button.grid(row=2,column=2)


root.mainloop()