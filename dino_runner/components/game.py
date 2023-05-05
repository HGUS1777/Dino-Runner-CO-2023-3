import pygame

from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICONS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,GAMEOVER,RESET,JUMPING
from dino_runner.components.dinosaur import Dinosaur
'''from dino_runner.components.cloud import Cloud'''
from dino_runner.components.obstacles.obstacle_manager import ObstacleMnager  
from dino_runner.components import text_util
from dino_runner.components.element_bg.element_manager import ElementManager

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
        self.obstacle_Manager = ObstacleMnager()
        self.power_up_manager = PowerUpManager()
        self.element_manager = ElementManager()
        self.points = 0
        self.death_count = 0
        self.night_min = 500
        self.night_max = 1000
        self.max_score_list = [0]

    def point(self): #metodo que muestra los puntos en pantalla y aumenta la velocidad del juego
        score, score_text = text_util.get_message_points(self.night_min,self.night_max,self.points,"Points: "+str(self.points),20,1000,40)
        self.screen.blit(score,score_text)

        if self.points % 100 == 0: # cada 100 puntos 
            self.game_speed += 1 #aumenta la velocidad del juego en 1 
        

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
            self.element_manager.update(self.game_speed)
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1
                if self.points > self.max_score_list[0]:
                    self.max_score_list.insert(0,self.points)
            if self.points > self.night_max:
                self.night_min += 1000
                self.night_max += 1000

    def powers(self):
        if self.player.shield:
            score, score_text = text_util.get_message_points(self.night_min,self.night_max,self.points,"Shield: "+str(self.player.time_to_show),20,1000,100)
            return self.screen.blit(score,score_text)
        if self.player.hammer:
            score, score_text = text_util.get_message_points(self.night_min,self.night_max,self.points,"Hammer: "+str(self.player.time_to_show),20,1000,100)
            return self.screen.blit(score,score_text)  
        
    def draw(self):
        if self.playing:#cuando se esta jugando
            self.clock.tick(FPS)
            if self.points > self.night_min and self.points < self.night_max:
                self.screen.fill((0, 0, 0))
            else:
                self.screen.fill((255, 255, 255))
                
            self.draw_background()
            self.element_manager.draw(self.screen)#muestra los elementos decorativos del fondo en el game
            self.obstacle_Manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            self.powers() 
            self.point() #se llama metodo para mostrar puntos en pantalla
            self.player.draw(self.screen)

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
            self.screen.blit(JUMPING, (500, 160))
            text,text_rect = text_util.get_message('Press any key to start', 30)
            self.screen.blit(text, text_rect)

        else:
            self.screen.blit(GAMEOVER, (357, 200))
            self.screen.blit(RESET, (512.5, 400))
            text,text_rect = text_util.get_message('Press any key to Restart', 30)
            score,score_rect = text_util.get_message('Your score: '+str(self.points), 30,height = SCREEN_HEIGHT//2 + 50)
            maxscore,listmaxscore = text_util.get_message('Max Score: '+str(self.max_score_list[0]),20,950,40 )
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)
            self.screen.blit(maxscore,listmaxscore)
    
    def reset_game(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_Manager = ObstacleMnager()
        self.power_up_manager = PowerUpManager()
        self.element_manager = ElementManager()
        self.points = 0

