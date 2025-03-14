# -*- coding: utf-8 -*-

from Player import Player
from Enemigo import Enemigo
import pygame

class Game:
    def __init__(self):
        pygame.init()

        # Configuración de pantalla
        self.ANCHO = 800
        self.ALTO = 600
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Caza al Enemigo")

        # Configuración del juego
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.running = True
        self.VELOCIDAD_JUGADOR = 5
        self.ANCHO_JUGADOR = 40
        self.ALTO_JUGADOR = 40
        self.ANCHO_ENEMIGO = 40
        self.ALTO_ENEMIGO = 40
        


        # Instancias
        self.jugador = Player(self.ANCHO, self.ALTO, self.VELOCIDAD_JUGADOR, self.ANCHO_JUGADOR, self.ALTO_JUGADOR)
        self.enemigos = [Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO) for _ in range(5)]
        self.proyectiles = []

    def manejar_eventos(self):
         for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                self.jugador.disparar(self.proyectiles)

    def actualizar(self):
        teclas = pygame.key.get_pressed()
        self.jugador.mover(teclas, self.ANCHO)

        for proyectil in self.proyectiles[:]:
            proyectil.mover()
            if proyectil.y < 0:
                self.proyectiles.remove(proyectil)

        for enemigo in self.enemigos[:]:
            enemigo.mover()
            if enemigo.y > self.ALTO:
                self.enemigos.remove(enemigo)
                self.enemigos.append(Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO))

        for proyectil in self.proyectiles[:]:
            for enemigo in self.enemigos[:]:
                if proyectil.colisionar(enemigo):
                    self.enemigos.remove(enemigo)
                    self.proyectiles.remove(proyectil)
                    self.enemigos.append(Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO))
                    break

    def dibujar(self):
        self.pantalla.fill((0, 0, 0)) #fondo negro
        self.jugador.dibujar(self.pantalla)
        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)
        for proyectil in self.proyectiles:
            proyectil.dibujar(self.pantalla)
        pygame.display.flip()

    def ejecutar(self):
        while self.running:
            self.clock.tick(30)
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
        pygame.quit()
        