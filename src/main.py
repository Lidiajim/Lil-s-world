#main.py donde iniciarás tu código.


from Player import Player
import pygame
from Platform import Platform
from Enemy import Enemy

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plataforma")

# Variables para la cámara
camera_x = 0
camera_y = 0

# Reloj para controlar la velocidad de actualización de la pantalla
clock = pygame.time.Clock()

# Inicializa el jugador
player = Player(100, 400)

# Inicializa las plataformas
platforms = [
    Platform(0, 450, 10000, 100),
    Platform(300, 350, 200, 20),
    Platform(500, 250, 200, 20),
    Platform(700, 150, 200, 20),
    Platform(900, 350, 200, 20),
    Platform(1300, 350, 200, 20)

]

# Inicializa los enemigos
enemies = [
    Enemy(200, 400, 50, 50, 2),  # Ajusta la posición Y para que esté en la misma altura que el suelo
    Enemy(600, 400, 50, 50, 2)   # Ajusta la posición Y para que esté en la misma altura que el suelo
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

    # Desplaza la cámara en función de la posición del jugador
    camera_x = player.x - screen_width / 2 + player.width / 2
    camera_y = player.y - screen_height / 2 + player.height / 2

    # Dibuja el fondo
    screen.fill((255, 255, 255))

    # Dibuja las plataformas
    on_platform = False
    '''
    for platform in platforms:
        platform.draw(screen)'''
    for platform in platforms:
        # Desplaza las plataformas según la posición de la cámara
        platform_x = platform.x - camera_x
        platform_y = platform.y - camera_y
        pygame.draw.rect(screen, (0, 0, 255), (platform_x, platform_y, platform.width, platform.height))

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

    # Dibuja los enemigos
    for enemy in enemies:
        enemy.update()
        enemy.draw(screen, camera_x, camera_y)

        # Verifica la colisión con el jugador
        if enemy.collide(player):
            print("¡Colisión con enemigo!")
            # Aquí puedes agregar la lógica para manejar la colisión, como reiniciar el nivel o restar vidas


    # Dibuja al jugador
    player_x = player.x - camera_x
    player_y = player.y - camera_y
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player.width, player.height))


    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de actualización de la pantalla
    clock.tick(60)

# Cierra Pygame
pygame.quit()
