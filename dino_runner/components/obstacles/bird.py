from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    Y_POS = 300
    def __init__(self):
        self.step_index = 0
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = self.Y_POS

        