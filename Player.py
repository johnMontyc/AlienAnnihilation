    # -*- coding: utf-8 -*-

import pygame
from Proyectil import Proyectil

class Player:
    
    def __init__(self, ancho_pantalla, alto_pantalla, velocidad, ancho, alto, escala):
        """Inicializa el jugador con su posición, tamaño, velocidad y sprite."""
        self.x = ancho_pantalla // 2
        self.y = alto_pantalla - alto # Posición inicial en la parte inferior de la pantalla
        self.velocidad = velocidad 
        self.width = int(ancho * escala)  
        self.height = int(alto * escala)
        
        # Cargar spritesheet
        self.spritesheet = pygame.image.load("player.png").convert_alpha()

        # Recortar la imagen del jugador desde el spritesheet (x, y, width, height)
        sprite_original = self.spritesheet.subsurface((0, 0, ancho, alto))

        # Escalar el sprite
        self.sprite = pygame.transform.scale(sprite_original, (self.width, self.height))
        self.sprite = pygame.transform.rotate(self.sprite, 90)
        
    def mover(self, teclas, ancho_pantalla):
        """Mueve al jugador dentro de los límites de la pantalla según las teclas presionadas."""
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x < ancho_pantalla - self.width:
            self.x += self.velocidad

    def disparar(self, proyectiles):
        """Crea un proyectil y lo añade a la lista de proyectiles."""
        proyectiles.append(Proyectil(self.x + self.width // 2, self.y, 7, 5, 10))

    def dibujar(self, pantalla):
        """Dibuja al jugador en la pantalla."""
        pantalla.blit(self.sprite, (self.x, self.y))
    
    def colisionar(self, enemigo):
        """Verifica si el jugador colisiona con un enemigo."""
        return pygame.Rect(self.x, self.y, 
                           self.width, self.height).colliderect(pygame.Rect(enemigo.x, enemigo.y, 
                                                                            enemigo.width, enemigo.height))