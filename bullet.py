import pygame
from pygame.sprite import Sprite
#子弹的封装
class Bullet(Sprite):
    def __init__(self,ai_game):
        #继承Sprit
        super().__init__()
        #属性的赋值
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #初始化边缘矩形
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        #生成在中间的顶部
        self.rect.midtop = ai_game.ship.rect.midtop
        #坐标初始化为矩形的初始位置
        self.y = float(self.rect.y)
    def update(self):
        #实时更新子弹位置和矩形高度
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)