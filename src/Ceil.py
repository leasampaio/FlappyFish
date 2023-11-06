from tupy import Group, Image, keyboard

class Ceil(Image):
    def __init__(self, x):
        self.file = '../assets/ceil.png'
        self.x = x
        self.y = 0

        self._speed = 1
    
    def update(self):
        self.x -= self._speed
        if self.x < -600: self.x += 2*1080
        else: self.x -= self._speed
        
