'''
v0.2 - GUI

Cal Tumminello
'''

'''
self.instruList = Listbox(bg='gray')
        self.instruList.insert(0, "Bongos")
        self.instruList.insert(1, "Guitar")
        self.instruList.insert(2, "Theremin")
        self.instruList.pack()
        self.instruList
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
    from enum import Enum
else:
    from tkinter import *
    from tkinter.ttk import *    
    from tkinter import Toplevel
    from enum import Enum
    from tkinter import Frame
# enumeration for instrument type

class Instruments(Enum):

    BONGOS = Enum
    THERAMIN = Enum
    GUITAR = Enum


    



# toplevel controller for window groups

top = Toplevel(bg="black")



#  window for windows users

class InstrumentWindow(Frame):
    def __init__(self) -> None:
        super().__init__()
        
        self.instrument = Instruments.BONGOS

        


    def setInstrument(self, instru):
        self.instrument = instru
    
    def getInstrument(self) -> Instruments:
        return self.instrument

    




window = InstrumentWindow()



'''
Widgets
'''

title = Label(text="Instruments")

# Basic buttons
startButton = Button()
stopButton = Button()
recordButton = Button()

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