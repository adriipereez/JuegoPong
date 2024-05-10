import random
import sys
import pygame

import constantes
from constantes import Colores, Posiciones, PelotaConstantes
from jugador import Jugador
from pelota import Pelota

pygame.init()

ventanaJuego = pygame.display.set_mode((600, 400))
jugador1 = Jugador(20, 100, 20, 140, 5, (255, 0, 0))
jugador2 = Jugador(20, 100, 560, 140, 5, (0, 0, 255))
pelota = Pelota(ventanaJuego, constantes.PelotaConstantes.VELOCIDAD_INICIAL, (255, 255, 255))

reloj = pygame.time.Clock()

gameOver = False

def PintarObjetos():
    ventanaJuego.fill(Colores.negro)
    pygame.draw.rect(ventanaJuego, Colores.verde, (Posiciones.posEscenario, Posiciones.midaEscenario))

    jugador1.pintar(ventanaJuego)
    jugador2.pintar(ventanaJuego)
    pelota.pintarPelota(ventanaJuego)

def DetectarEventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    jugador1.moverJugador(pygame.K_w,pygame.K_s)
    jugador2.moverJugador(pygame.K_UP,pygame.K_DOWN)

def moverPelota():
    pelota.posicionX += pelota.velocidad * pelota.direccionX
    pelota.posicionY += pelota.velocidad * pelota.direccionY

    # Rebote en el escenario verde
    if pelota.posicionY - pelota.medida[1] / 2 <= Posiciones.posEscenario[1] or pelota.posicionY + pelota.medida[
        1] / 2 >= Posiciones.posEscenario[1] + Posiciones.midaEscenario[1]:
        pelota.direccionY *= -1
        pelota.velocidad += PelotaConstantes.INCREMENTO_VELOCIDAD

    if pelota.posicionX - pelota.medida[0] / 2 <= Posiciones.posEscenario[0]:
        pelota.posicionX = ventanaJuego.get_width() // 2
        pelota.posicionY = ventanaJuego.get_height() // 2
        pelota.velocidad = PelotaConstantes.VELOCIDAD_INICIAL
        pelota.direccionX = random.choice([-1, 1])
        pelota.direccionY = random.choice([-1, 1])

    elif pelota.posicionX + pelota.medida[0] / 2 >= Posiciones.posEscenario[0] + Posiciones.midaEscenario[0]:
        pelota.posicionX = ventanaJuego.get_width() // 2
        pelota.posicionY = ventanaJuego.get_height() // 2
        pelota.velocidad = PelotaConstantes.VELOCIDAD_INICIAL
        pelota.direccionX = random.choice([-1, 1])
        pelota.direccionY = random.choice([-1, 1])

    elif (pelota.posicionX - pelota.medida[0] / 2 <= jugador1.posicionX + jugador1.medidaX and
          jugador1.posicionY <= pelota.posicionY <= jugador1.posicionY + jugador1.medidaY) or \
            (pelota.posicionX + pelota.medida[0] / 2 >= jugador2.posicionX and
             jugador2.posicionY <= pelota.posicionY <= jugador2.posicionY + jugador2.medidaY):
        pelota.direccionX *= -1
        pelota.velocidad += PelotaConstantes.INCREMENTO_VELOCIDAD

while not gameOver:
    PintarObjetos()
    DetectarEventos()

    moverPelota()
    reloj.tick(30)
    pygame.display.update()