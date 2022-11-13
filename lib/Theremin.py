from .Instrument import Instrument
import numpy as np
from pysinewave import SineWave
import math


class Theremin():
    def __init__(self):
        self.pitch_rod_x = 0.1
        self.pitch_rod_z = -0.8
        self.vol_rod_y   = 0.8
        self.sinewave = SineWave(pitch = 0, pitch_per_second = 10, decibels_per_second=10)
     
    def __calc_pitch_linear_distance(self, x, z):
        return math.sqrt(math.pow((x - self.pitch_rod_x), 2) + math.pow((z - self.pitch_rod_z), 2))
        
    def play(self, lhand, rhand):
        freq_scale = (math.exp(-1 * (10 / 3) * self.__calc_pitch_linear_distance(rhand[0][0], rhand[0][2])))
        dy = 100 * (self.vol_rod_y - lhand[0][1])
        if dy <= 0:
            self.sinewave.stop()
            return
        else:
            self.sinewave.play()

        self.sinewave.set_frequency(1500 * freq_scale)
        self.sinewave.set_volume(dy)
