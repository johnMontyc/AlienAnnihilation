# -*- coding: utf-8 -*-

import pygame
import random

class Enemigo:
    def __init__(self, ancho_pantalla, alto_pantalla, ancho, alto, escala):
        """Inicializa el enemigo con una posición aleatoria y velocidad de caída."""
        self.x = random.randint(0, ancho_pantalla - 40) 
        self.y = random.randint(-100, -40) # Aparece fuera de la pantalla
        self.velocidad = random.randint(2, 4) # Velocidad aleatoria de movimiento
        self.width = int(ancho * escala)  
        self.height = int(alto * escala)

        # Cargar spritesheet de los enemigos
        self.spritesheet = pygame.image.load("alien.png").convert_alpha()

        # Recortar el sprite del enemigo
        sprite_original = self.spritesheet.subsurface((0, 0, ancho, alto))

        # Escalar el sprite
        self.sprite = pygame.transform.scale(sprite_original, (self.width, self.height))

    def mover(self):
        """Mueve el enemigo hacia abajo en la pantalla."""
        self.y += self.velocidad

    def dibujar(self, pantalla):
        """Dibuja el enemigo en la pantalla."""
        pantalla.blit(self.sprite, (self.x, self.y))