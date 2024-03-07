import pygame, sys
from pygame.locals import * # type: ignore

pygame.init()

surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("我的pygame游戏")

while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()