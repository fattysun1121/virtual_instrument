# <<<<<<< HEAD
from tkinter import *
from tkinter import ttk 

# from Driver import Driver


'''
class GUI:
    def __init__(self, root):

        
        
        
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        camera_type_button = ttk.Button(root, padding="3 3 12 12", command=self.drop_down, text="Camera Type")
        camera_type_button.grid(column=2, row=0, sticky=(N, W, S, E))
        
		
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)


        ttk.Label(mainframe, text="Handstruments").grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text="Bongos").grid(column=1, row=2, sticky=(E, W))
        ttk.Button(mainframe, text="Theremin").grid(column=1, row=3, sticky=(E, W))


    def hi(self):
        print('haha')
    
    
    
    def drop_down(self):

        kinect_button = ttk.Button(root, text="kinect", padding="3 3 12 12").grid(column=2, row=1, sticky=(N))
        realsense_button = ttk.Button(root, text="real sense", padding="3 3 12 12").grid(column=2, row=2, sticky=(N))

'''

def drop_down():

    kinect_button = ttk.Button(root, text="kinect", padding="3 3 12 12").grid(column=2, row=1, sticky=(N))
    realsense_button = ttk.Button(root, text="real sense", padding="3 3 12 12").grid(column=2, row=2, sticky=(N))


root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

camera_type_button = ttk.Button(root, padding="3 3 12 12", command=drop_down, text="Camera Type")
camera_type_button.grid(column=2, row=0, sticky=(N, W, S, E))
        
		
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


ttk.Label(mainframe, text="Handstruments").grid(row=1, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Bongos",command=lambda : Driver().run('realsense', 'b')).grid(column=1, row=2, sticky=(W))
ttk.Button(mainframe, text="Theremin", command=lambda : Driver().run('realsense', 't')).grid(column=2, row=2, sticky=(E))






root.mainloop()
