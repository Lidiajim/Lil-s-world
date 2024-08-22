#main.py donde iniciarás tu código.


from Player import Player
import pygame
from Platform import Platform
from Enemy import Enemy

def show_game_over_screen(screen, font):
    screen.fill((0, 0, 0))
    text_game_over = font.render('Game Over', True, (255, 255, 255))
    text_restart = font.render('Press R to Restart', True, (255, 255, 255))
    text_quit = font.render('Press Q to Quit', True, (255, 255, 255))

    screen.blit(text_game_over, (screen_width / 2 - text_game_over.get_width() / 2, screen_height / 2 - text_game_over.get_height()))
    screen.blit(text_restart, (screen_width / 2 - text_restart.get_width() / 2, screen_height / 2))
    screen.blit(text_quit, (screen_width / 2 - text_quit.get_width() / 2, screen_height / 2 + 40))

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def reset_game():
    global player, platforms, enemies
    player = Player(100, 400)
    platforms = [
        Platform(0, 450, 10000, 100),
        Platform(300, 350, 200, 20),
        Platform(500, 250, 200, 20),
        Platform(700, 150, 200, 20),
        Platform(900, 350, 200, 20),
        Platform(1300, 350, 200, 20)

    ]
    enemies = [
        Enemy(200, 400, 50, 50, 2),  # Ajusta la posición Y para que esté en la misma altura que el suelo
        Enemy(600, 400, 50, 50, 2)   # Ajusta la posición Y para que esté en la misma altura que el suelo
    ]

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plataforma")

# Cargar la imagen de fondo
background_image = pygame.image.load('assets/fondo1.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Variables para la cámara
camera_x = 0
camera_y = 0

# Reloj para controlar la velocidad de actualización de la pantalla
clock = pygame.time.Clock()

# Fuente para el texto
font = pygame.font.Font(None, 36)

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
game_over = False
while running:
    if game_over:
        action = show_game_over_screen(screen, font)
        if action == 'restart':
            reset_game()
            game_over = False
        elif action == 'quit':
            running = False
        continue
        
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

    '''
    # Dibuja el fondo
    screen.fill((255, 255, 255))
    '''

 # Dibuja la imagen de fondo, repitiéndola si es necesario
    bg_width, bg_height = background_image.get_size()
    for x in range(-int(camera_x) // bg_width, (screen_width - int(camera_x)) // bg_width + 2):
        for y in range(-int(camera_y) // bg_height, (screen_height - int(camera_y)) // bg_height + 2):
            screen.blit(background_image, (x * bg_width - int(camera_x) % bg_width, y * bg_height - int(camera_y) % bg_height))


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
            player.take_damage()  # Resta una vida al jugador
            print(f"¡Colisión con enemigo! Vidas restantes: {player.lives}")

            # Cambia la dirección del enemigo
            enemy.change_direction()

    # Si el jugador se queda sin vidas, muestra el menú de Game Over
    if player.lives <= 0:
        game_over = True
        continue

    # Dibuja al jugador
    player_x = player.x - camera_x
    player_y = player.y - camera_y
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player.width, player.height))

    # Dibuja el número de vidas restantes
    text = font.render(f'Vidas: {player.lives}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de actualización de la pantalla
    clock.tick(60)

# Cierra Pygame
pygame.quit()


