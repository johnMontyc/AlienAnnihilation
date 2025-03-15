# -*- coding: utf-8 -*-

import pygame

class Proyectil:
    def __init__(self, x, y, velocidad, width, height):
        """Inicializa un proyectil en la posición del jugador."""
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.width = width #5
        self.height = height #10

    def mover(self):
        """Mueve el proyectil hacia arriba."""
        self.y -= self.velocidad

    def colisionar(self, enemigo):
        """Verifica si el proyectil colisiona con un enemigo."""
        return (self.x > enemigo.x and self.x < enemigo.x + enemigo.width) and \
               (self.y > enemigo.y and self.y < enemigo.y + enemigo.height)

    def dibujar(self, pantalla):
        """Dibuja el proyectil en la pantalla."""
        #Color blanco
        BLANCO = (255, 255, 255)
        
        
        pygame.draw.rect(pantalla, BLANCO, (self.x, self.y, self.width, self.height))