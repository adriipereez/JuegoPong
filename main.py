import random
import sys
import pygame

import constantes
from constantes import Colores, Posiciones, PelotaConstantes
from jugador import Jugador
from pelota import Pelota

pygame.init()

ventanaJuego = pygame.display.set_mode((600, 450))
jugador1 = Jugador(20, 100, 20, 140, 5, (255, 0, 0))
jugador2 = Jugador(20, 100, 560, 140, 5, (0, 0, 255))
pelota = Pelota(ventanaJuego, constantes.PelotaConstantes.VELOCIDAD_INICIAL, (255, 255, 255))
fontText = pygame.font.SysFont("monospace", 25)

reloj = pygame.time.Clock()

gameOver = False

def PintarObjetos():
    ventanaJuego.fill(Colores.negro)
    pygame.draw.rect(ventanaJuego, Colores.verde, (Posiciones.posEscenario, Posiciones.midaEscenario))



    # Mostrar els punts dels jugadors
    text1 = fontText.render(f"Jugador 1: {jugador1.puntos}", True, Colores.blanco)
    text2 = fontText.render(f"Jugador 2: {jugador2.puntos}", True, Colores.blanco)
    ventanaJuego.blit(text1, (10, ventanaJuego.get_height() - 50))
    ventanaJuego.blit(text2, (ventanaJuego.get_width() - text2.get_width() - 10, ventanaJuego.get_height() - 50))

    jugador1.pintar(ventanaJuego)
    jugador2.pintar(ventanaJuego)
    pelota.pintarPelota(ventanaJuego)

def DetectarEventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    jugador1.moverJugador(pygame.K_w,pygame.K_s)
    jugador2.moverJugador(pygame.K_UP,pygame.K_DOWN)


while not gameOver:
    PintarObjetos()
    DetectarEventos()

    pelota.moverPelota(ventanaJuego, jugador1, jugador2)
    reloj.tick(30)
    pygame.display.update()