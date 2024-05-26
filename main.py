#!/usr/bin/python3
import pygame
from objects import *

levels = {0 : [
    {'obj': ground, 'pos': (0, 700), 'size': (500, 50)},
    #{'obj': inviz_ground, 'pos': (500, 700), 'size': (100, 100)},
    {'obj': player, 'pos':(0, 250), 'size': (100, 100)},
   {'obj': player, 'pos': (200, 10), 'size': (10, 10)}
               ]
}


pygame.init()

screen = pygame.display.set_mode((1000, 800))

# p = player(screen=screen)
# p.scale(100, 100)
# p.make_on_pos(10, 10)

# g = ground(screen=screen)

# g.scale(1000, 100)
# g.make_on_pos(0, 700)
#יוצר אובייקים בשלב
load_level(screen, levels[0])
running = True

pygame.display.flip()

while running:
    screen.fill("black")
    update_obj_on_lvl(screen)
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        for p in players:
            p.velocity[0] = 20/0.6 
    if key[pygame.K_LEFT]:
        for p in players:
            p.velocity[0] = -20/0.6
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            for p in players:
                key = pygame.key.get_pressed()
                if p.on_ground:
                    if key[pygame.K_SPACE]:
                            p.velocity[1] = -20 - p.weight/50
                if key[pygame.K_v]:
                    game_over(screen)
                    break
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(30)
    pygame.display.flip()
