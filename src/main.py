#main.py donde iniciarás tu código.


from Player import Player
import pygame
from Platform import Platform

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Plataforma")

# Reloj para controlar la velocidad de actualización de la pantalla
clock = pygame.time.Clock()

# Inicializa el jugador
player = Player(100, 400)

# Inicializa las plataformas
platforms = [
    Platform(0, 400, 800, 100),
    Platform(300, 300, 200, 20),
    Platform(500, 200, 200, 20)
]

# Bucle principal
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Controles del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_SPACE] and not player.is_jumping:
        player.jump()

    # Actualiza el jugador
    player.update()

    # Dibuja el fondo
    screen.fill((255, 255, 255))

    # Dibuja al jugador
    player.draw(screen)

    # Dibuja las plataformas
    for platform in platforms:
        platform.draw(screen)

        # Verifica si el jugador colisiona con la plataforma
        if platform.collide(player):
            if player.y + 50 <= platform.y + platform.height and player.y + 50 > platform.y:
                player.y = platform.y - 50  # Ajusta la posición vertical del jugador para que se quede en la plataforma
                player.is_jumping = False  # Asegúrate de que el jugador no esté en el aire
                on_platform = True
    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de actualización de la pantalla
    clock.tick(60)

# Cierra Pygame
pygame.quit()

