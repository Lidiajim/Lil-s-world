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
        # Verifica si el jugador está dentro del área del enemigo
        if (player.x < self.x + self.width and
            player.x + player.width > self.x and
            player.y < self.y + self.height and
            player.y + player.height > self.y):
            
            # Verifica si el jugador está colisionando desde abajo o los lados
            if player.y + player.height - player.velocity_y <= self.y + self.height and player.y + player.height >= self.y:
                return True  # Colisión desde abajo
            elif player.x + player.width > self.x and player.x < self.x + self.width:
                return True  # Colisión desde los lados

        return False

    def change_direction(self):
        self.direction *= -1
