from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymongo
import datetime
from emperor_mong import add_user

client = pymongo.MongoClient('mongodb://username:password@IPAddress/')

db = client['Database Name']

users = db['users']

reg_window = Tk()
reg_window.title('Registration Form')
reg_window.geometry('300x200')
reg_window.configure(background = 'white');
a = Label(reg_window, text = "Username:").grid(row = 0, column = 0)
b = Label(reg_window, text = "Password:").grid(row = 1, column = 0)
c = Label(reg_window, text = "First Name:").grid(row = 2, column = 0)
d = Label(reg_window, text = "Email address:").grid(row = 3, column = 0)
e = Label(reg_window, text = "Gender:").grid(row = 4, column = 0)
f = Label(reg_window, text = "Location:").grid(row = 5, column = 0)
g = Label(reg_window, text = "Age:").grid(row = 6, column = 0)

aA = Entry(reg_window)
aA.grid(row = 0, column = 1)
bA = Entry(reg_window)
bA.grid(row = 1, column = 1)
cA = Entry(reg_window)
cA.grid(row = 2, column = 1)
dA = Entry(reg_window)
dA.grid(row = 3, column = 1)

var = IntVar()
Radiobutton(reg_window,text = "Male", padx = 1, pady = 0.5, variable= var, value=1).place(x = 100, y = 85)
Radiobutton(reg_window,text = "Female", padx = 1, pady = 0.5, variable= var, value=2).place(x = 150, y = 85)

country_list = ['UK', 'USA', 'Canada', 'Germany', 'Switzerland', 'New Zealand', 'Philippines']
svar = StringVar()
droplist = OptionMenu(reg_window, svar, *country_list)
droplist.config(width = 20)
droplist.grid(row = 5, column = 1)
svar.set('Select your Country')

age_groups = ["<13", "13-17", "18-25", "26-35", ">35"]
rvar = StringVar()
droplist = OptionMenu(reg_window, rvar, *age_groups)
droplist.config(width = 20)
droplist.grid(row = 6, column = 1)
rvar.set('Select your Age')

eA = var
fA = svar
gA = rvar

def sign_up():
    aB = aA.get()
    bB = bA.get()
    cB = cA.get()
    dB = dA.get()
    eB = eA.get()
    fB = fA.get()
    gB = gA.get()
    add_user(aB, bB, cB, dB, eB, fB, gB)
    tkinter.messagebox.showinfo('Welcome', 'Thank you for signing up!')
    reg_window.destroy()


button = ttk.Button(reg_window, text='Sign Up', command = sign_up).grid(row = 8, column = 1)
reg_window.mainloop()
