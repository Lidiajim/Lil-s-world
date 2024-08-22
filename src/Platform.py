# Define una clase Platform que represente las plataformas en el juego. Las plataformas tendrán propiedades como posición, tamaño y tal vez un tipo (por ejemplo, móvil o estática).
#Implementa la detección de colisiones entre el personaje y las plataformas para que el personaje pueda "pararse" sobre ellas.

import pygame

class Platform: 
    def __init__(self, x, y, width, height):
        self.x = x  # eje horizontal
        self.y = y  # eje vertical
        self.width = width  # ancho
        self.height = height # alto

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def collide(self, player):
        if player.x < self.x + self.width and player.x + 50 > self.x and player.y < self.y + self.height and player.y + 50 > self.y:
            return True
        return False