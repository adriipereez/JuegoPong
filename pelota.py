import random
import pygame

class Pelota:
    medida = (15, 15)

    def __init__(self, ventanajuego, velocidad, color):
        self.posicionX = ventanajuego.get_width() // 2
        self.posicionY = ventanajuego.get_height() // 2
        self.velocidad = velocidad
        self.direccionX = random.choice([-1, 1])
        self.direccionY = random.choice([-1, 1])
        self.color = color

    def pintar(self, ventanaJuego):
        pygame.draw.circle(ventanaJuego, self.color, (self.posicionX, self.posicionY), self.medida[0] // 2)
