from tkinter import *

from time import *

window = Tk()
window.title("Digital Clock")
window.resizable(False,False)

def update():
    text = strftime("%H:%M:%S %p")
    time_label.config(text=text)
    time_label.after(1000,update)

time_label = Label(window, font= ("digital-7", 50 , "bold"),background="green", foreground="blue")
time_label.pack(anchor="center")

update()


window.mainloop()