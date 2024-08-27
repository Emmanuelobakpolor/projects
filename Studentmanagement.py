from tkinter import *
from tkinter import ttk
import mysql.connector as pymysql


class Student:
    def __init__(self,window):
        self.window=window
        self.window.title("Student Management System")
        self.window.geometry("1350x700+0+0")
        self.window.resizable(False, False)
        self.window.title("Student management")

        title=Label(self.window, text="Student Mangement System", relief=SUNKEN, bd=10 ,font=("Consolas", 30, "bold"), bg="black",fg=
                    "blue")
        title.pack(side=TOP, fill=X)


        self.Roll_No=StringVar()
        self.Name=StringVar()
        self.MatricNo=StringVar()
        self.HostelName=StringVar()
        self.Contact=StringVar()
        self.Course=StringVar()
        self.Gender=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        manage_frame = Frame(self.window, bd=4, relief=RIDGE, bg="blue")
        manage_frame.place(x=20,y=100, width=450, height=570)

        detail_frame = Frame(self.window, bd=4, relief=RIDGE, bg="blue")
        detail_frame.place(x=500,y=100, width=750, height=570)

        manage_title = Label(manage_frame, text="Manage Students", bg="blue", fg="black", font=("Consolas", 17, "bold") )
        manage_title.grid(row=0,columnspan=2 )

        roll_no1 = Label(manage_frame, text="Roll_No", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no1.grid(row=1,columnspan=2 , pady=20, padx=10, sticky="w")

        Text_row = Entry(manage_frame, textvariable=self.Roll_No, font=("Consolas", 10, "bold"), bd=5, relief=SUNKEN )
        Text_row.grid(row=1,column=2,pady=10, padx=5, sticky="w")

        roll_no2 = Label(manage_frame, text="Name", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no2.grid(row=2,columnspan=2 , pady=20, padx=10, sticky="w")
        Text_row2 = Entry(manage_frame,textvariable=self.Name,  font=("Consolas", 10, "bold"), bd=5, relief=SUNKEN )
        Text_row2.grid(row=2,column=2,pady=10, padx=5, sticky="w")

        roll_no3 = Label(manage_frame, text="MatricNO", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no3.grid(row=3,columnspan=2 , pady=20, padx=10, sticky="w")
        Text_row3 = Entry(manage_frame,textvariable=self.MatricNo,  font=("Consolas", 10, "bold"), bd=5, relief=SUNKEN )
        Text_row3.grid(row=3,column=2,pady=10, padx=5, sticky="w")


        roll_no4 = Label(manage_frame, text="HostelName", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no4.grid(row=4,columnspan=2 , pady=20, padx=10, sticky="w")
        Text_row4 = Entry(manage_frame, textvariable=self.HostelName,  font=("Consolas", 10, "bold"), bd=5, relief=SUNKEN )
        Text_row4.grid(row=4,column=2,pady=10, padx=5, sticky="w")

        roll_no5 = Label(manage_frame, text="Contact", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no5.grid(row=5,columnspan=2 , pady=20, padx=10, sticky="w")
        Text_row5 = Entry(manage_frame, textvariable=self.Contact,  font=("Consolas", 10, "bold"), bd=5, relief=SUNKEN )
        Text_row5.grid(row=5,column=2,pady=10, padx=5, sticky="w")

        roll_no6 = Label(manage_frame, text="Course", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no6.grid(row=6,columnspan=2 , pady=20, padx=10, sticky="w")
        Text_row6 = Entry(manage_frame, textvariable=self.Course, font=("Consolas", 10, "bold"), bd=5, relief=SUNKEN )
        Text_row6.grid(row=6,column=2,pady=10, padx=5, sticky="w")


        roll_no7 = Label(manage_frame, text="Gender", bg="blue", fg="black", font=("Consolas", 15, "bold") )
        roll_no7.grid(row=7,columnspan=2 , pady=20, padx=10, sticky="w" )
        gender  = ttk.Combobox(manage_frame, textvariable=self.Gender,  font=("Consolas", 12, "bold") )
        gender['values']=['male', 'female']
        gender.grid(row=7, column=2, pady=10, sticky="w")


        button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="blue")
        button_frame.place(x=10, y=500, width= 400)

        addbutton = Button(button_frame, text="Add", width=10, command=self.add_students)
        addbutton.grid(row=0, column=0, padx=10, pady=10)

        addbutton = Button(button_frame, text="Update", command=self.update,  width=10)
        addbutton.grid(row=0, column=1, padx=10, pady=10)

        addbutton = Button(button_frame, text="Delete", command=self.delete_data, width=10)
        addbutton.grid(row=0, column=2, padx=10, pady=10)

        addbutton = Button(button_frame, text="Clear", command=self.clear, width=10)
        addbutton.grid(row=0, column=3, padx=10, pady=10)

        search_by = Label(detail_frame, text="Search by", bg="blue", fg="black", font=("Consolas", 17, "bold"))
        search_by.grid(row=0, column=0, padx=10, pady=10)

        search_bycombo = ttk.Combobox(detail_frame, textvariable=self.search_by, width=10, font=("Consolas", 14, "bold"))
        search_bycombo["values"] = ["Roll_no", "MatricNo", "Name"]
        search_bycombo.grid(row=0, column=1, padx=10, pady=10)

        txtentry = Entry(detail_frame, textvariable=self.search_txt, font=("Consolas", 14, "bold"), width=20)
        txtentry.grid(row=0, column=2, padx=10,pady=10)

        searchbtn = Button(detail_frame, text="Search", width=10)
        searchbtn.grid(row=0, column=3, padx=10,pady=10)

        showall = Button(detail_frame, text="Show all", width=10)
        showall.grid(row=0, column=4, padx=10,pady=10)

        table_frame = Frame(detail_frame, bd=2, relief=SUNKEN, bg="blue")
        table_frame.place(x=10, y=70,width=720, height=460)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("roll", "name", "matricno", "hostelname", "contact", "course", "gender"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll", text="Roll_no")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("matricno", text="Matricno")
        self.student_table.heading("hostelname", text="Hostelname")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("course", text="Course")
        self. student_table.heading("gender", text="Gender")

        self.student_table['show']='headings'
        self.student_table.column('roll', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('matricno', width=100)
        self.student_table.column('hostelname', width=100)
        self.student_table.column('contact', width=100)
        self.student_table.column('course', width=100)
        self.student_table.column('gender', width=100)



        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="smt"
                             )

        conn = db.cursor()
        conn.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No.get(),
                                                                              self.Name.get(),
                                                                              self.MatricNo.get(),
                                                                              self.HostelName.get(),
                                                                              self.Contact.get(),
                                                                              self.Course.get(),
                                                                              self.Gender.get(),
                                                                              ))
        db.commit()
        self.fetch_data()
        self.clear()
        db.close()


    def fetch_data(self):
          db = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="smt"
                             )

          conn = db.cursor()
          conn.execute('select * from students')
          rows = conn.fetchall()
          if len(rows)!=0:
               self.student_table.delete(*self.student_table.get_children())
               for i in rows:
                self.student_table.insert('', END, values=i)
               db.commit()
          conn.close()

    def clear(self):
        self.Roll_No.set(""),
        self.Name.set(""),
        self.MatricNo.set(""),
        self.HostelName.set(""),
        self.Contact.set(""),
        self.Course.set(""),
        self.Gender.set(""),
    

    def get_cursor(self,ev):
        cursoro_row=self.student_table.focus()
        content = self.student_table.item(cursoro_row)
        row=content["values"]
        
        self.Roll_No.set(row[0]),
        self.Name.set(row[1]),
        self.MatricNo.set(row[2]),
        self.HostelName.set(row[3]),
        self.Contact.set(row[4]),
        self.Course.set(row[5]),
        self.Gender.set(row[6])

    def update(self):
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="smt"
                             )

        conn = db.cursor()
        conn.execute("update students set Roll=%s, Name=%s, MatricNo=%s,HostelName= %s, Contact=%s, Course=%s,Gender=%s ", (self.Roll_No.get(),
                                                                                                                                        self.Name.get(),
                                                                                                                                        self.MatricNo.get(),
                                                                                                                                        self.HostelName.get(),
                                                                                                                                        self.Contact.get(),
                                                                                                                                        self.Course.get(),
                                                                                                                                        self.Gender.get()
                                                                                                                                        ))
        db.commit()
        self.fetch_data()
        self.clear()
        db.close()

    def delete_data(self):
         db = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="smt")
         
         conn = db.cursor()

         conn.execute('delete from students where Roll_no=%s',self.Roll_No.get())
                                                                                                                                       
        
         db.commit()
         self.fetch_data()
         self.clear()


    

          
            
               

        



window = Tk()

ob=Student(window)
window.mainloop()