from tkinter import *
import tkinter as tk

GREY_LIGHT = "#F5F5F5"
LABEL_VALUE = "#25265E"
SMALL_FONT_STYLE=("Arial", 16)
LARGE_FONT_STYLE=("Arial", 40, "bold")
BUTTON_FONT_STYLE = ("Arial", 24, "bold")

class calculator:
    def __init__(self):
        self.window =tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(False,False)
        self.window.title(" Calculator Program")
        
        self.total_expression = ""
        self.current_expression = ""
     

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()

        



        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,1)
        }

        self.operations ={"/": "\u00F7", "*": "\u0007", "-" : "-", "+":"+"}


        self.display_button = self.create_display_button()
        self.create_digit_button()
        self.create_operator_button()
        self.special()
        self.display_button.rowconfigure(0,weight=1)

        for x in range(1,5):
            self.display_button.rowconfigure(x,weight=1)
            self.display_button.columnconfigure(x,weight=1)

    def special(self):
        self.create_equal_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_sqt_button()

        
    def create_display_label(self):
        total_label = tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E, bg=GREY_LIGHT, fg=LABEL_VALUE,padx=24,
                                font=SMALL_FONT_STYLE )
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E, bg=GREY_LIGHT, fg=LABEL_VALUE,padx=24,
                                font=LARGE_FONT_STYLE )
        label.pack(expand=True, fill="both")

        return total_label, label


        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=GREY_LIGHT)
        frame.pack(expand=True, fill="both")
        return frame


    
        

    
    def add_to_exp(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_button(self):
        for digits,grid_value in self.digits.items():
            button = tk.Button(self.display_button, text=str(digits), bg="white", fg=LABEL_VALUE, font=BUTTON_FONT_STYLE, borderwidth=0, command= lambda x=digits: self.add_to_exp(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


    def append_operator(self, operator): 
        self.current_expression += operator
        self.total_expression+=self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression =""
        self.total_expression=""
        self.update_total_label()
        self.update_label()



    def create_operator_button(self):
        i=0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.display_button, text=symbol, fg=LABEL_VALUE,borderwidth=0, font=BUTTON_FONT_STYLE,bg="white", command= lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1

    def square(self):
        self.current_expression= str(eval(f"{self.current_expression}**2"))
        self.update_label()


    def create_square_button(self):
         button = tk.Button(self.display_button, text="x\u00b2", fg=LABEL_VALUE,borderwidth=0, font=BUTTON_FONT_STYLE,bg="white", command=self.square)
         button.grid(row=0, column=1 ,sticky=tk.NSEW)


    
    def sqt(self):
        self.current_expression= str(eval(f"{self.current_expression}**0.5"))
        self.update_label()


    def create_sqt_button(self):
         button = tk.Button(self.display_button, text="\u221ax", fg=LABEL_VALUE,borderwidth=0, font=BUTTON_FONT_STYLE,bg="white", command=self.sqt)
         button.grid(row=0, column=3, sticky=tk.NSEW)

    
    def create_clear_button(self):
         button = tk.Button(self.display_button, text="C", fg=LABEL_VALUE,borderwidth=0, font=BUTTON_FONT_STYLE,bg="white", command=self.clear)
         button.grid(row=0, column=2, sticky=tk.NSEW)


    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        try:

            self.current_expression = str(eval(self.total_expression))
            self.total_expression =""
            self.update_label()

        except Exception:
           self.current_expression = " Syntax Error"
           self.update_label()



    def create_equal_button(self):
         button = tk.Button(self.display_button, text="=", fg=LABEL_VALUE,borderwidth=0, font=BUTTON_FONT_STYLE,bg="white", command=self.evaluate)
         button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)
        

    def create_display_button(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_total_label(self):
        expression = self.total_expression
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
   calc = calculator()
   calc.run()
   calc.create_display_label()