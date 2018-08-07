

from tkinter import *
import random
from tkinter import messagebox 


def generate():
    entry.delete(0,END)
    pwd = generatepwd()
    entry.insert(10,pwd)
    
def generatepwd():
    low = "abcdefghijklmnopqrstuvwxyz"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    length = var1.get()
    choice = var.get()
    password = ""
    if choice == 1:
        for i in range(length):
            password += random.choice(low)
        return password
    
    elif choice == 2:
        for i in range(length):
            password += random.choice(medium)
        return password
    
    elif choice == 3:
        for i in range(length):
            password += random.choice(strong)
        return password
    else:
        messagebox.showinfo("Alert", "Please choose Password Complexity")
    
def printpassword():
    password = entry.get()
    if password == "":
       messagebox.showinfo("Alert", "Please Generate Password First") 
    else:
        messagebox.showinfo("Generated Password", "Generated Password is {}".format(password))
        print(password)

root = Tk()
root.resizable(0,0)
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
rp=Label(root,text="RandomPass")
rp.grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=0,column=1)
length = Label(root,text="Length")
length.grid(row=1)
copy=Button(root,text="Print",command=printpassword)
copy.grid(row=0,column=2)
generate=Button(root,text="Generate",command=generate)
generate.grid(row=0,column=3)

radio_low = Radiobutton(root, text="Low",variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium",variable=var,  value=2)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong",variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')



combo = Combobox(root,textvariable=var1)
 
#Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

root.mainloop()
