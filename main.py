import sys

import jugador
from constantes import Colores
from constantes import Posiciones
from jugador import Jugador
import pygame

pygame.init()

vetanaJuego = pygame.display.set_mode((600, 400))
jugador1 = Jugador(20,100,20,140,5, (255, 0, 0))
jugador2 = Jugador(20,100,560,140,5, (0, 0, 255))
reloj = pygame.time.Clock()

gameOver = False

def PintarObjetos():
    vetanaJuego.fill(Colores.negro)
    pygame.draw.rect(vetanaJuego, Colores.verde, (Posiciones.posEscenario,Posiciones.midaEscenario))

    jugador1.pintar(vetanaJuego)
    jugador2.pintar(vetanaJuego)

def DetectarEventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



while not gameOver:

    PintarObjetos()

    DetectarEventos()

    reloj.tick(30)
    pygame.display.update()

