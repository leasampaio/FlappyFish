from tupy import Image


class Background(Image):
    def __init__(self) -> None:
        self.file = "../assets/background.png"
        self.x = 500
        self.y = 250
