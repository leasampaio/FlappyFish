from tupy import *
from Status import Status


class Floor(Image):
    def __init__(self, x: int) -> None:
        self.file = "../assets/floor.png"
        self.x = x
        self.y = 430
        self._speed = 3
        self._status = Status.GAME

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        self._status = value

    def update(self) -> None:
        if self._status == Status.GAME:
            self.x -= self._speed
            if self.x < -600:
                self.x += 2 * 1080
            else:
                self.x -= self._speed
