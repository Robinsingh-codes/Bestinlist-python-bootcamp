from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Registration screen")

window.geomerty('400x400')

window.configure(background = "blue")

Firstname = Label(window, text = "First name").grid(row=0,column=0)

Middlename = Label(window,text = "Middle name").grid(row=1,column=0)

Lastname = Label(window,text= "Last name").grid(row=2,column=0)

Employid = Label(window,text = "Employid").grid(row =3,column=0)

Email = Label(window,text = "Email id").grid(row=4,column=0)

Mobile = Label(window,text = "Contact number").grid(row=5,column=0)

Fathername = Label(window,text="Father name").grid(row=6,column=0)

Fathercontact= Label(window,text= "father's contact").grid(row=7,column=0)

Nationality = Label(window,text="Nationality").grid(row=8,column=0)

Religion = Label(window,text="Religion").grid(row=9,column=0)

Adress = Label(window,text = "Adress").grid(row=10,column=0)

Firstname1 = Entry(window).grid(row=0,column=1)

Middlename1 = Entry(window).grid(row=1,column=1)

Lastname1 = Entry(window).grid(row=2,column=1)

Employid1 = Entry(window).grid(row=3,column=1)

Email1 = Entry(window).grid(row=4,column=1)

Mobile1 = Entry(window).grid(row=5,column=1)

Fathername1 = Entry(window).grid(row=6,column=1)

Fathercontact1 = Entry(window).grid(row=7,column=1)

Nationality1 = Entry(window).grid(row=8,column=1)

Religion1 = Entry(window).grid(row=9,column=1)

Adress1 = Entry(window).grid(row=10,column=1)

def clicked():

    res = "welcome to " + txt.get()

    lbl.configure(text=res)

    btn = ttk.Button(window,text="Submit").grid(row=4,column=0)

window.mainloop()

