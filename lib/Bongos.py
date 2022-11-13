from .Instrument import Instrument 
from pygame import mixer

class Bongos(Instrument):
	def __init__(self):
		self.lplaying = 0
		self.rplaying = 0

		mixer.init()

		self.high_sound = mixer.Sound("./sounds/Bongo_high.wav")
		self.deep_sound = mixer.Sound("./sounds/Bongo_deep.wav")
		self.mixed_sound = mixer.Sound("./sounds/Bongo_mixed.wav")

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

	# Play bongos
	def play(self, lhand, rhand):
		hands = self.get_pitch(lhand, rhand)

		if hands == 'left':	
			self.high_sound.stop()
			self.high_sound.play()
		elif hands == 'right':
			self.deep_sound.stop()
			self.deep_sound.play()	
		elif hands == 'left and right':
			self.mixed_sound.stop()
			self.mixed_sound.play()