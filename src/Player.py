#Define una clase para tu personaje (Player) que tenga propiedades como posición (x, y), velocidad, y funciones para moverse (por ejemplo, move_left(), move_right(), jump()).
#Implementa la lógica básica para que el personaje pueda moverse en el eje horizontal y saltar.

import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.jump_strength = 30
        self.gravity = 3
        self.velocity_y = 0
        self.is_jumping = False
        self.on_ground = False

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity_y = -self.jump_strength
            self.on_ground = False

    def update(self):
        if self.is_jumping:
            self.velocity_y += self.gravity  # Aplicar gravedad cuando está saltando
        else:
            self.velocity_y = self.gravity  # Aplicar gravedad cuando está cayendo

        self.y += self.velocity_y

        # Verifica si el jugador ha tocado el suelo
        if self.y >= 400:  # Ajusta según la altura del suelo
            self.y = 400
            self.velocity_y = 0
            self.is_jumping = False
            self.on_ground = True
        else:
            self.on_ground = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
