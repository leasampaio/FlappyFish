from tupy import *
from Status import Status
from Ceil import Ceil
from Floor import Floor
from BubbleFish import BubbleFish
from Score import Score
from Krappy import Krappy
from MaskFish import MaskFish
from random import randint
from typing import List, Union, Optional


class GameHandler(Image):
    POINTS_RATE = 20

    def __init__(self) -> None:
        self.x = -1000
        self.y = -1000
        self._ceil: List[Ceil] | None = None
        self._floor: List[Floor] | None = None
        self._player: BubbleFish | None = None
        self._score: Score | None = None
        self._enemies: List[Union[MaskFish, Krappy]] = []
        self._enemy_spawn_rate: int = 100
        self._background: Optional[Image] = None
        self._game_over: Optional[Image] = None
        self.start()

    def start(self) -> None:
        self._status: Status = Status.START
        self._background = Image("../assets/play.png", 550, 250)

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        # START -> GAME
        if self.status == Status.START:
            self._background.destroy() if self._background is not None else None
            self._background = Image("../assets/background.png", 500, 250)
            self._ceil = [Ceil(0), Ceil(1080)]
            self._floor = [Floor(0), Floor(1080)]
            self._player = BubbleFish(200, 200)
            self._score = Score()
            self._status = Status.GAME
            self._counter = self._enemy_spawn_rate
            self._point_counter = 0

        # GAME -> GAMEOVER
        elif self.status == Status.GAME:
            self._game_over = Image("../assets/game_over.png", 500, 200)
            # self._game_over=Image('../assets/press_space.png', 500, 300)
            self._status = Status.GAME_OVER
            if self._player is not None:
                self._player.status = Status.GAME_OVER
                if self._ceil is not None and self._floor is not None:
                    self._ceil[0].status = Status.GAME_OVER
                    self._ceil[1].status = Status.GAME_OVER
                    self._floor[0].status = Status.GAME_OVER
                    self._floor[1].status = Status.GAME_OVER

            for enemy in self._enemies:
                enemy.status = Status.GAME_OVER

        # GAMEOVER -> START
        elif self.status == Status.GAME_OVER:
            if self._player is not None:
                self._player._destroy()
                self._player = None
                for enemy in self._enemies:
                    enemy.destroy()
                self._enemies.clear()
                if (
                    self._ceil is not None
                    and self._floor is not None
                    and self._background is not None
                    and self._game_over is not None
                    and self._score is not None
                ):
                    self._ceil[0].destroy()
                    self._ceil[1].destroy()
                    self._ceil.clear()
                    self._floor[0].destroy()
                    self._floor[1].destroy()
                    self._floor.clear()
                    self._game_over.destroy()
                    self._game_over = Image("../assets/play.png", 550, 250)
                    self._background.destroy()
                    self._background = Image("../assets/background.png", 500, 250)
                    self._score.destroy()
                    self._score = None
                    self.start()

    def update(self) -> None:
        if self.status == Status.START:
            if keyboard.is_key_just_down("space"):
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
                    speed = randint(10, 15)
                    self._enemies.append(Krappy(y, speed))
                else:
                    d = randint(0, 4)
                    self._enemies.append(MaskFish(d))

            # check each enemy
            for enemy in self._enemies:
                if self._player is not None:
                    if enemy.x <= -100:
                        enemy.destroy()
                        self._enemies.remove(enemy)
                    elif enemy._collides_with(self._player):
                        self.status = Status.GAME_OVER

            # increase one point for every POINTS_RATE frames
            if self._point_counter >= GameHandler.POINTS_RATE:
                self._point_counter -= GameHandler.POINTS_RATE
                if self._score is not None:
                    self._score.increase()

        elif self.status == Status.GAME_OVER:
            if keyboard.is_key_just_down("space"):
                self.status = Status.START
