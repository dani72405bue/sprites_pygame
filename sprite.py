import sys
import pygame

class Cuadrado(pygame.sprite.Sprite): # definir sprite cuadrado heredando de pygame.sprite.Sprite
    def __init__(self): # constructor del sprite cuadrado
        super().__init__() # inicializar el sprite base de pygame
        self.image = pygame.Surface((80, 80)) # crear superficie de 80x80 píxeles
        self.image.fill((255, 0, 0)) # rellenar la superficie con color rojo
        self.rect = self.image.get_rect() # obtener el rectángulo que delimita la imagen
        self.rect.x = 200 # posición inicial en el eje x
        self.rect.y = 200 # posición inicial en el eje y
        self.DESPLAZAMIENTO = 3 # velocidad de desplazamiento en píxeles por frame

    def update(self): # método update que se llama cada frame
        self.rect.x += self.DESPLAZAMIENTO # mover el sprite horizontalmente

        if self.rect.x >= 320: # si llega al borde derecho permitido
            self.rect.x = 320 # fijar la posición en el borde derecho
            self.DESPLAZAMIENTO = -3 # invertir dirección hacia la izquierda

        elif self.rect.x <= 0: # si llega al borde izquierdo permitido
            self.rect.x = 0 # fijar la posición en el borde izquierdo
            self.DESPLAZAMIENTO = 3 # invertir dirección hacia la derecha


def main(): # función principal del programa
    pygame.init() # inicializar pygame
screen = pygame.display.set_mode((400, 400)) # crear ventana de 400x400 píxeles
BG = pygame.Surface(screen.get_size()) # crear superficie de fondo del tamaño de la pantalla
BG.fill((0, 0, 255)) # rellenar el fondo con color azul
pygame.display.set_caption("freaking chicken") # establecer el título de la ventana
clock = pygame.time.Clock() # crear reloj para controlar los fps

all_sprites = pygame.sprite.Group() # crear grupo de sprites
cuadrado_sprite = Cuadrado() # crear instancia del sprite cuadrado
all_sprites.add(cuadrado_sprite) # añadir el sprite al grupo

running = True # bandera para mantener el bucle principal activo

while running: # bucle principal del juego
    for event in pygame.event.get(): # recorrer todos los eventos de pygame
        if event.type == pygame.QUIT: # si se recibe la señal de cerrar ventana
            running = False # salir del bucle principal

screen.blit(BG, (0, 0)) # dibujar el fondo en la pantalla
all_sprites.update() # actualizar todos los sprites del grupo
all_sprites.draw(screen) # dibujar todos los sprites en la pantalla

pygame.display.flip() # actualizar la pantalla completa
clock.tick(60) # limitar el juego a 60 fotogramas por segundo

pygame.quit() # cerrar pygame
sys.exit() # salir del programa


if __name__ == "__main__": # ejecutar la función principal solo si se ejecuta el archivo directamente
    main() # iniciar el programa





