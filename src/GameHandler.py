from tupy import *
from Status import Status
from Ceil import Ceil
from Floor import Floor
from BubbleFish import BubbleFish
from Score import Score
from Krappy import Krappy
from MaskFish import MaskFish
from random import randint

class GameHandler(Image):
    POINTS_RATE = 20

    def __init__(self):
        self.start()

    def start(self):
        self.x = -1000
        self.y = -1000
        self._background = Image('../assets/play.png', 500, 250)
        self._ceil = None
        self._floor = None
        self._player = None
        self._score = None
        self._enemies = []

        self._status = Status.START
        self._enemy_spawn_rate = 100

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if self.status == Status.START:
            self._background.destroy()
            self._background = Image('../assets/background.png', 500, 250)
            self._ceil = [Ceil(0), Ceil(1080)]
            self._floor = [Floor(0), Floor(1080)]
            self._player = BubbleFish(200,200)
            self._score = Score()
            self._status = Status.GAME
            self._counter = self._enemy_spawn_rate
            self._point_counter = 0
        elif self.status == Status.GAME:
             
            self._game_over=Image('../assets/game_over.png', 500, 200)
            self._game_over=Image('../assets/press_space.png', 500, 300)
            self._status = Status.GAME_OVER
            self._player.status = Status.GAME_OVER
            self._ceil[0].status = Status.GAME_OVER
            self._ceil[1].status = Status.GAME_OVER
            self._floor[0].status = Status.GAME_OVER
            self._floor[1].status = Status.GAME_OVER

            for enemy in self._enemies:
                enemy.status = Status.GAME_OVER

        elif self.status == Status.GAME_OVER:
           self.start()


    def update(self):
        if self.status == Status.START:
            if keyboard.is_key_just_down('space'):
                self.status = Status.GAME
                 

        elif self.status == Status.GAME:
            self._counter += 1
            self._point_counter += 1

            # spawn an enemy every self._enemy_spawn_rate frames
            # 1:4 - Mask Fish
            # 5 - Krappy
            if self._counter >= self._enemy_spawn_rate:
                if self._enemy_spawn_rate >= 30:
                    self._enemy_spawn_rate -= 10
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
                    self.status = Status.GAME_OVER
                    

            # increase one point for every POINTS_RATE frames
            if self._point_counter >= GameHandler.POINTS_RATE:
                self._point_counter -= GameHandler.POINTS_RATE
                self._score.increase()

        elif self.status == Status.GAME_OVER:
                if keyboard.is_key_just_down('space'):
                    self.status = Status.GAME