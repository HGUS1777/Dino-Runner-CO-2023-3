import random
from dino_runner.utils.constants import CLOUD
#from dino_runner.components.background.Background import Background

class Cloud():
    FINAL = -300
    def __init__(self,speed_cloud,type_cloud,x_pos_cloud):
        self.image_cloud = CLOUD[type_cloud]
        self.speed_cloud = speed_cloud
        self.x_pos_cloud = x_pos_cloud
        self.y_pos_cloud = random.randint(220, 280)
        self.y_pos_cloud_high = random.randint(50, 100)
        #super().__init__(self):
            
    def new_cloud_low(self,screen):
        image_width_cloud_1 = self.image_cloud.get_width() 
        screen.blit(self.image_cloud, (image_width_cloud_1 + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= self.FINAL:
            screen.blit(self.image_cloud, (image_width_cloud_1 + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = random.randint(1010,1180)
            self.y_pos_cloud = random.randint(210, 300)
        self.x_pos_cloud -= self.speed_cloud

    def new_cloud_high(self,screen):
        image_width_cloud_1 = self.image_cloud.get_width()
        screen.blit(self.image_cloud, (image_width_cloud_1 + self.x_pos_cloud, self.y_pos_cloud_high))
        if self.x_pos_cloud <= self.FINAL:
            screen.blit(self.image_cloud, (image_width_cloud_1 + self.x_pos_cloud, self.y_pos_cloud_high))
            self.x_pos_cloud = random.randint(1010,1180)
            self.y_pos_cloud_high = random.randint(10, 100)
        self.x_pos_cloud -= self.speed_cloud