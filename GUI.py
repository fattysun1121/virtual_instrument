'''
v0.2 - GUI

Cal Tumminello
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
    from tkinter import ttk
else:
    from enum import Enum
    from tkinter import Tk, Label, Frame, Toplevel, Canvas
    import tkinter as tk
    import tkinter.ttk as ttk


