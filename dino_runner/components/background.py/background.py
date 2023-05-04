from dino_runner.utils.constants import SCREEN_WIDTH

class Background:
    FINAL = -300
    SPEED_CLOUD = 1
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 1020

    def update(self, ):
        self.rect.x -= self.SPEED_CLOUD
 
    def draw(self,screen):
        screen.blit(self.image,self.rect)