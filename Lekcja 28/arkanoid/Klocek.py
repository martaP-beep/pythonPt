import pygame
import copy 

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800

class Klocek(pygame.sprite.Sprite):
    def __init__(self, x, y, zdrowie):
        super(Klocek, self).__init__()
        self.obraz_oryginalny = pygame.image.load("images_arkanoid/brick.png")
        self.rect = pygame.Rect(x, y, 96, 48)
        self.zdrowie = zdrowie
    
    def aktualizuj(self):
        kolor = 0
        if self.zdrowie == 3:
            kolor = (0, 128, 0) #RGB zielony
        if self.zdrowie == 2:
            kolor = (0, 0, 128) # niebieski
        if self.zdrowie == 1:
            kolor = (128, 0, 0) # czerwony
        self.obraz = copy.copy(self.obraz_oryginalny)
        self.obraz.fill(kolor, special_flags=pygame.BLEND_ADD)
    
    def update(self):
        self.aktualizuj()
    
    def uderzenie(self):
        self.zdrowie -= 1
        if self.zdrowie <= 0:
            self.kill()
         
