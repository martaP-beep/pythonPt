import pygame

from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek

poziom1 = [
[0, 0, 1, 2, 2, 3, 2, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = poziom1
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32 + i * 96, 32 + j * 48, wczytany_poziom[j][i])
                klocki.add(klocek)


dodaj_klocki()

pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont("Arial", 30)
 
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
 
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
pygame.display.set_caption("Gra")
 
clock = pygame.time.Clock()
 
status = True

obraz_tla = pygame.image.load("images_arkanoid/background.png")

platforma = Platforma()
kulka = Kulka()

zycia = 3

while status:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            status = False
            pass
    

    wcisniete_klawisze = pygame.key.get_pressed()
    if wcisniete_klawisze[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)
    if wcisniete_klawisze[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)


    kulka.aktualizuj(platforma, klocki)
    klocki.update()
    platforma.aktulizuj()

    screen_surface.blit(obraz_tla, (0,0))

    for k in klocki:
        screen_surface.blit(k.obraz, k.rect)

    screen_surface.blit(platforma.obraz, platforma.rect)
    screen_surface.blit(kulka.obraz, kulka.rect)

    if kulka.przegrana:
        zycia -= 1
        if zycia == 0 :
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    tekst = czcionka.render(f"Życia: {zycia}", False, (255,255,255) )
    screen_surface.blit(tekst, (10,10))
    pygame.display.flip()
    clock.tick(60)
    pass
 
pygame.quit()
quit()