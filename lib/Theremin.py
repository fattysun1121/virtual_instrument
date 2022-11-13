from .Instrument import Instrument
import numpy as np
import pygame
import math


class Theremin():
    def __init__(self):
        self.pitch_rod_x = 0.7
        self.pitch_rod_z = 0.7
        self.vol_rod_y   = 0.7
    
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
        pitch_scale = self.__calc_pitch_linear_distance(rhand[0][0], rhand[0][2])
        print(pitch_scale)