'''
v0.2 - GUI

Cal Tumminello
'''

# import tkinter as tk
import sys

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
    from tkinter import *
    from tkinter.ttk import *
else:
    from enum import Enum
    from tkinter import Tk, Label, Frame, Toplevel, Canvas
    import tkinter as tk
    import tkinter.ttk as ttk

# enumeration for instrument type
class Instruments(Enum):

    BONGOS = 1
    THERAMIN = 2
    COMPOSER = 3

# Capture from camera
feed = 0
cap = cv2.VideoCapture(feed)

# Sets up User Interface
class InstrumentWindow(tk.Tk):
    def __init__(self, instru=1, master=None):
        super().__init__(master)
        self.instrument = instru
        # self.geometry(f'{WIDTH}x{HEIGHT}')
        #canvas = Canvas(master, width=WIDTH, height=HEIGHT)

        # Rows
        row1 = tk.Label(master, bg='pink', text= ' ').grid(row=0, column=0)
        row2 = tk.Label(master, bg='light gray', text= ' ').grid(row=1, column=0)
        row3 = tk.Label(master, bg='pink', text= ' ').grid(row=2, column=0)
        row4 = tk.Label(master, bg='light gray', text= ' ').grid(row=3, column=0)
        row5 = tk.Label(master, bg='pink', text= ' ').grid(row=4, column=0)

        # Columns
        
        col1 = tk.Label(master, bg='pink', text= ' ').grid(row=0, column=0)
        col2 = tk.Label(master, bg='light gray', text= ' ').grid(row=0, column=1)
        col3 = tk.Label(master, bg='pink', text= ' ').grid(row=0, column=2)
        col4 = tk.Label(master, bg='light gray', text= ' ').grid(row=0, column=3)
        col5 = tk.Label(master, bg='pink', text= ' ').grid(row=0, column=4)
        
        
        title = tk.Label(master, bg='light gray', text= 'Handstruments', font=("Times New Roman", 25)).grid(row=0, column=2)
        
        instruButt = tk.Button(master, text='Instruments', padx=50, pady=20).grid(row=3, column=0)
    
    def setInstrument(self, instru):
        self.instrument = instru

    def getInstrument(self):
        print(f'{self.instrument}')
        

# function to center screen 
def screencenter(o):
    w, h = o.winfo_width(), o.winfo_height()
    x = int((o.winfo_screenwidth() - w) / 2)
    y = int((o.winfo_screenheight() - h) / 2)
    o.geometry(f'{w}x{h}+{x}+{y}')       


# Widgets here
window = InstrumentWindow()

#masterFrame.update()
#screencenter(masterFrame)
#masterFrame.deiconify()
window.mainloop()