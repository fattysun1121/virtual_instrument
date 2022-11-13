from tkinter import *
from tkinter import ttk 
from Driver import Driver


root = Tk()
root.title("Handstruments")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Handstruments").grid(row=1, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Bongos",command=lambda : Driver().run('realsense', 'b')).grid(column=1, row=2, sticky=(W))
ttk.Button(mainframe, text="Theremin", command=lambda : Driver().run('realsense', 't')).grid(column=2, row=2, sticky=(E))

root.mainloop()
