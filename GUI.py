from tkinter import *
from tkinter import ttk 
from Driver import Driver

class GUI:
	def __init__(self, root):
		mainframe = ttk.Frame(root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		ttk.Label(mainframe, text="Handstruments").grid(row=1, columnspan=2, sticky=(W, E))
		ttk.Button(mainframe, text="Bongos").grid(column=1, row=2, sticky=(W))
		ttk.Button(mainframe, text="Theremin").grid(column=2, row=2, sticky=(E))

	def hi(self):
		print('haha')
 
root = Tk()
root.title("Handstruments")
gui = GUI(root)
root.mainloop()
