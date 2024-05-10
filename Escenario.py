import pygame

class Escenario:
    medida = (15,15)

    def pintar(self, ventanaJuego):
        pygame.draw.rect(ventanaJuego, self.color, ((self.posicionX, self.posicionY), (self.medidaX, self.medidaY)))

    def pintarPelota(self, ventanaJuego):
        pygame.draw.circle(ventanaJuego, self.color, (self.posicionX, self.posicionY), self.medida[0] // 2)