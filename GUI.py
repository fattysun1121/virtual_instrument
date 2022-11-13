from tkinter import *
from tkinter import ttk 


root = Tk()

camera_type_list = ["kinect", "real sense"]

instrument_type_list = ["Bongos", "Theremin"]



camera_choice = StringVar()
camera_choice.set(camera_type_list[0])

instrument_choice = StringVar()
instrument_choice.set(camera_type_list[0])


camera_menu = ttk.Combobox(root, value=camera_type_list)
instrument_menu = ttk.Combobox(root, value=instrument_type_list)


title = Label(root, text="Handstruments", font=("Times New Roman", 25)).grid(row=0, column=1)

Label(root,text="instrument menu").grid(row=0, column=1, sticky=(S))

camera_menu.grid(column=0, row=1, sticky=(N))
instrument_menu.grid(column=2, row=1)

row4 = Label(root, height=3).grid(row=4, column=2)
row5 = Label(root, height=3).grid(row=5, column=2)
row6 = Label(root, height=3).grid(row=6, column=2)


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

		
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="Handstruments").grid(column=1, row=1, sticky=(N, W, E, S))
ttk.Button(mainframe, text="Bongos").grid(column=1, row=2, sticky=(E, W))
ttk.Button(mainframe, text="Theremin").grid(column=1, row=3, sticky=(E, W))





root.title("Handstruments")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



root.mainloop()
