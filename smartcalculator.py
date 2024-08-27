from tkinter import *
import math


def click(value):
    ex=entry.get()
    Answer = ""
    try:

        if value == "C":
            ex = entry.get()
            ex = ex[0:len(ex)-1]
            entry.delete(0,END)
            entry.insert(0,ex)
            return
        elif value == "CE":
            entry.delete(0, END)

        elif value == "√":
            Answer = math.sqrt(eval(ex))

        elif value == "π":
            Answer = math.pi
        
        elif value == "sin":
            Answer = math.sin(math.radians(eval(ex)))
        

        elif value == "cos":
            Answer = math.cos(math.radians(eval(ex)))
        
        
        elif value == "tan":
            Answer = math.tan(math.radians(eval(ex)))

        elif value == "2π":
            Answer = 2*math.pi
            

        elif value == "sinh":
            Answer = math.sinh(math.radians(eval(ex)))
        
        
        elif value == "cosh":
            Answer = math.cosh(math.radians(eval(ex)))
            

        
        elif value == "tanh":
            Answer = math.tanh(math.radians(eval(ex)))
            

        
        elif value == chr(8731):
            Answer =eval(ex)**(1/3)
            

        elif value == "deg":
            Answer =math.degrees(eval(ex))
            

        elif value == "rad":
            Answer =math.radians(eval(ex))
            

        elif value == "e":
            Answer =math.e
            
        elif value == "^":
            entry.insert(END, "**")
            return

        elif value == "x!":
            Answer = math.factorial(ex)

        
        elif value == "log10":
            Answer = math.log10(eval(ex))
            

        
        elif value == "log2":
            Answer = math.log2(eval(ex))

        elif value == "/":
            entry.insert(END, "/")
            return

        elif value == "=":
            Answer =eval(ex)

        else:
            entry.insert(END, value)
            return
        


        entry.delete(0, END)    
        entry.insert(0, Answer)
    except SyntaxError:
        pass


window = Tk()

window.title("smart calculator")
window.config(background="black")
window.geometry("650x420")
window.resizable(False, False)




entry = Entry(window, font= ("Arial", 20, "bold"), background="white",fg="green", width= 30, relief= SUNKEN, bd=10,   )
entry.grid(row=0, column=0, columnspan=7)

button_list = ["C", "CE", "√","log10" ,"^", "log2", "2π" ,"π",
                "sin", "1", "2", "3","cos","tan", "sinh","tanh",
               chr(8731), "4", "5", "6", "/", "deg", "rad",
               "e", "x!", "7","8", "9","*", "+", "-", "=",
               "0"]

rowvalue = 1
columnvalue = 0
for i in button_list:


    button = Button(window, width=5, height= 2, relief=SUNKEN, bd = 5, text=i,bg="black",
    fg="white", font=("arial", 16, "bold") , activebackground= "black", command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue)
    columnvalue+=1
    if columnvalue >7:
        rowvalue+=1
        columnvalue=0






window.mainloop()