from pydub import AudioSegment
from pydub import playback as pb
from threading import Thread

high_audio = AudioSegment.from_file("../sounds/Bongo_high.wav", format="wav")


t = Thread(target=pb.play, args=(high_audio,))
t.start()