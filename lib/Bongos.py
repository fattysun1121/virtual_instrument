from .Instrument import Instrument 
from pydub import AudioSegment
from pydub import playback as pb
import soundfile as sf


class Bongos(Instrument):
	def __init__(self):
		self.high_audio = AudioSegment.from_file("./sounds/Bongo_high.wav", format="wav")
		self.deep_audio = AudioSegment.from_file("./sounds/Bongo_deep.wav", format="wav")
		self.mixed_audio = self.high_audio.overlay(self.deep_audio)


	# Control which sound file to play (left hand or right hand)
	# Use accelaration and position to decide whether play sound or not
	def get_pitch(self):
		pass



	# Use velocity before hitting area to decide the volume
	def get_volume(self):
		pass

	# Play bongos
	def play(self, lhand, rhand):
		hands = self.get_pitch()
		if hands == 'left':
			pb.play(self.high_audio)
		elif hands == 'right':
			pb.play(self.deep_audio)
		elif hands == 'left and right':
			pb.play(self.mixed_audio)

b = Bongos()
b.play()

	
	