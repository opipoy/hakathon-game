#!/usr/bin/python3
import pygame
from objects import *
WIDTH, HEIGHT = 800, 600
levels = {0 : [
    {'obj': ground, 'pos': (0, HEIGHT-50), 'size': (400, 50)},
    {'obj': ground, 'pos': (550, HEIGHT - 50), 'size': (200, 50)},
    {'obj': player, 'pos':(0, 250), 'size': (50, 50)},
    {'obj': player, 'pos':(100, 250), 'size': (50, 50)},
               ]
}


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
players_list = players.sprites()
while running:
    screen.fill("black")
    update_obj_on_lvl(screen)
    key = pygame.key.get_pressed()

    #for first player

    if key[pygame.K_d]:
        players_list[0].velocity[0] = 20/0.6
    if key[pygame.K_a]:
        players_list[0].velocity[0] = -20/0.6
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if players_list[0].on_ground:
                #jump first player
                if key[pygame.K_w]:
                        players_list[0].velocity[1] = -18
            if players_list[1].on_ground:
                #jump second
                if key[pygame.K_UP]:
                    players_list[1].velocity[1] = -18
    #second player
    if key[pygame.K_RIGHT]:
        players_list[1].velocity[0] = 20/0.6
    if key[pygame.K_LEFT]:
        players_list[1].velocity[0] = -20/0.6


    #on player death
    for p in players:
        if p.rect.y > HEIGHT:
            game_over(screen)
            running = False
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(30)
    pygame.display.flip()
