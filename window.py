import tkinter as tk
from tkinter import ttk
import generator as gen

def get_length():
    
    # Setup window 
    winLength = tk.Tk()
    winLength.geometry("200x100")
    winLength.title("Generator")

    # Setup label
    labelLength = tk.Label(winLength, text="Enter length for password:")
    labelLength.pack()

    # Setup entry
    entry = tk.Entry(winLength)
    entry.focus_set()
    entry.pack()

    # Submit button
    ttk.Button(winLength, text="OK", command= lambda: display_password(entry)).pack()

def display_password(length_var):

    length = length_var.get()
    
    password = gen.generate(length)
    
    winDisp = tk.Tk()
    winDisp.geometry("200x100")
    winDisp.title("Password")

    labelDisp = tk.Label(winDisp, text = "Password generated:\n" + password)
    labelDisp.place(anchor = "center", relx = 0.5, rely = 0.5)

def view_passwords():
    winPass = tk.Tk()
    winPass.geometry("200x100")
    winPass.title("Passwords")

    labelPass = tk.Label(winPass, text = "TODO")
    labelPass.place(anchor = "center", relx = 0.5, rely = 0.5)

# Setup Window
winMain = tk.Tk()
winMain.geometry("250x100")
winMain.title("M64's Password Generator")

# Create Buttons
ttk.Button(winMain, text = "Generate Password", command = get_length).place(anchor = "center", relx = 0.5, rely = 0.3)
ttk.Button(winMain, text = "View Passwords", command = view_passwords).place(anchor = "center", relx = 0.5, rely = 0.7)

# idk needs to be here
winMain.mainloop()