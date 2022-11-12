# Driver class drives the camera, GUI, and FrameProcessor. It gives FrameProcessor the frame, and receives
# the frame with skeletonization and the hands kinematics

import cv2
import mediapipe as mp
import numpy as np
from lib import FrameProcessor

class Driver:
	def __init__(self):
		self.introduction() 
		# initialize Pose estimator



	# Run the program by the input camera type 
	def run(self, camera_type):
		if camera_type == 'realsense':
			import pyrealsense2.pyrealsense2 as rs

			# Start a pipeline representing the bgr camera
			pipe = rs.pipeline()
			config = rs.config()
			config.enable_stream(rs.stream.color, rs.format.bgr8, 30)
			pipe.start(config)

		elif camera_type == 'kinect':
			from freenect import sync_get_depth as get_depth, sync_get_video as get_video
		else:
			print('Camera not supported')
		

	# Play the instrument based on the passed string arg
	def play_instrument(self, instrument):
		

	
	@staticmethod
	def introduction():
		print('Virtual Instrument starting.....')
		print('Please input camera type (realsense or kinect)')


driver = Driver()





