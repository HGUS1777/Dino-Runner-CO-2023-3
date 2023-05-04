import pygame

from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICONS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleMnager  
from dino_runner.components import text_util

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICONS)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False #estado para jugar
        self.running = False #estado para mostrar el menu
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
        self.font = pygame.font.SysFont(None,30) #EL número establece el tamaño del texto
        self.death_count = 0

    def point(self): #metodo que muestra los puntos en pantalla y aumenta la velocidad del juego
        score, score_text = text_util.get_message("Points: "+str(self.points),20,1000,40)
        self.screen.blit(score,score_text)
        if self.points % 100 == 0:
            self.game_speed += 1
        

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(2000)
        pygame.quit()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset_game()
                
    def update(self):
        if self.playing:
            self.points += 1
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.obstacle_Manager.update(self.game_speed, self.player, self.points)
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1
        
           
    def draw(self):
        if self.playing:#cuando se esta jugando
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.cloud.new_cloud_low(self.screen)
            self.cloud_1.new_cloud_low(self.screen)
            self.cloud_2.new_cloud_high(self.screen)
            self.cloud_3.new_cloud_high(self.screen)
            self.obstacle_Manager.draw(self.screen)
            self.point() #se llama metodo para mostrar puntos en pantalla
            self.player.draw(self.screen)
            self.power_up_manager.draw(self.screen)

        else:#cuando no se esta jugando
            self.draw_menu()
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

    def draw_menu(self):
        white_color = (255,255,255)
        self.screen.fill(white_color)
        if self.death_count == 0:
            text,text_rect = text_util.get_message('Press any key to start', 30)
            self.screen.blit(text, text_rect)
        else: 
            text,text_rect = text_util.get_message('Press any key to Restart', 30)
            score,score_rect = text_util.get_message('Your score: '+str(self.points), 30,height = SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)
    
    def reset_game(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_Manager = ObstacleMnager()
        self.power_up_manager = PowerUpManager()
        self.points = 0


        #COMO MINIMO TODAS LAS FUNCIOONALIDADES MAS LAS TAREAS AGREGADAS EN CLASE
        #MINIMO TRES FUNCIONALIDADES EXTRAS DEL CODIGO
        #CONTADOR DE PODER
        #MAXIMO SCORE
