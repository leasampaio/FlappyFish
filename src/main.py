from tupy import *
from BubbleFish import BubbleFish
from Background import Background
from Ceil import Ceil
from Floor import Floor
from Krappy import Krappy
from MaskFish import MaskFish

background = Background()
ceil1 = Ceil(0)
ceil2 = Ceil(1080)
floor1 = Floor(0)
floor2 = Floor(1080)
bubblefish = BubbleFish(200,200)
krappy = Krappy(400,100)
maskfish = MaskFish(400, 300)

run(globals())