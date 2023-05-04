from dino_runner.components.background.Background import Background
from dino_runner.utils.constants import CLOUD
import random

class Cloud(Background):
    def __init__(self):
        self.image = CLOUD
        super().__init__(self.image)
        self.rect.y = random.randint(20, 280)