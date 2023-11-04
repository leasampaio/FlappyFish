from tupy import Image, keyboard
from Animation import Animation

class BubbleFish(Image):
    def __init__(self, x, y):
        self._animation_move = Animation([
            '../assets/bubble-fish/move_0.png',
            '../assets/bubble-fish/move_1.png',
            '../assets/bubble-fish/move_2.png',
            '../assets/bubble-fish/move_3.png',
            '../assets/bubble-fish/move_4.png',
            '../assets/bubble-fish/move_5.png'
        ])
        self.x = x
        self.y = y
        self.file = self._animation_move.file()

        self._speed = 0
        self._gravity = 0.2
        self._jump_speed = 10
    
    def jump(self):
        self._speed = -self._jump_speed

    def update(self):
        self.file = self._animation_move.file()
