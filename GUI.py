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
    from tkinter import Toplevel
elif (sys.platform == 'darwin'):
    from tkinter import *
    from tkinter.ttk import *
else:
    from tkinter import *
    from tkinter.ttk import *    
    from tkinter import Toplevel
    from enum import Enum
    from tkinter import Frame

# enumeration for instrument type
window = Tk()

class instruments(Enum):

    BONGOS = 1
    THERAMIN = 2
    COMPOSER = 3


    



# toplevel controller for window groups

top = Toplevel(bg="white")

#  window for windows users

class InstrumentWindow(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.instrument = None
        








'''
Widgets
'''

title = Label(text="Instruments", foreground="white", background="gray")

# Basic buttons
startButton = Button(width=10)
stopButton = Button(width=10)
recordButton = Button(width=10)

# List box buttons
instruList = Listbox(background="gray", width=20)
instruList.insert(1, "Bongos")
instruList.insert(2, "Guitar")
instruList.insert(3, "Theremin")

instruList.pack()

#

title.pack()
instruList.pack()

# User
window.mainloop()