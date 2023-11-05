from tupy import Image, keyboard
from Animation import Animation

class BubbleFish(Image):
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

        self._speed = 0
        self._GRAVITY = 2
        self._JUMP_SPEED = 10

        self._status = 'playing'
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
    
    def jump(self):
        self._speed = -self._JUMP_SPEED

    def update(self):
        if self.status == 'playing':
            self.file = self._animation.file()
            self.y += self._speed
            self._speed += self._GRAVITY
            if keyboard.is_key_down('space'):
                self.jump()
        else:
            self.file = '../assets/bubble-fish/hit1_0.png'
