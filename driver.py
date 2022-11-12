# Driver class drives the camera, GUI, and FrameProcessor. It gives FrameProcessor the frame, and receives
# the frame with skeletonization and the hands kinematics

import cv2
import mediapipe as mp
import numpy as np
from lib import FrameProcessor as fp

class Driver:
	def __init__(self):
		self.introduction() 
		self.processor = fp.FrameProcessor()


	# Run the program by the input camera type 
	def run(self, camera_type):
		if camera_type == 'realsense':
			import pyrealsense2.pyrealsense2 as rs

			# Start a pipeline representing the bgr camera
			pipe = rs.pipeline()
			config = rs.config()
			config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
			pipe.start(config)

			while True:
				# Get BGR frame
			    frames = pipe.wait_for_frames()
			    color = frames.get_color_frame()

			    if not color: continue

			    color_array = np.asanyarray(color.get_data())
			    

			    self.processor.process_frame(color_array)
			    
			    # show the final output
			    cv2.imshow('Output', color_array)
			    
			    if cv2.waitKey(1) == ord('q'):
			        break

			pipe.stop()

		elif camera_type == 'kinect':
			from freenect import sync_get_depth as get_depth, sync_get_video as get_video
		else:
			print('Camera not supported')
		
 
	# Play the instrument based on the passed string arg
	def play_instrument(self, instrument):
		pass
	
	@staticmethod
	def introduction():
		print('Virtual Instrument starting.....')
		print('Please input camera type (realsense or kinect)')


driver = Driver()
driver.run('realsense')





