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
    import tkinter as tk
    import tkinter.ttk as ttk
else:
    from enum import Enum
    from tkinter import Tk, Label, Frame, Toplevel
    import tkinter as tk





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


class InstrumentWindow(tk.Tk):


    def __init__(self) -> None:
        super().__init__()
        self.instrument = Instruments.BONGOS

        
        self.Btn_list = []

        # self.instruList = tk.Listbox(bg='gray')
        bongoBut = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        bongoBut.grid(row=0,column=0)
        self.Btn_list.append(bongoBut)

        # self.instruList.insert(1, "Bongos")
        guitarBut = tk.Button(text="Guitar", width=10, height=5, fg="white", bg="gray")
        guitarBut.grid(row=1,column=0)
        self.Btn_list.append(bongoBut)

        # self.instruList.insert(2, "Guitar")
        thereminBut = tk.Button(text="Theremin", width=10, height=5, fg="white", bg="gray")
        thereminBut.grid(row=2, column=0)
        self.Btn_list.append(bongoBut)

        self.setGrid(5)
        # self.instruList.insert(3, "Theremin")
        


    def setInstrument(self, instru):
        self.instrument = instru

    def getInstrument(self) -> Instruments:
        return self.instrument

    def setGrid(self, factor):
        x = 0
        y = 0

        label1 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label2 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label3 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label4 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label5 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label6 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label7 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label8 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label9 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")
        label10 = tk.Button(text="Bongos", width=10, height=5, fg="white", bg="gray")

        label1.grid(row=0, column=0)
        label2.grid(row=1,column=0)
        label3.grid(row=2, column=0)
        label4.grid(row=3,column=0)
        label5.grid(row=4, column=0)


        label6.grid(row=0,column=0)
        label7.grid(row=0, column=1)
        label8.grid(row=0,column=2)
        label9.grid(row=0, column=3)
        label10.grid(row=0,column=4)




        '''
        while x < factor:

            label.grid(row=x,column=0)

            while y < factor:

                label.grid(row=0,column=y)

                label = tk.Label(text=" ", bg="gray")
                y = y +1
        x = x + 1
        '''



# Creates the Window for instruments, master window for all calculations

window = InstrumentWindow()




WINDOW_HEIGHT = window.winfo_height()

WINDOW_WIDTH = window.winfo_width()




'''
----------SHIT I PULLED FROM STACK OVERFLOW TO SHOW CAMERA FEED-----------


# Create a frame

# Create a label in the frame
lmain = tk.Label(window)
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

'''
-------------------------------------------------------------------------------
'''

screen = InstrumentWindow()



'''
Widgets
'''

title = tk.Label(text="Instruments", foreground="white", background="gray")

# Basic buttons
startButton = tk.Button(width=10)
stopButton = tk.Button(width=10)
recordButton = tk.Button(width=10)

# instruList.pack()

#


# instruList.pack()

# User
window.mainloop()