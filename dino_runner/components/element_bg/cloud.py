from dino_runner.components.element_bg.element import Element
from dino_runner.utils.constants import CLOUD
import random

class Cloud(Element):
    def __init__(self):
        self.image = random.choice(CLOUD)
        super().__init__(self.image)
        self.rect.y = random.randint(20, 290)