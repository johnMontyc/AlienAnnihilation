# -*- coding: utf-8 -*-

import pygame

class Proyectil:
    def __init__(self, x, y, velocidad, width, height):
        self.x = x
        self.y = y
        self.velocidad = velocidad #7
        self.width = width #5
        self.height = height #10

    def mover(self):
        self.y -= self.velocidad

    def colisionar(self, enemigo):
        return (self.x > enemigo.x and self.x < enemigo.x + enemigo.width) and \
               (self.y > enemigo.y and self.y < enemigo.y + enemigo.height)

    def dibujar(self, pantalla):
        
        #Color blanco
        BLANCO = (255, 255, 255)
        
        
        pygame.draw.rect(pantalla, BLANCO, (self.x, self.y, self.width, self.height))