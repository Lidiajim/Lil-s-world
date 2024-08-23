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
        # Verifica si hay superposición horizontal
        if player.x < self.x + self.width and player.x + player.width > self.x:
            # Verifica si hay superposición vertical
            if player.y < self.y + self.height and player.y + player.height > self.y:
                # Verifica colisión en los bordes izquierdo o derecho del jugador
                if (abs(player.x - (self.x + self.width)) < 5 or  # Colisión borde izquierdo
                    abs((player.x + player.width) - self.x) < 5):  # Colisión borde derecho
                    return 'side'  # Colisión con los bordes del jugador
                elif player.y + player.height - player.velocity_y <= self.y:
                    return 'top'  # Colisión desde arriba
        return None

    def change_direction(self):
        self.direction *= -1
