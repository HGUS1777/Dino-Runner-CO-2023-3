import pygame
from dino_runner.utils.constants import BIRD
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle:

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self, game_speed, player):
        if self.image == BIRD[0] or self.image == BIRD[1]:
            self.image = BIRD[0] if self.step_index < 5 else BIRD[1] 
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0

        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            player.dead()
            pygame.time.delay(2000)
            player.dino_dead = True

            
