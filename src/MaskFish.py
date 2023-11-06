from tupy import Image, keyboard
from Animation import Animation
from math import cos, pi

class MaskFish(Image):
    def __init__(self, x):
        self._animation_move = Animation([
            '../assets/mask-fish/move_0.png',
            '../assets/mask-fish/move_1.png',
            '../assets/mask-fish/move_2.png',
            '../assets/mask-fish/move_3.png',
            '../assets/mask-fish/move_4.png',
            '../assets/mask-fish/move_5.png'
        ])
        self.x = x
        self.file = self._animation_move.file()

        self._speed = 2
        self.A = 130
        self.w = 0.05*pi
        self.counter = 1

    def update(self):
        self.file = self._animation_move.file()
        self.x -= self._speed
        self.y = 250 + self.A * cos(self.w*self.counter)
        self.counter += 1
        if (self.x >= -80):
            self.x -= 1
        else:
            self.x = 940
