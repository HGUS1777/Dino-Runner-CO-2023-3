from dino_runner.components.element_bg.cloud import Cloud
import random

class ElementManager:
    FINAL = 200
    def __init__(self):
        self.element = []
        self.position = random.randint(200,500)
        self.position_1 = random.randint(200,300)
    def update(self,game_speed):

        if len(self.element) == 0:
            self.element.append(Cloud())
        if len(self.element) == 1 and self.element[0].rect.x < self.position:
            self.element.append(Cloud())
        
        for background in self.element:
            if background.rect.x < - self.FINAL:
                self.element.remove(background)
            background.update(game_speed)

    def draw(self,screen):
        for background in self.element:
            background.draw(screen)