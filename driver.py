# Driver class drives the camera, GUI, and FrameProcessor. It gives FrameProcessor the frame, and receives
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

keep_running = True

class Driver:
	def __init__(self):
		self.introduction() 
		self.processor = fp.FrameProcessor()
		self.instruments = {'b': Bongos(), 't': Theremin()}

	# Run the program by the input camera type 
	def run(self, camera_type):

		if camera_type == 'realsense':
			import pyrealsense2.pyrealsense2 as rs

			# Start a pipeline representing the bgr camera
			pipe = rs.pipeline()
			config = rs.config()
			config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
			pipe.start(config)
			while keep_running:
				# Get BGR frame

				frames = pipe.wait_for_frames()
				color = frames.get_color_frame()

				color_array = np.asanyarray(color.get_data())
				


			    if self.processor.process_frame(color_array) == 0:
			    	lhand, rhand = self.processor.get_kinematics()
			    	self.instruments['b'].play(lhand, rhand)
			    
			    # Show the final output
			    cv2.imshow('Output', color_array)
			    
			    if cv2.waitKey(1) == ord('q'):
			        break


			pipe.stop()

		elif camera_type == 'kinect':
			from freenect import sync_get_depth as get_depth, sync_get_video as get_video

			while keep_running:
				(depth,_), (rgb,_) = get_depth(), get_video()

				self.processor.process_frame(rgb)

				cv2.imshow('Output', rgb[:, :, ::-1])

				rhand, lhand = self.processor.get_kinematics()

				instr.play(rhand, lhand)

				if cv2.waitKey(1) == ord('q'):
					break
		else:
			print('Camera not supported!')
	
	
	@staticmethod
	def introduction():
		print('Virtual Instrument starting.....')
		print('Please input camera type (realsense or kinect)')

def handler(signum, frame):
	global keep_running
	keep_running = False


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: python driver.py [kinect | realsense]")
	else:
		signal.signal(signal.SIGINT, handler)
		driver = Driver()
		driver.run(sys.argv[1])






