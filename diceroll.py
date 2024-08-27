from tkinter import *
import random

window = Tk()
window.geometry("700x350")
window.title("Dice roll")

label = Label(window, font=("times", 200) )
def roll():
    dice= ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()


button = Button(window, text="Lets Roll It...", width=40, height=5, font=("ink free", 10),
 bg="black", fg="green",relief=SUNKEN, command=roll)
button.pack(anchor=CENTER)



window.mainloop()