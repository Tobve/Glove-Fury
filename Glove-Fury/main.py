import pygame
import sys
from button import Button

pygame.init()

#Definición de la pantalla y carga de imágenes
screen = pygame.display.set_mode((1405, 900))
pygame.display.set_caption("Glove Fury")

OptionsBG = pygame.image.load("assets/Faceoff.png")
BG = pygame.image.load("assets/Background.png")
pygame.mixer.music.load('sonido/1303905_Electronic-Nightmare.mp3')
pygame.mixer.music.play(-1)

#Función para obtener una fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#Función para la pantalla de juego
def play():
    #No toques las direcciones de las imagenes el juego ya esta dentro de la carpeta no hace falta que pongas el "Glove-Fury"
    imagen = pygame.image.load("assets/octagono.png").convert_alpha()
    Peleador1 = pygame.image.load("assets/Boxeador.png").convert_alpha()
    Peleador2 = pygame.image.load("assets/Boxeador2.png")
    Vida_Rojo = pygame.image.load("assets/VidaRojo.png")
    Vida_Azul = pygame.image.load("assets/VidaAzul.png")
    Golpear1 = pygame.image.load("assets/Golpe1.png")
    Golpear2 = pygame.image.load("assets/Golpe2.png")
    Ganador_Azul = pygame.image.load("assets/GanadorAzul.png")
    Ganador_Rojo = pygame.image.load("assets/GanadorRojo.png")
     
    #Variables para las posiciones
    Peleador1_x = -320
    Peleador1_Y = 50
    Peleador2_x = 1200
    Peleador2_Y = 50

    #Variable para añadir velocidad
    Velocidad = 10
    
    #Variables de golpeos
    Golpe_rojo = 0
    Golpe_azul = 0
    
    #Variable de teclas para que no puedan hacer daño manteniendo
    P_Pressed = False
    Q_Pressed = False

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(imagen, [0, 0])

        #Variables para las teclas
        Tecla = pygame.key.get_pressed()
        
        #Movimientos del peleador rojo
        if Tecla[pygame.K_a]:
            Peleador1_x -= Velocidad
        if Tecla[pygame.K_d]:
            Peleador1_x += Velocidad

        #Colisiones del peleador rojo
        if Peleador1_x < 0:
            Peleador1_x = 0
        if Peleador1_x > Peleador2_x - 196:
            Peleador1_x = Peleador2_x - 196

        #Movimientos del peleador azul
        if Tecla[pygame.K_LEFT]:
            Peleador2_x -= Velocidad
        if Tecla[pygame.K_RIGHT]:
            Peleador2_x += Velocidad

        #Colisiones del peleador azul
        if Peleador2_x > 1200:
            Peleador2_x = 1200
        elif Peleador2_x < Peleador1_x + 196:
            Peleador2_x = Peleador1_x + 196
        elif Peleador2_x < Peleador1_x + Peleador1.get_width() - 1:
            Peleador2_x = Peleador1_x + Peleador1.get_width() - 1

        #Detección de golpes y animaciones
        if Tecla[pygame.K_q] and not Q_Pressed:
            Q_Pressed = True
            if Peleador1_x - 270 <= Peleador2_x <= Peleador1_x - 270 + Golpear1.get_width() -196:
                Golpe_rojo += 1
            screen.blit(Golpear1, (Peleador1_x - 270, Peleador1_Y))
        elif not Tecla[pygame.K_q]:
            Q_Pressed = False
            screen.blit(Peleador1, (Peleador1_x, Peleador1_Y))
        else:
            screen.blit(Peleador1, (Peleador1_x, Peleador1_Y))

        if Tecla[pygame.K_p] and not P_Pressed:
            P_Pressed = True
            if Peleador2_x + 270 >= Peleador1_x >= Peleador2_x + 270 - Golpear2.get_width() +196:
                Golpe_azul += 1
            screen.blit(Golpear2, (Peleador2_x - 390, Peleador2_Y))
        elif not Tecla[pygame.K_p]:
            P_Pressed = False
            screen.blit(Peleador2, (Peleador2_x, Peleador2_Y))
        else:
            screen.blit(Peleador2, (Peleador2_x, Peleador2_Y))

        #Barra de vida
        Vida_Largo = 477
        Vida_Alto = 27
        Vida_RojoX = 112
        Vida_RojoY = 31
        Vida_AzulX = 812
        Vida_AzulY = 31

        screen.blit(Vida_Rojo, [100, 0])
        screen.blit(Vida_Azul, [800, 0])
        
        longitud_barra_azul = Vida_Largo - Golpe_rojo * 15 #Daño
        longitud_barra_rojo = Vida_Largo - Golpe_azul * 15 #Daño
        
    #Dibujar las barras de vida (parte inerior)
        pygame.draw.rect(screen, (255, 0, 0), (Vida_RojoX, Vida_RojoY, longitud_barra_rojo, Vida_Alto))
        pygame.draw.rect(screen, (0, 0, 255), (Vida_AzulX, Vida_AzulY, longitud_barra_azul, Vida_Alto))
        
        if longitud_barra_rojo <= 0:
            screen.blit(Ganador_Azul, [450, 200])
            pygame.display.update()
            pygame.time.delay(3000)  
            pygame.mixer.music.play(3)
            return
        
        if longitud_barra_azul <= 0:
            screen.blit(Ganador_Rojo, [450, 200])
            pygame.display.update()
            pygame.time.delay(3000)  
            pygame.mixer.music.play(3)
            return
        
        pygame.mixer.music.stop()
        pygame.display.flip()
        pygame.display.update()
    
#Función para la pantalla de opciones
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(OptionsBG, (0, 0))

        OPTIONS_TEXT = get_font(45).render("Opciones", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(700, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(700, 760), text_input="Inicio", font=get_font(75), base_color="Black", hovering_color="White")
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

#Función para la pantalla principal del menú
def main_menu():
    PLAY_BUTTON = Button(image=pygame.image.load("assets/OptionsButton.png"), pos=(700, 250), text_input="Boxear", font=get_font(47), base_color="White", hovering_color="Black")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/OptionsButton.png"), pos=(700, 400), text_input="Ajustes", font=get_font(47), base_color="White", hovering_color="Black")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/OptionsButton.png"), pos=(700, 550), text_input="Miedo?", font=get_font(47), base_color="White", hovering_color="Black")

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

main_menu()
