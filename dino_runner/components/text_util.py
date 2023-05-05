from pygame.font import Font
from dino_runner.utils.constants import SCREEN_HEIGHT,SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)
white_color = (255,255,255)

def get_message_points(night_min,night_max,points, message,size,width = SCREEN_WIDTH// 2, height = SCREEN_HEIGHT // 2):
    if points > night_min and points < night_max:
        font = Font(FONT_STYLE,size)
        text = font.render(message,True,white_color)
        text_rect = text.get_rect()
        text_rect.center = (width,height)
    else:
        font = Font(FONT_STYLE,size)
        text = font.render(message,True,black_color)
        text_rect = text.get_rect()
        text_rect.center = (width,height)
    return text, text_rect

def get_message(message,size,width = SCREEN_WIDTH// 2, height = SCREEN_HEIGHT // 2):
        font = Font(FONT_STYLE,size)
        text1 = font.render(message,True,black_color)
        text1_rect = text1.get_rect()
        text1_rect.center = (width,height)
        return text1, text1_rect