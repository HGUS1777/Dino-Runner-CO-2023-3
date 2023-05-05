from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    Y_POS = 290
    def __init__(self,points):
        self.image = BIRD[0]
        self.y_pos = self.Y_POS
        if points > 500 and points < 800:   
            self.y_pos = 250
        elif points > 800: 
            self.y_pos = 210
            
        super().__init__(self.image)
        self.rect.y = self.y_pos