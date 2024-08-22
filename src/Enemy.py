import pygame

class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = 1  # 1 para derecha, -1 para izquierda
        

    def update(self):
        # Mueve al enemigo horizontalmente
        self.x += self.speed * self.direction
        
        # Cambia de dirección si el enemigo toca el borde de la pantalla o de la plataforma
        if self.x <= 0 or self.x + self.width >= 800:  # Ajusta el borde según el tamaño de la pantalla
            self.direction *= -1

    def draw(self, screen, camera_x, camera_y):
        pygame.draw.rect(screen, (0, 255, 0), (self.x - camera_x, self.y - camera_y, self.width, self.height))

    def collide(self, player):
        if (self.x < player.x + player.width and
            self.x + self.width > player.x and
            self.y < player.y + player.height and
            self.y + self.height > player.y):
            return True
        return False

    def change_direction(self):
        self.direction *= -1
