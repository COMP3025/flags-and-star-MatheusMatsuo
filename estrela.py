import sys

import math

import pygame
from pygame.draw import polygon
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')


def calcular_pontos_pentagono(position, size):
  angle = math.radians(360 / 5)
  points = []
  for i in range(5):
    x = int(position[0] + size * math.cos(i * angle))
    y = int(position[1] + size * math.sin(i * angle))
    points.append((x, y))
  return points


def rotacao(point, angle):
  x_rot = point[0] * math.cos(angle) - point[1] * math.sin(angle)
  y_rot = point[0] * math.sin(angle) + point[1] * math.cos(angle)
  return (x_rot, y_rot)


def draw_star(screen, position, size, angle):
  angle = math.radians(angle)
  pontosPentagono = calcular_pontos_pentagono(position, size)
  pontosRotacionados = []
  for ponto in pontosPentagono:
    ponto_rotacionado = rotacao(ponto, angle)
    pontosRotacionados.append((ponto_rotacionado[0] + position[0],
                               ponto_rotacionado[1] + position[1]))

  pygame.draw.polygon(screen, (255, 255, 0), [
      pontosRotacionados[0], pontosRotacionados[3], pontosRotacionados[1],
      pontosRotacionados[4], pontosRotacionados[2], pontosRotacionados[0]
  ])


while True:
  draw_star(DISPLAYSURF, (53, 55), 60, -17)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
