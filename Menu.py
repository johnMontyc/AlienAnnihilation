# -*- coding: utf-8 -*-

import pygame

class Menu:
    def __init__(self, pantalla, ancho, alto):
        """Inicializa el menú con referencias a la pantalla y dimensiones."""
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto
        self.fuente = pygame.font.Font(None, 40) # Fuente para los textos del menú

    def mostrar_menu_principal(self):
        """Muestra el menú principal con opciones para jugar o salir."""
        while True:
            self.pantalla.fill((0, 0, 0))
            texto_jugar = self.fuente.render("Presiona ENTER para jugar", True, (255, 255, 255))
            texto_salir = self.fuente.render("Presiona ESC para salir", True, (255, 255, 255))

            self.pantalla.blit(texto_jugar, (self.ancho // 2 - 150, self.alto // 2 - 30))
            self.pantalla.blit(texto_salir, (self.ancho // 2 - 150, self.alto // 2 + 30))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        return "jugando"
                    if evento.key == pygame.K_ESCAPE:
                        return "salir"

    def mostrar_menu_pausa(self):
        """Muestra el menú de pausa y espera la reanudación del juego."""
        while True:
            self.pantalla.fill((50, 50, 50))
            texto_continuar = self.fuente.render("Presiona ENTER para continuar", True, (255, 255, 255))
            texto_menu = self.fuente.render("Presiona ESC para volver al menú", True, (255, 255, 255))

            self.pantalla.blit(texto_continuar, (self.ancho // 2 - 180, self.alto // 2 - 30))
            self.pantalla.blit(texto_menu, (self.ancho // 2 - 180, self.alto // 2 + 30))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        return "jugando"
                    if evento.key == pygame.K_ESCAPE:
                        return "menu"

    def mostrar_menu_victoria(self):
        """Muestra la pantalla de victoria."""
        while True:
            self.pantalla.fill((0, 100, 0))
            texto_victoria = self.fuente.render("¡Has ganado!", True, (255, 255, 255))
            texto_menu = self.fuente.render("Presiona ESC para volver al menú", True, (255, 255, 255))

            self.pantalla.blit(texto_victoria, (self.ancho // 2 - 80, self.alto // 2 - 60))
            self.pantalla.blit(texto_menu, (self.ancho // 2 - 180, self.alto // 2))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return "menu"

    def mostrar_menu_derrota(self):
        """Muestra la pantalla de derrota."""
        while True:
            self.pantalla.fill((100, 0, 0))
            texto_derrota = self.fuente.render("¡Has perdido!", True, (255, 255, 255))
            texto_menu = self.fuente.render("Presiona ESC para volver al menú", True, (255, 255, 255))

            self.pantalla.blit(texto_derrota, (self.ancho // 2 - 80, self.alto // 2 - 60))
            self.pantalla.blit(texto_menu, (self.ancho // 2 - 180, self.alto // 2))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return "menu"