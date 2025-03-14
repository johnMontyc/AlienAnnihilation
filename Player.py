    # -*- coding: utf-8 -*-

import pygame
from Proyectil import Proyectil

class Player:
    
    def __init__(self, ancho_pantalla, alto_pantalla, velocidad, ancho, alto):
        self.x = ancho_pantalla // 2
        self.y = alto_pantalla - 50
        self.velocidad = velocidad #5
        self.width = ancho #40
        self.height = alto #40
        
    def mover(self, teclas, ancho_pantalla):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x < ancho_pantalla - self.width:
            self.x += self.velocidad

    def disparar(self, proyectiles):
        proyectiles.append(Proyectil(self.x + self.width // 2, self.y, 7, 5, 10))

    def dibujar(self, pantalla):
        
        #Color azul
        AZUL = (0, 0, 255)
        
        pygame.draw.rect(pantalla, AZUL, (self.x, self.y, self.width, self.height))