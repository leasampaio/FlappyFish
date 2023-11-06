from tupy import Image
from BubbleFish import BubbleFish
from random import randint
from Krappy import Krappy
from MaskFish import MaskFish
from Score import Score
from Ceil import Ceil
from Floor import Floor

class GameHandler(Image):
    POINTS_RATE = 60
    def __init__(self):
        self.x = -1000
        self.y = -1000

        self._enemy_spawn_rate = 100

        self._player = BubbleFish(200,200)
        self._score = Score()
        self._ceil = [Ceil(0), Ceil(1080)]
        self._floor = [Floor(0), Floor(1080)]
        self._enemies = []
        self._status = 'playing'
        self._counter = 100
        self._point_counter = 0

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if value == 'gameover':
            self._status = value
            self._player.status = value
            self._ceil[0].status = value
            self._ceil[1].status = value
            self._floor[0].status = value
            self._floor[1].status = value

            for enemy in self._enemies:
                enemy.status = value

    def update(self):
        if self._status == 'playing':
            self._counter += 1
            self._point_counter += 1

            # check collision with ceil/floor
            if self._player.y <= 70:
                self.status = 'gameover'
            elif self._player.y >= 430:
                self.status = 'gameover'

            # spawn an enemy every self._enemy_spawn_rate frames
            # 1:4 - Mask Fish
            # 5 - Krappy
            if self._counter >= self._enemy_spawn_rate:
                if self._enemy_spawn_rate >= 70:
                    self._enemy_spawn_rate -= 2
                self._counter -= self._enemy_spawn_rate
                i = randint(1, 5)
                if i < 5:
                    y = randint(100, 400)
                    speed = randint(10,15)
                    self._enemies.append(Krappy(y, speed))
                else:
                    d = randint(0, 4)
                    self._enemies.append(MaskFish(d))

            # check each enemy
            for enemy in self._enemies:
                if enemy.x <= -100:
                    enemy.destroy()
                    self._enemies.remove(enemy)
                elif enemy._collides_with(self._player):
                    self.status = 'gameover'
            
            # increase one point for every POINTS_RATE frames
            if self._point_counter >= GameHandler.POINTS_RATE:
                self._point_counter -= GameHandler.POINTS_RATE
                self._score.increase()
            
            
                
