'''
v0.1 - GUI
'''
import tkinter as tk
window = tk.Tk()

# Code to add widgets will go here...

title = tk.Label(text="Instruments")
instruList = tk.Listbox()
instruList.insert(1, "Bongos")
instruList.insert(2, "Guitar")
instruList.insert(3, "Theremin")

title.pack()
instruList.pack()

window.mainloop()