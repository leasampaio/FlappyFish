from tupy import *
from Animation import Animation
from Status import Status

class BubbleFish(Image):
    LIMIT_R = 920
    LIMIT_U = 50
    LIMIT_L = 50
    LIMIT_D = 430

    def __init__(self, x, y):
        self._animation = Animation([
            '../assets/bubble-fish/move_0.png',
            '../assets/bubble-fish/move_1.png',
            '../assets/bubble-fish/move_2.png',
            '../assets/bubble-fish/move_3.png',
            '../assets/bubble-fish/move_4.png',
            '../assets/bubble-fish/move_5.png'
        ])
        self.x = x
        self.y = y
        self.file = self._animation.file()

        self._speed = 10
        self._status = Status.GAME
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
    
    def update(self):
        if self.status == Status.GAME:
            self.file = self._animation.file()
            if keyboard.is_key_down('Right'):
                if self.x < BubbleFish.LIMIT_R: self.x += self._speed
            elif keyboard.is_key_down('Up'):
                if self.y > BubbleFish.LIMIT_U: self.y -= self._speed
            elif keyboard.is_key_down('Left'):
                if self.x > BubbleFish.LIMIT_L: self.x -= self._speed
            elif keyboard.is_key_down('Down'):
                if self.y < BubbleFish.LIMIT_D: self.y += self._speed
