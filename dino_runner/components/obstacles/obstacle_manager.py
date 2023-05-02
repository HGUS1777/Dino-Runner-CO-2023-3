from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleMnager:
    def __init__(self):
        self.obstacles = []
        self.index = 0
        self.change = Cactus()
    def update(self,game_speed, player):
        if len(self.obstacles) == 0:
                self.obstacles.append(self.change)
        for obstacle in self.obstacles:
            if obstacle.rect.x < - obstacle.rect.width:
                self.obstacles.remove(obstacle)
                if self.index % 2 == 0:
                    self.change = Bird()
                    self.index += 1
                else:
                    self.change = Cactus()
                    self.index += 1
            obstacle.update(game_speed,player)
            
        print(self.index )
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            