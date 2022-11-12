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
elif (sys.platform == 'darwin'):
    import tkinter as tk


#  window for windows users
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

# 

title.pack()
instruList.pack()

# User
window.mainloop()