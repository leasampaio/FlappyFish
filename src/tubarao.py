from tupy import Image, keyboard
from Animation import Animation

class Tubarao(Image):
    def __init__(self, x, y):
        self._animation_move = Animation([
            '../assets/move_0.png',
           
        ])
        self.x = x
        self.y = y
        self.file = self._animation_move.file()

        self._speed = 5

    def update(self):
        self.file = self._animation_move.file()
        self.x -= self._speed

        if (self.x >= -80):
            self.x -= -1
        else:
            self.x = 940
