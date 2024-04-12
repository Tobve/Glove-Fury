import sys
import pygame
from moviepy.editor import *


pygame.init()

#Resolucion de la pantalla
size = (1405, 900)

#Aqui vamos a crear la ventana

screen = pygame.display.set_mode(size)
#Para cargar las imagenes
imagen = pygame.image.load("boxeo2.png").convert()

gif= VideoFileClip("andre-antunes-i-foot-work.gif")
frames = gif.iter_frames()

#Y aqui ponemos el evento para cuando quieras cerrarlo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            sys.exit()
    screen.blit(imagen, [0, 0])
    frame = next(frames, None)
    if frame is None:
        frames = gif.iter_frames()
        frame = next(frames, None)

    screen.blit(pygame_frame, (0, 0))


    pygame.display.flip()
  




