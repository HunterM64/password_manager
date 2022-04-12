import tkinter as tk

window = tk.Tk()

title = tk.Label(text = "M64's Password Generator")
title.pack()

def open_popup():
    top = tk.Toplevel()
    top.title("Generated Password")
    tk.Label(top, text = "Your password is: ").pack()

generate = tk.Button(text = "Generate Password", command = open_popup)
generate.pack()

window.mainloop()