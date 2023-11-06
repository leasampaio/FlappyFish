from tupy import Image, keyboard

class Floor(Image):
    def __init__(self, x):
        self.file = '../assets/floor.png'
        self.x = x
        self.y = 430

        self._speed = 3
        self._status = 'playing'

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
    
    def update(self):
        if self._status == 'playing':
            self.x -= self._speed
            if self.x < -600: self.x += 2*1080
            else: self.x -= self._speed