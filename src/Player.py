#Define una clase para tu personaje (Player) que tenga propiedades como posición (x, y), velocidad, y funciones para moverse (por ejemplo, move_left(), move_right(), jump()).
#Implementa la lógica básica para que el personaje pueda moverse en el eje horizontal y saltar.

import pygame

class Player:
    def __init__(self, x, y):
        self.x = x  # eje horizontal
        self.y = y  # eje vertical
        self.speed = 5  # velocidad de movimiento
        self.jump_strength = 15
        self.gravity = 1
        self.velocity_y = 0
        self.is_jumping = False
        self.on_ground = False


# mueve el personaje hacia la izquierda  <--
    def move_left(self):
        self.x -= self.speed 

# mueve el personaje hacia la derecha  -->
    def move_right(self):
        self.x += self.speed

# hace que el personaje salte
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y -= 100  # reduce y para mover el personaje hacia arriba  ( el eje y aumenta hacia abajo)

# Actualiza la posición del personaje, especialmente la posición vertical durante un salto
    def update(self):
        if self.is_jumping:
            self.y += 5  # aumenta y para simular la gravedad y que el personaje caiga
            if self.y >= 400:  # si el personaje ha vuelto al suelo (y = 400)
                self.is_jumping = False
                self.y = 400 # restablece la posición vertical del personaje

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 50, 50))