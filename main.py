import sys
from constantes import colores
from constantes import posiciones
import pygame

pygame.init()

vetanaJuego = pygame.display.set_mode((600, 400))

reloj = pygame.time.Clock()

gameOver = False

def PintarObjetos():
    vetanaJuego.fill(colores.negro)
    pygame.draw.rect(vetanaJuego, colores.verde, (posiciones.posEscenario,posiciones.midaEscenario))


def DetectarEventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



while not gameOver:

    PintarObjetos()

    DetectarEventos()

    reloj.tick(30)
    pygame.display.update()

