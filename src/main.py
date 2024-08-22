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
    if keys[pygame.K_SPACE]:
        player.jump()

    # Actualiza el jugador
    player.update()

    # Dibuja el fondo
    screen.fill((255, 255, 255))

    # Dibuja las plataformas
    on_platform = False
    for platform in platforms:
        platform.draw(screen)

        # Verifica si el jugador colisiona con la plataforma
        if (player.x < platform.x + platform.width and
            player.x + player.width > platform.x and
            player.y + player.height > platform.y and
            player.y + player.height - player.velocity_y <= platform.y):
            # Ajusta la posición vertical del jugador para que se quede en la plataforma
            player.y = platform.y - player.height
            player.velocity_y = 0
            player.is_jumping = False
            player.on_ground = True
            on_platform = True

    # Si el jugador no está en una plataforma, está en el aire
    if not on_platform and player.y < 400:
        player.on_ground = False

    # Dibuja al jugador
    player.draw(screen)

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de actualización de la pantalla
    clock.tick(60)

# Cierra Pygame
pygame.quit()
