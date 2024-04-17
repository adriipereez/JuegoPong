import pygame


class Jugador:
    midaJugador = (20, 100)

    color1 = (255, 0, 0)
    posicionJugador1 = (20, 140)

    color2 = (0, 0, 255)
    posicionJugador2 = (20, 80)

    def __init__(self, medidaX, medidaY, posicionX, posicionY, velocidad, color):
        self.medidaX = medidaX
        self.medidaY = medidaY
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.vel = velocidad
        self.color = color

    def pintar(self, ventanaJuego):
        pygame.draw.rect(ventanaJuego, self.color, ((self.posicionX, self.posicionY), (self.medidaX, self.medidaY)))