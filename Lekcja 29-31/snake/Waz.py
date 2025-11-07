import pygame 
from Kierunek import Kierunek
from Segment import Segment
import copy


class Waz(pygame.sprite.Sprite):
    def __init__(self):
        #oryginalny obraz glowny 
        self.oryginalny_obraz = pygame.image.load("images_snake/head.png")
        # dodanie obrazu pomocniczego (bedzie sie zmienial przy zmianie kierunku poruszania sie )
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz,0)

        #wspolrzedne glowy 
        self.rect = self.obraz.get_rect(center = (12*32+16,9*32+16))

        # zmienne odpowiedzialne za kierunek i nowy wyznaczony kierunek 
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA

        self.ostatnia_pozycja = self.rect
        self.dodaj_segment = False
        self.segmenty = []

    

    def zmien_kierunek(self,kierunek):          # waz nie moze obracac sie o 180 stopni !!!
        zmiana_mozliwa = True
        if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:     
            zmiana_mozliwa = False
        if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False 
        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz,(self.kierunek.value*-90))

        self.ostatnia_pozycja = copy.deepcopy(self.rect)

        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0,-32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32,0)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32,0)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0,32)
        
        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
                pass
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)
                pass

        if self.dodaj_segment:
            nowy = Segment()
            nowa_pozycja = None
            if len(self.segmenty) > 0 :
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].pozycja)
                pass
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
                pass
            nowy.pozycja = nowa_pozycja
            self.segmenty.append(nowy)
            self.dodaj_segment = False
    
    def zjedz_jablko(self):
        self.dodaj_segment = True
    
    def rysuj_segmenty(self, ekran):                                                  
        for segment in self.segmenty:
            ekran.blit(segment.obraz, segment.pozycja)
