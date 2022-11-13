from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGETEXT 
from PIL import ImageTk, Image
from Driver import Driver


root = Tk()
root.title("Handstruments")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Dropdown menu setup
camera_type_list = ["kinect", "realsense"]
instrument_type_list = ["Bongos", "Theremin"]

camera_choice = StringVar()
camera_choice.set(camera_type_list[0])

instrument_choice = StringVar()
instrument_choice.set(camera_type_list[0])


camera_menu = ttk.Combobox(root, value=camera_type_list, textvariable=camera_choice)
instrument_menu = ttk.Combobox(root, value=instrument_type_list, textvariable=instrument_choice)

instrument_choice.set(instrument_menu.get())
camera_choice.set(camera_menu.get())


# Title
Label(root, text="Handstruments", font=("Times New Roman", 25)).grid(row=0, column=1)

# Choices title
Label(root,text="Instrument Menu").grid(row=0, column=2, sticky=(S))
Label(root,text="Camera Menu").grid(row=0, column=0, sticky=(S))

camera_menu.grid(column=0, row=1, sticky=(N))
instrument_menu.grid(column=2, row=1, sticky=(N))

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

run_button = ttk.Button(root, text="Run", command=lambda : run(camera_choice, instrument_choice)).grid(column=1, row=2, sticky=(E, W))


# Bongos and theremin image setup
bongos_resize = Image.open("Bongos.PNG").resize(size=(100, 120))
theremin_resize = Image.open("theremin.PNG").resize(size=(100,120))
bongos_picture = ImageTk.PhotoImage(bongos_resize)
theremin_picture = ImageTk.PhotoImage(theremin_resize)
bongos_label = Label(root, image=bongos_picture, width=100, height=100)
theremin_label = Label(root, image=theremin_picture, width=100, height=100)
bongos_label.grid(row=5, column=0, sticky=(E))
theremin_label.grid(row=5,column=2, sticky=(W))

ttk.Button(root, text="Quit", command=root.destroy).grid(row=6, column=1, stick=S)

def run(camera, instrument):
    # Frame to hold the image label
    image_frame = ttk.Frame(root, width=600, height=500)
    image_frame.grid(row=5, column=1, padx=10, pady=2)

    # Label to hold the image
    image_holder = ttk.Label(image_frame)
    image_holder.grid(row=0, column=1)

    # Initiate and run driver 
    driver = Driver(image_holder)
    driver.run(camera, instrument)


root.mainloop()

