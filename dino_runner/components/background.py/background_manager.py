from dino_runner.components.background.cloud import Cloud

class BackgroundManager:
    def __init__(self):
        self.element = []

    def update(self,game_speed):
        if len(self.element) == 0:
                self.element.append(Cloud())
        for background in self.element:
            if background.rect.x < - background.rect.width:
                self.element.remove(background)
            background.update(game_speed)

    def draw(self,screen):
        for background in self.element:
            background.draw(screen)