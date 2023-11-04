from tupy import Image, keyboard

class Floor(Image):
    def __init__(self, x):
        self.file = '../assets/floor.png'
        self.x = x
        self.y = 380

        self._speed = 1
    
    def update(self):
        self.x -= self._speed
        if self.x < -600: self.x += 2*1080
        else: self.x -= self._speed