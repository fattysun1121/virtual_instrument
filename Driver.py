# Driver class drives the camera, the instruments, and FrameProcessor. It gives FrameProcessor the frame, and receives
# the frame with skeletonization and the hands kinematics

# Local libraries
from lib.Bongos import Bongos
from lib.Theremin import Theremin
from lib import FrameProcessor as fp

# Image processing
import cv2
import mediapipe as mp
import numpy as np

# Theremin dependencies
import pygame
import signal
import sys

# tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

keep_running = True

class Driver:
	def __init__(self):
		self.introduction() 
		self.processor = fp.FrameProcessor()
		self.instruments = {'b': Bongos(), 't': Theremin()}


		root = Tk()
		root.title("Camera Feed")
		#Graphics window
		imageFrame = ttk.Frame(root, width=600, height=500)
		imageFrame.grid(row=0, column=0, padx=10, pady=2)

		#Capture video frames
		lmain = ttk.Label(imageFrame)
		lmain.grid(row=0, column=2)

		# Quit buttom
		quit_btn = ttk.Button(root, text="Quit", command=root.destroy).grid(row=1, column=2, stick=S)

		self.lmain = lmain
		self.root = root

	# Run the program by the input camera type 

	def run(self, camera_type, instrument):
		lmain = self.lmain
		if camera_type == 'realsense':
			import pyrealsense2.pyrealsense2 as rs

			# Start a pipeline representing the bgr camera
			self.pipe = rs.pipeline()
			config = rs.config()
			config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 60)
			self.pipe.start(config)
			# Repeat after an interval to capture continiously
			self.show_feed(instrument)
			

		elif camera_type == 'kinect':
			from freenect import sync_get_depth as get_depth, sync_get_video as get_video

			self.update_frame_k(instrument)
			

		else:
			print('Camera not supported!')
	
	def show_feed(self, instrument):
		lmain = self.lmain
		frames = self.pipe.wait_for_frames()
		color = frames.get_color_frame()
		# Get the latest frame and convert into Image
		color_array = np.asanyarray(color.get_data())
		if self.processor.process_frame(color_array) == 0:
			lhand, rhand = self.processor.get_kinematics()
			self.instruments[instrument].play(lhand, rhand)
		cv2image= cv2.cvtColor(color_array, cv2.COLOR_BGR2RGB)

		img = Image.fromarray(cv2image)

		# Convert image to PhotoImage
		imgtk = ImageTk.PhotoImage(image = img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.after(17, lambda : self.show_feed(instrument))

	def update_frame_k(self, instrument):
		lmain = self.lmain
		(depth,_), (rgb,_) = get_depth(), get_video()

		self.processor.process_frame(rgb)

		cv2.imshow('Output', rgb[:, :, ::-1])

		lhand, rhand = self.processor.get_kinematics()

		self.instruments[instrument].play(lhand, rhand)
		cv2image= cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)

		img = Image.fromarray(cv2image)

		# Convert image to PhotoImage
		imgtk = ImageTk.PhotoImage(image = img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.after(17, lambda : self.update_frame_k(instrument))


	
	@staticmethod
	def introduction():
		print('Virtual Instrument starting.....')
		print('Please input camera type (realsense or kinect)')

def handler(signum, frame):
	global keep_running
	keep_running = False


d = Driver()
d.run('realsense', 'b')
d.root.mainloop()




