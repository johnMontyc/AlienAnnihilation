# -*- coding: utf-8 -*-

from Player import Player
from Enemigo import Enemigo
from Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()

        # Configuración de pantalla
        self.ANCHO = 800
        self.ALTO = 600
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Caza al Enemigo")

        # Cargar fondo y escalar la imagen del fondo
        self.fondo = pygame.image.load("meteorito1.png")
        self.fondo = pygame.transform.scale(self.fondo, (self.ANCHO, self.ALTO))

        # Configuración del juego
        self.FPS = 30 # Velocidad de actualización del juego
        self.clock = pygame.time.Clock()
        self.running = True
        self.estado = "menu"  # Estados posibles: menu, jugando, pausa, victoria, derrota
        self.VELOCIDAD_JUGADOR = 5 # Velocidad de movimiento del jugador
        self.ANCHO_JUGADOR = 120
        self.ALTO_JUGADOR = 120
        self.ANCHO_ENEMIGO = 215
        self.ALTO_ENEMIGO = 215
        self.escala_enemigo = 0.4
        self.escala_personaje = 0.8
        self.vidas = 5  # Cantidad de vidas del jugador
        self.tiempo_inicio = None  # Tiempo en que comienza la partida
        self.tiempo_victoria = 30  # Tiempo necesario para ganar (segundos)

        # Instancias
        self.jugador = Player(self.ANCHO, self.ALTO, self.VELOCIDAD_JUGADOR, self.ANCHO_JUGADOR, self.ALTO_JUGADOR, self.escala_personaje)
        self.enemigos = [Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO, self.escala_enemigo) for _ in range(5)]
        self.proyectiles = []
        self.menu = Menu(self.pantalla, self.ANCHO, self.ALTO)

    def manejar_eventos(self):
        """ Maneja los eventos de entrada del jugador, como teclas presionadas. """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False  # Cierra el juego si se presiona el botón de cerrar
            if self.estado == "jugando":
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        self.jugador.disparar(self.proyectiles)  # Disparo del jugador
                    if evento.key == pygame.K_ESCAPE:
                        self.estado = "pausa" # Pausar el juego

    def actualizar(self):
        """ Actualiza la posición de los objetos en el juego y verifica colisiones. """
        if self.estado == "jugando":
            teclas = pygame.key.get_pressed()
            self.jugador.mover(teclas, self.ANCHO)

            # Mover los proyectiles
            for proyectil in self.proyectiles[:]:
                proyectil.mover()
                if proyectil.y < 0:
                    self.proyectiles.remove(proyectil)
            # Mover y verificar colisiones con enemigos
            for enemigo in self.enemigos[:]:
                enemigo.mover()
                if enemigo.y > self.ALTO:
                    self.enemigos.remove(enemigo)
                    self.enemigos.append(Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO, self.escala_enemigo))

                # Verificar colisión entre el jugador y los enemigos
                if self.jugador.colisionar(enemigo):
                    self.vidas -= 1
                    self.enemigos.remove(enemigo)
                    self.enemigos.append(Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO, self.escala_enemigo))

                    if self.vidas <= 0:
                        self.estado = "derrota"

            # Verificar colisión entre proyectiles y enemigos
            for proyectil in self.proyectiles[:]:
                for enemigo in self.enemigos[:]:
                    if proyectil.colisionar(enemigo):
                        self.enemigos.remove(enemigo)
                        self.proyectiles.remove(proyectil)
                        self.enemigos.append(Enemigo(self.ANCHO, self.ALTO, self.ANCHO_ENEMIGO, self.ALTO_ENEMIGO, self.escala_enemigo))
                        break

            # Verificar si el jugador ha ganado
            if pygame.time.get_ticks() - self.tiempo_inicio > self.tiempo_victoria * 1000:
                self.estado = "victoria"

    def dibujar(self):
        """ Dibuja los elementos en la pantalla según el estado actual del juego. """
        self.pantalla.fill((0, 0, 0))
        self.pantalla.blit(self.fondo, (0, 0))
        if self.estado == "jugando":
            self.jugador.dibujar(self.pantalla)
            for enemigo in self.enemigos:
                enemigo.dibujar(self.pantalla)
            for proyectil in self.proyectiles:
                proyectil.dibujar(self.pantalla)
            self.mostrar_hud()
        elif self.estado == "menu":
            self.menu.mostrar_menu_principal()
        elif self.estado == "pausa":
            self.menu.mostrar_menu_pausa()
        elif self.estado == "victoria":
            self.menu.mostrar_menu_victoria()
        elif self.estado == "derrota":
            self.menu.mostrar_menu_derrota()
        pygame.display.flip()
        
    def mostrar_hud(self): 
        """ Muestra la interfaz de usuario con el contador de vidas y el tiempo restante. """
        fuente = pygame.font.Font(None, 36) 
        texto_vidas = fuente.render(f"Vidas: {self.vidas}", True, (255, 255, 255))
        self.pantalla.blit(texto_vidas, (10, 10))
    
        # Calcular el tiempo restante
        tiempo_transcurrido = (pygame.time.get_ticks() - self.tiempo_inicio) // 1000
        tiempo_restante = max(0, self.tiempo_victoria - tiempo_transcurrido)
        texto_tiempo = fuente.render(f"Tiempo: {tiempo_restante}s", True, (255, 255, 255))
        self.pantalla.blit(texto_tiempo, (self.ANCHO - 150, 10))  

    def ejecutar(self):
        """ Bucle principal del juego que maneja los eventos, la lógica y el dibujo. """
        while self.running:
            self.clock.tick(self.FPS)
            if self.estado == "menu":
                self.estado = self.menu.mostrar_menu_principal()
                self.vidas = 5 #Se reinicia el numero de vidas
                if self.estado == "jugando":
                    self.tiempo_inicio = pygame.time.get_ticks()
                elif self.estado == "salir":
                    self.running = False
            elif self.estado == "pausa":
                self.estado = self.menu.mostrar_menu_pausa()
            elif self.estado == "victoria":
                self.estado = self.menu.mostrar_menu_victoria()
            elif self.estado == "derrota":
                self.estado = self.menu.mostrar_menu_derrota()
            else:
                self.manejar_eventos()
                self.actualizar()
                self.dibujar()
        pygame.quit()
