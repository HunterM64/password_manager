import tkinter as tk
from tkinter import ttk
import generator as gen

def display_text():
    global entry
    string = entry.get()
    print(string)
    
    password = gen.generate(string)
    print(password)
    
    win2 = tk.Tk()
    win2.title("Password Generated")
    label2 = tk.Label(win2, text = password)
    label2.pack()

    

window = tk.Tk()

label = tk.Label(window, text="Enter length for password:")
label.pack()

entry = tk.Entry(window)
entry.focus_set()
entry.pack()

ttk.Button(window, text="OK", command= display_text).pack()

window.mainloop()