import pygame
import sys

pygame.init()

#Resolucion de la pantalla
size = (1405, 900)

#Aqui vamos a crear la ventana

screen = pygame.display.set_mode(size)
#Para cargar las imagenes
image = pygame.image.load("boxeo2.png").convert()


#Y aqui ponemos el evento para cuando quieras cerrarlo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            sys.exit()
    screen.blit(image, [0, 0])
    pygame.display.flip()
  




