import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS

class Cactus(Obstacle):
    Y_POS_SMALL_CACTUS = 325
    Y_POS_LARGE_CACTUS = 302
    def __init__(self):
        counter_type_cactus = random.randint(1,2)
        if counter_type_cactus == 1:
            self.image = random.choice(SMALL_CACTUS)
            self.y = self.Y_POS_SMALL_CACTUS
        if counter_type_cactus == 2:
            self.image = random.choice(LARGE_CACTUS)
            self.y = self.Y_POS_LARGE_CACTUS
        super().__init__(self.image)
        self.rect.y = self.y

