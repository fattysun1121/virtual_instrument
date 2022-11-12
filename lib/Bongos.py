from .Instrument import Instrument 
from pydub import AudioSegment
from pydub import playback as pb
from threading import Thread

class Bongos(Instrument):
	def __init__(self):
		self.high_audio = AudioSegment.from_file("./sounds/Bongo_high.wav", format="wav")
		self.deep_audio = AudioSegment.from_file("./sounds/Bongo_deep.wav", format="wav")
		self.mixed_audio = self.high_audio.overlay(self.deep_audio)
		self.lplaying = 0
		self.rplaying = 0

	# Control which sound file to play (left hand or right hand)
	# Use accelaration and position to decide whether play sound or not
	def get_pitch(self, lhand, rhand):
		lhand_py = lhand[0][1]
		rhand_py = rhand[0][1]

		if lhand_py > 0.2 and lhand_py < 0.5:
			self.lplaying = 0

		if rhand_py > 0.2 and rhand_py < 0.5:
			self.rplaying = 0

		if self.lplaying == 0 and self.rplaying == 0 and lhand_py > 0.6 and rhand_py > 0.6:
			self.lplaying = 1
			self.rplaying = 1
			return 'left and right'



		if self.lplaying == 0 and lhand_py > 0.6:
			self.lplaying = 1
			return 'left'
		
	

		if self.rplaying == 0 and rhand_py > 0.6:
			self.rplaying = 1
			return 'right'

		



	# Use velocity before hitting area to decide the volume
	def get_volume(self):
		pass


	# Play bongos
	def play(self, lhand, rhand):
		hands = self.get_pitch(lhand, rhand)
		if hands == 'left':	
			
			t = Thread(target=pb.play, args=(self.high_audio,))
			t.start()
		elif hands == 'right':
			t = Thread(target=pb.play, args=(self.deep_audio,))
			t.start()		
		elif hands == 'left and right':
			t = Thread(target=pb.play, args=(self.mixed_audio,))
			t.start()		




