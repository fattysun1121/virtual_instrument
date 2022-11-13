from .Instrument import Instrument
import numpy as np
from pysinewave import SineWave
import math


class Theremin():
    def __init__(self):
        self.pitch_rod_x = 0.1
        self.pitch_rod_z = -0.8
        self.vol_rod_y   = 0.8
        self.sinewave = SineWave(pitch = 0, pitch_per_second = 50, decibels_per_second=50)
            
    def get_pitch(self, lhand, rhand):
        sampleRate = 44100
        freq = 300

        pygame.mixer.init(sampleRate, -16, 2, 512)

        arr = np.array([4096 * np.sin(2.0 * np.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(np.int16)
        arr2 = np.c_[arr, arr]
        sound = pygame.sndarray.make_sound(arr2)
        sound.play(-1)
        pygame.time.delay(1000)
        sound.stop()
        pass

    def __calc_pitch_linear_distance(self, x, z):
        return math.sqrt(math.pow((x - self.pitch_rod_x), 2) + math.pow((z - self.pitch_rod_z), 2))

    def get_volume(self):
        pass

    def play(self, rhand, lhand):
        freq_scale = (math.exp(-1 * (10 / 3) * self.__calc_pitch_linear_distance(rhand[0][0], rhand[0][2])))
        dy = 100 * (self.vol_rod_y - lhand[0][1])
        if dy <= 0:
            self.sinewave.stop()
            return
        else:
            self.sinewave.play()
        print(f"X: {freq_scale:.3f}\tLeft Hand y: {dy:.3f}")

        self.sinewave.set_frequency(2000 * freq_scale)
        self.sinewave.set_volume(dy)

        # sampleRate = 44100
        # freq = 300 * pitch_scale

        # pygame.mixer.init(sampleRate, -16, 2, 512)

        # arr = np.array([(4096 * dy * 5) * np.sin(2.0 * np.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(np.int16) 
        # arr2 = np.c_[arr, arr]
        # sound = pygame.sndarray.make_sound(arr2)
        # sound.play(-1)
        # pygame.time.delay(100)
        # sound.stop()