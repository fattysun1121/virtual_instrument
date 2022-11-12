# Driver class drives the camera, GUI, and FrameProcessor. It gives FrameProcessor the frame, and receives
# the frame with skeletonization and the hands kinematics

import cv2
import mediapipe as mp
import numpy as np
import pygame
from lib import FrameProcessor as fp
from lib import Theremin as th
import signal
import sys

keep_running = True

class Driver:
	def __init__(self):
		self.introduction() 
		self.processor = fp.FrameProcessor()


	# Run the program by the input camera type 
	def run(self, camera_type):

		sampleRate = 44100
		freq = 300

		pygame.mixer.init(sampleRate, -16, 2, 512)

		arr = np.array([4096 * np.sin(2.0 * np.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(np.int16)
		arr2 = np.c_[arr, arr]
		sound = pygame.sndarray.make_sound(arr2)
		sound.play(-1)
		pygame.time.delay(1000)
		sound.stop()

		instr = th.Theremin()

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
		
 
	# Play the instrument based on the passed string arg
	def play_instrument(self, instrument):
		if instrument == 'b':
			from lib import Bongos
		elif instrument == 't':
			from lib import Theremin

	
	@staticmethod
	def introduction():
		print('Virtual Instrument starting.....')
		print('Please input camera type (realsense or kinect)')

def handler(signum, frame):
	global keep_running
	keep_running = False


<<<<<<< HEAD
driver = Driver()
driver.run('realsense')
=======
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: python driver.py [kinect | realsense]")
		pass
	signal.signal(signal.SIGINT, handler)
	driver = Driver()
	driver.run(sys.argv[1])
>>>>>>> f74d4295240178e38241daf99d53185a74e6ce61






