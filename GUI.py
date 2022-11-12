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
    from tkinter import Toplevel
    from tkinter.ttk import *
elif (sys.platform == 'darwin'):
    from enum import Enum
    from tkinter import *
    from tkinter.ttk import *
else:
    from enum import Enum
    from tkinter import *
    from tkinter import Frame, Toplevel
    from tkinter.ttk import *

# enumeration for instrument type
window = Tk()

class Instruments(Enum):

    BONGOS = 1
    THERAMIN = 2
    COMPOSER = 3


    



# toplevel controller for window groups

top = Toplevel(bg="black")



#  window for windows users

class InstrumentWindow(Frame):
    def __init__(self, instrumentNum) -> None:
        super().__init__()

        self.instrument = Instruments(instrumentNum).name
        self.instruList = Listbox(bg='gray')
        self.instruList.insert(1, "Bongos")
        self.instruList.insert(2, "Guitar")
        self.instruList.insert(3, "Theremin")
        self.instruList.pack()
        

    def setInstrument(self, instru):
        self.instrument = instru

    def getInstrument(self) -> Instruments:
        return self.instrument





window = InstrumentWindow()



'''
Widgets
'''

title = Label(text="Instruments", foreground="white", background="gray")

# Basic buttons
startButton = Button(width=10)
stopButton = Button(width=10)
recordButton = Button(width=10)

# List box buttons
# instruList = Listbox(bg='gray')
# instruList.insert(1, "Bongos")
# instruList.insert(2, "Guitar")
# instruList.insert(3, "Theremin")

# instruList.pack()

#

title.pack()
# instruList.pack()

# User
window.mainloop()