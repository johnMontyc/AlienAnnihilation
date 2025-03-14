# -*- coding: utf-8 -*-

import pygame
import random

class Enemigo:
    def __init__(self, ancho_pantalla, alto_pantalla, ancho, alto):
        self.x = random.randint(0, ancho_pantalla - 40)
        self.y = random.randint(-100, -40)
        self.velocidad = random.randint(2, 5)
        self.width = ancho #40
        self.height = alto #40

    def mover(self):
        self.y += self.velocidad

    def dibujar(self, pantalla):
        
        #Color rojo
        ROJO = (255, 0, 0)
        pygame.draw.rect(pantalla, ROJO, (self.x, self.y, self.width, self.height))