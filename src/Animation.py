class Animation:
    def __init__(self, sprites: list[str], refresh_rate: int = 5):
        self._sprites = sprites
        self._refresh_rate = refresh_rate
        self._counter = 0
        self._state = 0
    
    def file(self):
        if self._counter < self._refresh_rate:
            self._counter += 1
        else:
            self._counter = 0
            self._state += 1
            self._state %= len(self._sprites)
        return self._sprites[self._state]

    def reset(self):
        self._counter = 0
        self._state = 0
