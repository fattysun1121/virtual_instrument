'''
v0.2 - GUI

Cal Tumminello
'''

# import tkinter as tk
import sys
from tkinter import OptionMenu, StringVar

import cv2

from PIL import ImageTk, Image

# Screen sizing
WIDTH = 800
HEIGHT = 700

# Changes import based on os 
if (sys.platform == "linux" or sys.platform == "linux2"):
    from tk import * 
elif (sys.platform == "win64"):
    from tkinter import *
    from tkinter import Toplevel
    from tkinter.ttk import *
elif (sys.platform == 'darwin'):
    from enum import Enum
    import tkinter as tk
    import tkinter.ttk as ttk
else:
    from enum import Enum
    from tkinter import Tk, Label, Frame, Toplevel, Canvas
    import tkinter as tk
    import tkinter.ttk as ttk





'''

Defines the Classes we will use, 

CLASSES: 

Instruments - Enumeration for the types of instruments they will use

InstrumentWindow - 

'''






'''

Defines the Classes we will use, 

CLASSES: 

Instruments - Enumeration for the types of instruments they will use

InstrumentWindow - 

'''


# enumeration for instrument type


class Instruments(Enum):

    BONGOS = 1
    THERAMIN = 2
    COMPOSER = 3

# toplevel controller for window groups

# Sets up User Interface
class InstrumentWindow(tk.Tk):
    def __init__(self, instru=1, master=None):
        super().__init__()
        self.instrument = instru
        # self.geometry(f'{WIDTH}x{HEIGHT}')
        #canvas = Canvas(master, width=WIDTH, height=HEIGHT)

        self.dropBool = False

        # Rows
        self.row1 = tk.Label(master, bg='pink', text= ' ', height=int(self.winfo_height() / 30), width=int(self.winfo_width() / 20)).grid(row=0, column=0)
        self.row2 = tk.Label(master, bg='light gray', text= ' ', height=int(self.winfo_height() / 30), width=int(self.winfo_width() / 20)).grid(row=1, column=0)
        self.row3 = tk.Label(master, bg='pink', text= ' ', height=int(self.winfo_height() / 30), width=int(self.winfo_width() / 20)).grid(row=2, column=0)
        self.row4 = tk.Label(master, bg='light gray', text= ' ', height=int(self.winfo_height() / 30), width=int(self.winfo_width() / 20)).grid(row=3, column=0)
        self.row5 = tk.Label(master, bg='pink', text= ' ', height=int(self.winfo_height() / 30), width=int(self.winfo_width() / 20)).grid(row=4, column=0)

        # Columns
        
        self.col1 = tk.Label(master, bg='pink', text= ' ', height=int(self.winfo_height() / 20), width=int(self.winfo_width() / 20)).grid(row=0, column=0)
        self.col2 = tk.Label(master, bg='light gray', text= ' ', height=int(self.winfo_height() / 20), width=int(self.winfo_width() / 20)).grid(row=0, column=1)
        self.col3 = tk.Label(master, bg='pink', text= ' ', height=int(self.winfo_height() / 20), width=int(self.winfo_width() / 20)).grid(row=0, column=2)
        self.col4 = tk.Label(master, bg='light gray', text= ' ', height=int(self.winfo_height() / 20), width=int(self.winfo_width() / 20)).grid(row=0, column=3)
        self.col5 = tk.Label(master, bg='pink', text= ' ', height=int(self.winfo_height() / 20), width=int(self.winfo_width() / 40)).grid(row=0, column=4)
        
        
        self.title = tk.Label(master, bg='light gray', text= 'Handstruments', font=("Times New Roman", 25)).grid(row=0, column=2)
        
        self.instruButt = tk.Button(master, text="instruments", bg='pink', padx=25, pady=20).grid(row=3,column=0)
        
    
    def setInstrument(self, instru):
        self.instrument = instru

    def getInstrument(self):
        print(f'{self.instrument}')
    
    def dropDown(self):

        if self.dropBool == False:
            self.bongoButton = tk.Button(master=self, bg="pink",text='Bongos', padx=25, pady=20).grid(row=3, column=1)
            self.guitarButton = tk.Button(master=self, bg='pink', text='Guitar', padx=25, pady=20).grid(row=4, column=1)
            self.thereminButton = tk.Button(master=self, bg='pink', text='Theremin', padx=25, pady=20).grid(row=5, column=1)
        else:
            self.bongoButton = None
            self.guitarButton = None
            self.thereminButton = None






window = InstrumentWindow()

clicked = StringVar()

drop = OptionMenu(window,clicked, "Bongos", "Guitar", "Theremin")



        

# function to center screen 
def screencenter(o):
    w, h = o.winfo_width(), o.winfo_height()
    x = int((o.winfo_screenwidth() - w) / 2)
    y = int((o.winfo_screenheight() - h) / 2)
    o.geometry(f'{w}x{h}+{x}+{y}')       


# Widgets here

#masterFrame.update()
screencenter(window)
#masterFrame.deiconify()
window.mainloop()