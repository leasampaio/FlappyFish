from tupy import Image, keyboard
from Animation import Animation

class Krappy(Image):
    def __init__(self, x, y):
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
    #     self._speed += self._gravity
    #     self.y += self._speed

    #     if keyboard.is_key_just_down('space'):
    #         self.jump()
