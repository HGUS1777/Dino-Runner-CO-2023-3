import pygame

from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleMnager  


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud(1,0,1080)
        self.cloud_1 = Cloud(1,0,1380)
        self.cloud_2 = Cloud(1.5,1,1280)
        self.cloud_3 = Cloud(1.5,2,1980)
        self.obstacle_Manager = ObstacleMnager()
        self.power_up_manager = PowerUpManager()
        self.points = 0

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.points += 1
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        self.obstacle_Manager.update(self.game_speed,self.player)
        if self.player.dino_dead:
            self.playing = False
            
            
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud.new_cloud_low(self.screen)
        self.cloud_1.new_cloud_low(self.screen)
        self.cloud_2.new_cloud_high(self.screen)
        self.cloud_3.new_cloud_high(self.screen)
        self.obstacle_Manager.draw(self.screen)
        self.player.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed