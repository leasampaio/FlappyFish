from tupy import Image, keyboard
from Animation import Animation
from math import cos, pi


class MaskFish(Image):
    def __init__(self, d: int = 0) -> None:
        self._animation_move = Animation(
            [
                "../assets/mask-fish/move_0.png",
                "../assets/mask-fish/move_1.png",
                "../assets/mask-fish/move_2.png",
                "../assets/mask-fish/move_3.png",
                "../assets/mask-fish/move_4.png",
                "../assets/mask-fish/move_5.png",
            ]
        )
        self.x = 1100
        self.file = self._animation_move.file()

        self._speed = 5
        self._A = 170
        self._w = 0.03 * pi
        self._d = d
        self._counter = 1

        self._status = "playing"

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        self._status = value

    def update(self) -> None:
        self.file = self._animation_move.file()
        if self._status == "playing":
            self.x -= self._speed
            self.y = 250 + self._A * cos(self._w * self._counter + self._d)
            self._counter += 1
