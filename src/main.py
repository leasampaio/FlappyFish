from tupy import *
from BubbleFish import BubbleFish
from Background import Background
from Ceil import Ceil
from Floor import Floor
from Krappy import Krappy
from MaskFish import MaskFish
from tubarao import Tubarao
from Score import Score
from GameHandler import GameHandler

class Play(Image):
    
    def update(self) -> None:
    
        
        if keyboard.is_key_just_down('space'):
            
            background = Background()
            ceil1 = Ceil(0)
            ceil2 = Ceil(1080)
            floor1 = Floor(0)
            floor2 = Floor(1080)    
            score = Score()        
            bubblefish = BubbleFish(200,200)
            krappy = Krappy(400,100)
            tubarao = Tubarao(940,250)
            maskfish = MaskFish(400)
            gamehandler = GameHandler()
            

play = Play ('play.png')


play.x = 500
play.y = 250
run(globals())
