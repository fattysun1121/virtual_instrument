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
    import tkinter as tk
    from tkinter import Toplevel
elif (sys.platform == 'darwin'):
    import tkinter as tk
    from tkinter import Toplevel
    from enum import Enum
    from tkinter import Frame
# enumeration for instrument type

class instruments(Enum):

    BONGOS = 1
    THERAMIN = 2
    COMPOSER = 3


    



# toplevel controller for window groups

top = Toplevel(bg="black", fg="white", )


#  window for windows users

class InstrumentWindow(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.instrument = None
        self.




window = tk.Tk()



'''
Widgets
'''

title = tk.Label(text="Instruments")

# Basic buttons
startButton = tk.Button()
stopButton = tk.Button()
recordButton = tk.Button()

# List box buttons
instruList = tk.Listbox(bg='gray')
instruList.insert(1, "Bongos")
instruList.insert(2, "Guitar")
instruList.insert(3, "Theremin")

instruList.pack()

# 

title.pack()
instruList.pack()

# User
window.mainloop()