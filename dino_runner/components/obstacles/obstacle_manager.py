from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleMnager:
    def __init__(self):
        self.obstacles = []
        self.index = 0
        self.change = Cactus()

    def update(self,game_speed, player, points):
        if len(self.obstacles) == 0:
                self.obstacles.append(self.change)
                print("aqui")

        for obstacle in self.obstacles:
            if player.destroyed:
                if len(self.obstacles) == 0:
                    self.obstacles.append(self.change)
    
                
                if obstacle.rect.colliderect(player.dino_rect) or obstacle.rect.x < - obstacle.rect.width:
                    self.obstacles.remove(obstacle)
                    
                    if self.index % 2 == 0 and points > 200 : #or points > 800:
                        self.change = Bird(points)
                        self.index += 1
                        '''elif points < 800:'''
                    else:
                        self.change = Cactus()
                        self.index += 1
            if not player.destroyed:
                if obstacle.rect.x < - obstacle.rect.width:
                    self.obstacles.remove(obstacle)
                    
                    if self.index % 2 == 0 and points > 200 :#or points > 800:
                        self.change = Bird(points)
                        self.index += 1
                        '''elif points < 800:'''
                    else:
                        self.change = Cactus()
                        self.index += 1
        
        obstacle.update(game_speed,player,points)
            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            