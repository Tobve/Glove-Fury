mport pygame
import sys
from button import Button  # Asumo que tienes un módulo llamado 'button' que contiene la clase Button

pygame.init()

# Definición de la pantalla y carga de imágenes
screen = pygame.display.set_mode((1420, 885))
pygame.display.set_caption("Glove Fury")

OptionsBG = pygame.image.load("Pygame-main/Glove-Fury/assets/Faceoff.png")
BG = pygame.image.load("Pygame-main/Glove-Fury/assets/Background.png")
pygame.mixer.music.load('Pygame-main/Glove-Fury/sonido/1303905_Electronic-Nightmare.mp3')
pygame.mixer.music.play(3)

# Función para obtener una fuente
def get_font(size):
    return pygame.font.Font("Pygame-main/Glove-Fury/assets/font.ttf", size)

# Función para la pantalla de juego
def play():
    imagen = pygame.image.load("Pygame-main/Glove-Fury/assets/octagono.png").convert()
    Peleador1 = pygame.image.load("Pygame-main/Glove-Fury/assets/Boxeador.png").convert_alpha()
    Peleador2 = pygame.image.load("Pygame-main/Glove-Fury/assets/Boxeador2.png")
    Vida_Rojo = pygame.image.load("Pygame-main/Glove-Fury/assets/VidaRojo.png")
    Vida_Azul = pygame.image.load("Pygame-main/Glove-Fury/assets/VidaAzul.png")
    Golpear1 = pygame.image.load("Pygame-main/Glove-Fury/assets/Golpe1.png")
    Golpear2 = pygame.image.load("Pygame-main/Glove-Fury/assets/Golpe2.png")

    # Variables para las posiciones
    Peleador1_x = -320
    Peleador1_Y = 30
    Peleador2_x = 1200
    Peleador2_Y = 30

    # Variable para añadir velocidad
    Velocidad = 20

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(imagen, [0, 0])

        # Variables para las teclas
        Tecla = pygame.key.get_pressed()

        # Movimientos del peleador rojo
        if Tecla[pygame.K_a]:
            Peleador1_x -= Velocidad
        if Tecla[pygame.K_d]:
            Peleador1_x += Velocidad

        # Colisiones del peleador rojo
        if Peleador1_x < 0:
            Peleador1_x = 0
        if Peleador1_x > Peleador2_x - 196:
            Peleador1_x = Peleador2_x - 196

        # Movimientos del peleador azul
        if Tecla[pygame.K_LEFT]:
            Peleador2_x -= Velocidad
        if Tecla[pygame.K_RIGHT]:
            Peleador2_x += Velocidad

        # Colisiones del peleador azul
        if Peleador2_x > 1200:
            Peleador2_x = 1200
        elif Peleador2_x < Peleador1_x + 196:
            Peleador2_x = Peleador1_x + 196
        elif Peleador2_x < Peleador1_x + Peleador1.get_width() - 1:
            Peleador2_x = Peleador1_x + Peleador1.get_width() - 1

        # Detección de golpes y animaciones
        if Tecla[pygame.K_q]:
            screen.blit(Golpear1, (Peleador1_x - 270, Peleador1_Y))
        else:
            screen.blit(Peleador1, (Peleador1_x, Peleador1_Y))

        if Tecla[pygame.K_p]:
            screen.blit(Golpear2, (Peleador2_x - 390, Peleador2_Y))
        else:
            screen.blit(Peleador2, (Peleador2_x, Peleador2_Y))

        # Barra de vida
        Vida_Largo = 477
        Vida_Alto = 27
        Vida_RojoX = 112
        Vida_RojoY = 31
        Vida_AzulX = 812
        Vida_AzulY = 31

        screen.blit(Vida_Rojo, [100, 0])
        screen.blit(Vida_Azul, [800, 0])

        pygame.draw.rect(screen, (255, 0, 0), (Vida_RojoX, Vida_RojoY, 477, 27))
        pygame.draw.rect(screen, (0, 0, 255), (Vida_AzulX, Vida_AzulY, 477, 27))

        pygame.display.flip()
        pygame.display.update()

# Función para la pantalla de opciones
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(OptionsBG, (0, 0))

        OPTIONS_TEXT = get_font(45).render("Opciones", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(700, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(700, 760),
                             text_input="Inicio", font=get_font(75), base_color="Black", hovering_color="White")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Función para la pantalla principal del menú
def main_menu():
    PLAY_BUTTON = Button(image=pygame.image.load("Pygame-main/Glove-Fury/assets/OptionsButton.png"), pos=(700, 250),
                         text_input="Boxear", font=get_font(47), base_color="White", hovering_color="Black")
    OPTIONS_BUTTON = Button(image=pygame.image.load("Pygame-main/Glove-Fury/assets/OptionsButton.png"), pos=(700, 400),
                            text_input="Ajustes", font=get_font(47), base_color="White", hovering_color="Black")
    QUIT_BUTTON = Button(image=pygame.image.load("Pygame-main/Glove-Fury/assets/OptionsButton.png"), pos=(700, 550),
                         text_input="Miedo?", font=get_font(47), base_color="White", hovering_color="Black")

    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Glove Fury", True, "#E19226")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Llamada a la pantalla principal del menú
main_menu()
