import pygame

from Escenario import Escenario
from constantes import Posiciones


class Jugador(Escenario):
    def __init__(self, medidaX, medidaY, posicionX, posicionY, velocidad, color):
        self.medidaX = medidaX
        self.medidaY = medidaY
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.vel = velocidad
        self.color = color

    def moverJugador(self, teclaArriba, teclaAbajo):
        if pygame.key.get_pressed()[teclaArriba]:
            self.posicionY = max(Posiciones.posEscenario[1], self.posicionY - self.vel)
        elif pygame.key.get_pressed()[teclaAbajo]:
            self.posicionY = min(Posiciones.posEscenario[1] + Posiciones.midaEscenario[1] - self.medidaY,
                                self.posicionY + self.vel)


