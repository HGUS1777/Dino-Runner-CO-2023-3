from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Element:
    SPEED_CLOUD = 1
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1100, 1150)

    def update(self,speed):
        self.rect.x -= self.SPEED_CLOUD
 
    def draw(self,screen):
        screen.blit(self.image,self.rect)