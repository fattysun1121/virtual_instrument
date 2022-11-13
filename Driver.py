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

from PIL import ImageTk, Image


class Driver:
	def __init__(self, image_holder):
		self.processor = fp.FrameProcessor()
		self.instruments = {'Bongos': Bongos(), 'Theremin': Theremin()}	
		# Image_holder for each frame
		self.image_holder = image_holder

	# Run the program by the input camera type and instrument
	def run(self, camera_type, instrument):
		if camera_type == 'realsense':
			import pyrealsense2.pyrealsense2 as rs

			# Start a pipeline representing the bgr camera
			self.pipe = rs.pipeline()
			config = rs.config()
			config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 60)
			self.pipe.start(config)
		
			self.update_frame_r(instrument)
		elif camera_type == 'kinect':
			self.update_frame_k(instrument)
		else:
			print('Camera not supported!')
	
	def update_frame_r(self, instrument):
		# Get BGR frame from pipeline
		frames = self.pipe.wait_for_frames()
		color = frames.get_color_frame()

		# Get the data and convert into an array
		color_array = np.asanyarray(color.get_data())

		
		if self.processor.process_frame(color_array) == 0:
			lhand, rhand = self.processor.get_kinematics()
			self.instruments[instrument].play(lhand, rhand)

		cv2image= cv2.cvtColor(color_array, cv2.COLOR_BGR2RGB)

		img = Image.fromarray(cv2image)

		# Convert image to PhotoImage
		imgtk = ImageTk.PhotoImage(image=img)
		self.image_holder.imgtk = imgtk
		self.image_holder.configure(image=imgtk)
		self.image_holder.after(17, lambda : self.update_frame_r(instrument))

	def update_frame_k(self, instrument):
		from freenect import sync_get_depth as get_depth, sync_get_video as get_video
		(depth,_), (rgb,_) = get_depth(), get_video()

		if self.processor.process_frame(rgb) == 0:
			lhand, rhand = self.processor.get_kinematics()
			self.instruments[instrument].play(lhand, rhand)

		img = Image.fromarray(rgb)

		# Convert image to PhotoImage
		imgtk = ImageTk.PhotoImage(image=img)
		self.image_holder.imgtk = imgtk
		self.image_holder.configure(image=imgtk)
		self.image_holder.after(17, lambda : self.update_frame_k(instrument))
