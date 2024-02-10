import tkinter as tk # basic logic
from tkinter import ttk #gives widgets

# window

window = tk.Tk()

# title
window.title("Demo")
window.geometry('300x150') # width by height
 
# widget number 1 - the labelings

title_label = ttk.Label(master = window, text = "Miles to kilometers", font = "Arial 20 bold") # a widget which has text
title_label.pack() # place widget into master - which is the window

# input field
input_widget = ttk.Frame(master = window)
entry = ttk.Entry(master = input_widget)
button = ttk.Button(master = input_widget, text = "Convert")

# place widgets into masters 
button.pack(side = "left", padx=10) # this cuses it fro it it be right next to each other
entry.pack(side = "left")
input_widget.pack(pady= 10)

# run window
window.mainloop()