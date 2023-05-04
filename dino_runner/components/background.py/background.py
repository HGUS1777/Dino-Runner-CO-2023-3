class Background:
    FINAL = -300
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 1020

    def update(self):
        pass

    def draw(self):
        pass