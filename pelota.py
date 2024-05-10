import random
import pygame

from Escenario import Escenario
from constantes import Posiciones, PelotaConstantes


class Pelota(Escenario):

    def __init__(self, ventanajuego, velocidad, color):
        self.posicionX = ventanajuego.get_width() // 2
        self.posicionY = ventanajuego.get_height() // 2
        self.velocidad = velocidad
        self.direccionX = random.choice([-1, 1])
        self.direccionY = random.choice([-1, 1])
        self.color = color

    def moverPelota(self, ventanaJuego, jugador1, jugador2):
        self.posicionX += self.velocidad * self.direccionX
        self.posicionY += self.velocidad * self.direccionY

        # Rebote en el escenario verde
        if self.posicionY - self.medida[1] / 2 <= Posiciones.posEscenario[1] or self.posicionY + self.medida[
            1] / 2 >= Posiciones.posEscenario[1] + Posiciones.midaEscenario[1]:
            self.direccionY *= -1
            self.velocidad += PelotaConstantes.INCREMENTO_VELOCIDAD

        if self.posicionX - self.medida[0] / 2 <= Posiciones.posEscenario[0]:
            self.posicionX = ventanaJuego.get_width() // 2
            self.posicionY = ventanaJuego.get_height() // 2
            self.velocidad = PelotaConstantes.VELOCIDAD_INICIAL
            self.direccionX = random.choice([-1, 1])
            self.direccionY = random.choice([-1, 1])
            jugador2.puntos += 1
        elif self.posicionX + self.medida[0] / 2 >= Posiciones.posEscenario[0] + Posiciones.midaEscenario[0]:
            self.posicionX = ventanaJuego.get_width() // 2
            self.posicionY = ventanaJuego.get_height() // 2
            self.velocidad = PelotaConstantes.VELOCIDAD_INICIAL
            self.direccionX = random.choice([-1, 1])
            self.direccionY = random.choice([-1, 1])
            jugador1.puntos += 1
        elif (self.posicionX - self.medida[0] / 2 <= jugador1.posicionX + jugador1.medidaX and
              jugador1.posicionY <= self.posicionY <= jugador1.posicionY + jugador1.medidaY) or \
                (self.posicionX + self.medida[0] / 2 >= jugador2.posicionX and
                 jugador2.posicionY <= self.posicionY <= jugador2.posicionY + jugador2.medidaY):
            self.direccionX *= -1
            self.velocidad += PelotaConstantes.INCREMENTO_VELOCIDAD