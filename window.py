import tkinter as tk
from tkinter import ttk
import generator as gen
from manager import savePassword, readPasswords

def get_length():
    
    # Setup window 
    winLength = tk.Tk()
    winLength.geometry("200x120")
    winLength.title("Generator")

    # Setup label
    labelLength = tk.Label(winLength, text="Enter length for password:")
    labelLength.pack()

    # Setup entry
    entry = tk.Entry(winLength)
    entry.focus_set()
    entry.pack()

    labelWebsite = tk.Label(winLength, text="Enter website for password:")
    labelWebsite.pack()

    entry2 = tk.Entry(winLength)
    entry2.pack()

    

    # Submit button
    ttk.Button(winLength, text="OK", command= lambda: [display_password(entry, entry2), winLength.destroy()]).pack()

def display_password(length_var, website_var):

    length = length_var.get()
    website = website_var.get()
    
    password = gen.generate(length)
    
    winDisp = tk.Tk()
    winDisp.geometry("200x100")
    winDisp.title("Password")

    labelDisp = tk.Label(winDisp, text = "Password Generated:\n" + password)
    labelDisp.place(anchor = "center", relx = 0.5, rely = 0.5)

    ttk.Button(winDisp, text = "Click to Save Password", command = lambda: [savePassword(website, password), winDisp.destroy()]).place(anchor = "center", relx = 0.5, rely = 0.9)

def view_passwords():
    winPass = tk.Tk()
    winPass.title("Passwords")

    passwordDict = readPasswords()

    for website in passwordDict:
        label = tk.Label(winPass, text = website + ": " + passwordDict[website])
        label.pack(padx = 10, pady = 1, anchor = "w")

# Setup Window
winMain = tk.Tk()
winMain.geometry("250x100")
winMain.title("M64's Password Generator")

# Create Buttons
ttk.Button(winMain, text = "Generate Password", command = get_length).place(anchor = "center", relx = 0.5, rely = 0.3)
ttk.Button(winMain, text = "View Passwords", command = view_passwords).place(anchor = "center", relx = 0.5, rely = 0.7)

# idk needs to be here
winMain.mainloop()