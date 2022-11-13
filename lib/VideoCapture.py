import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
'''
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
def Life_feed():
    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_COLOR)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Image saved!")
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
'''

root = Tk()
root.title("Camera Feed")
label = ttk.Label(root)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Graphics window
imageFrame = ttk.Frame(root, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = ttk.Label(imageFrame)
lmain.grid(row=0, column=2)


# Define function to show frame
def show_feed():
    # Get the latest frame and convert into Image
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)

    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_feed)
    
def take_video() -> bool:
    # This will return video from the first webcam on your computer.
    while(True):
        # loop runs if capturing has been initialized. 
        # reads frames from a camera 
        # ret checks return at each frame
        ret, frame = cap.read() 
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        # output the frame
        out.write(cv2image) 
    

def stop_video():
    out.release()
    cap.release()
    cv2.destroyAllWindows()

# Repeat after an interval to capture continiously
lmain.after(20, show_feed)
record_btn = ttk.Button(root, text='Record', command=take_video).grid(row=1, column=1, sticky=W)
quit_btn = ttk.Button(root, text="Quit", command=root.destroy).grid(row=1, column=2, stick=S)

if (take_video):
    stop_btn = ttk.Button(root, text='Stop', command=stop_video).grid(row=1, column=3, sticky=E)

root.mainloop()


