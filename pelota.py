import random
import pygame

from Escenario import Escenario


class Pelota(Escenario):

    def __init__(self, ventanajuego, velocidad, color):
        self.posicionX = ventanajuego.get_width() // 2
        self.posicionY = ventanajuego.get_height() // 2
        self.velocidad = velocidad
        self.direccionX = random.choice([-1, 1])
        self.direccionY = random.choice([-1, 1])
        self.color = color