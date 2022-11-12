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

from PIL import ImageTk, Image

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
    from tkinter import Tk, Label, Frame, Toplevel
    import tkinter as tk

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
    def __init__(self, instru) -> None:
        super().__init__()

        self.instrument = instru
        self.instruList = tk.Listbox(bg='gray')
        bongoBut = tk.Button(text="Bongos", width=10, height=10, fg="white", bg="gray")
        self.instruList.insert(1, "Bongos")
        guitarBut = tk.Button(text="Guitar", width=10, height=10, fg="white", bg="gray")
        self.instruList.insert(2, "Guitar")
        thereminBut = tk.Button(text="Theremin", width=10, height=10, fg="white", bg="gray")
        self.instruList.insert(3, "Theremin")
        


    def setInstrument(self, instru):
        self.instrument = instru

    def getInstrument(self) -> Instruments:
        return self.instrument


'''
----------SHIT I PULLED FROM STACK OVERFLOW TO SHOW CAMERA FEED-----------
'''

# Create a frame

# Create a label in the frame
lmain = Label(window)
lmain.grid()

# Capture from camera
cap = cv2.VideoCapture(0)

def video_stream():
    
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

video_stream()
'''
-------------------------------------------------------------------------------
'''

screen = InstrumentWindow(Instruments.BONGOS)



'''
Widgets
'''

title = Label(text="Instruments", foreground="white", background="gray")

# Basic buttons
startButton = tk.Button(width=10)
stopButton = tk.Button(width=10)
recordButton = tk.Button(width=10)

# instruList.pack()

#


# instruList.pack()

# User
window.mainloop()