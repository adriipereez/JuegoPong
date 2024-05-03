import pygame


class Jugador:

    def __init__(self, medidaX, medidaY, posicionX, posicionY, velocidad, color):
        self.medidaX = medidaX
        self.medidaY = medidaY
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.vel = velocidad
        self.color = color

    def pintar(self, ventanaJuego):
        pygame.draw.rect(ventanaJuego, self.color, ((self.posicionX, self.posicionY), (self.medidaX, self.medidaY)))