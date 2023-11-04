from tupy import Image, keyboard
from Animation import Animation

class MaskFish(Image):
    def __init__(self, x, y):
        self._animation_move = Animation([
            '../assets/mask-fish/move_0.png',
            '../assets/mask-fish/move_1.png',
            '../assets/mask-fish/move_2.png',
            '../assets/mask-fish/move_3.png',
            '../assets/mask-fish/move_4.png',
            '../assets/mask-fish/move_5.png'
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