from dino_runner.utils.constants import CLOUD

class Cloud:
    FINAL = -500

    def __init__(self,speed_cloud,type_cloud,x_pos_cloud,y_pos_cloud):
        self.image_cloud = CLOUD[type_cloud]
        self.speed_cloud = speed_cloud
        self.x_pos_cloud = x_pos_cloud
        self.y_pos_cloud = y_pos_cloud
        
    def new_cloud(self,screen):
        image_width_cloud_1 = self.image_cloud.get_width()
        screen.blit(self.image_cloud, (image_width_cloud_1 + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= self.FINAL:
            screen.blit(self.image_cloud, (image_width_cloud_1 + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1010
        self.x_pos_cloud -= self.speed_cloud