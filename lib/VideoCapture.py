import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import pyrealsense2.pyrealsense2 as rs



root = Tk()
root.title("Camera Feed")

pipe = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipe.start(config)

cap = cv2.VideoCapture(0)

#Graphics window
imageFrame = ttk.Frame(root, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = ttk.Label(imageFrame)
lmain.grid(row=0, column=2)

# Define function to show frame
def show_feed():
    frames = pipe.wait_for_frames()
    color = frames.get_color_frame()
    # Get the latest frame and convert into Image
    color_array = np.asanyarray(color.get_data())
    cv2image= cv2.cvtColor(color_array, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(cv2image)

    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_feed)

# Repeat after an interval to capture continiously
lmain.after(20, show_feed)

quit_btn = ttk.Button(root, text="Quit", command=root.destroy).grid(row=1, column=2, stick=S)


    

root.mainloop()


