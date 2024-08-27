from tkinter import *
from PIL import ImageTk, Image
import sqlite3

window = Tk()
window.title("Address book")
window.geometry("450x300")

conn = sqlite3.connect('address_book.sqlite3')

c = conn.cursor()
'''
c.execute('DROP TABLE IF EXISTS address')

c.execute('CREATE TABLE address (FIRST_NAME TEXT, LAST_NAME TEXT, ADDRESS TEXT, CITY TEXT, STATE TEXT)')
'''
try:
    def submit():
            
        conn = sqlite3.connect('address_book.sqlite3')
        c = conn.cursor()

        c.execute("INSERT INTO address VALUES(:A,:B,:C,:D,:E)",
                {
                    'A': firstname.get(),
                    'B': lastname.get(),
                    'C': adddress.get(),
                    'D': city.get(),
                    'E': state.get(),
                }
                
                )
        conn.commit()
        conn.close()

        firstname.delete(0,END)
        lastname.delete(0,END)
        adddress.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)

       

except Exception:
    print("details added successfully")

def query():
    conn = sqlite3.connect('address_book.sqlite3')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM address " )
    records = c.fetchall()
    print(records)

    recordss = ''
    for i in records:
        recordss += str(i[0]) + " " 

    query_label = Label(window, text=recordss)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def delete():
     conn = sqlite3.connect('address_book.sqlite3')
     c = conn.cursor()

     c.execute("DELETE FROM address WHERE oid = PLACEHOLDER")

     conn.commit()
     conn.close()







firstname = Entry(window, width=30, relief=SUNKEN)
firstname.grid(row=0, column=1)


lastname = Entry(window, width=30 , relief=SUNKEN)
lastname.grid(row=1, column=1)

adddress = Entry(window, width=30, relief=SUNKEN)
adddress.grid(row=2, column=1)

city = Entry(window, width=30, relief=SUNKEN)
city.grid(row=3, column=1)

state = Entry(window, width=30, relief=SUNKEN)
state.grid(row=4, column=1)

delete_box = Entry(window, width=30)
delete_box.grid(row=9, column=1)

first_label = Label(window, text="firstname", font=("Arial", 10, "bold"))
first_label.grid(row=0, column=0)

last_label = Label(window, text="lastname",font=("Arial", 10, "bold"))
last_label.grid(row=1, column=0)

adddress_label = Label(window, text="address", font=("Arial", 10, "bold"))
adddress_label.grid(row=2, column=0)

city_label = Label(window, text="city", font=("Arial", 10, "bold"))
city_label.grid(row=3, column=0)

state_label = Label(window, text="state" ,font=("Arial", 10, "bold"))
state_label.grid(row=4, column=0)
delete_box_label = Label(window, text="ID NUMBER")
delete_box_label.grid(row=9, column=0)
btn = Button(window, text="Add record to database", command=submit)
btn.grid(row= 6, column=0, columnspan=2, ipadx=137)

Q_btn = Button(window, text="Show records", command=query)
Q_btn.grid(row = 7, column=0, columnspan=2, ipadx=137)

delete_btn = Button(window, text="Delete records", command=delete)
delete_btn.grid(row = 10, column=0, columnspan=2, ipadx=135)


conn.commit()


conn.close()




window.mainloop()