'''
v0.2 - GUI

Cal Tumminello
'''

# import tkinter as tk
import sys
import cv2 
#from PIL import ImageTk, Image

# Changes import based on os 
if (sys.platform == "linux" or sys.platform == "linux2"):
    from tk import * 
elif (sys.platform == "win64"):
    from tkinter import *
    from tkinter.ttk import *
elif (sys.platform == 'darwin'):
    from tkinter import *
    from tkinter.ttk import *
else:
    from tkinter import *
    from tkinter.ttk import *

#  window for windows users
window = Tk()

'''
Widgets
'''

title = Label(text="Instruments")

# Basic buttons
startButton = Button()
stopButton = Button()
recordButton = Button()

# List box buttons
instruList = Listbox(bg='gray')
instruList.insert(1, "Bongos")
instruList.insert(2, "Guitar")
instruList.insert(3, "Theremin")

# 

title.pack()
instruList.pack()

# User
window.mainloop()