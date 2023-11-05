from tupy import Image, keyboard
from Animation import Animation

class Krappy(Image):
    def __init__(self, y, speed):
        self._animation_move = Animation([
            '../assets/krappy/move_0.png',
            '../assets/krappy/move_1.png',
            '../assets/krappy/move_2.png',
            '../assets/krappy/move_3.png',
            '../assets/krappy/move_4.png',
            '../assets/krappy/move_5.png',
            '../assets/krappy/move_6.png',
            '../assets/krappy/move_7.png',
            '../assets/krappy/move_8.png',
            '../assets/krappy/move_9.png',
            '../assets/krappy/move_10.png',
            '../assets/krappy/move_11.png',
            '../assets/krappy/move_10.png'
        ])
        self.x = 1100
        self.y = y
        self.file = self._animation_move.file()

        self._speed = speed

        self._status = 'playing'
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value

    def update(self):
        if self._status == 'playing':
            self.file = self._animation_move.file()
            self.x -= self._speed
