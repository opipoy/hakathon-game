#!/usr/bin/python3
import pygame
from objects import *

levels = {0 : [
    {'obj': ground, 'pos': (0, 700), 'size': (1000, 100)},
    {'obj': ground, 'pos': (600, 600), 'size': (100, 100)},
    {'obj': player, 'pos':(0, 700), 'size': (100, 100)},
    {'obj': player, 'pos': (10, 10), 'size': (5, 5)}
               ]
}


pygame.init()

def update_obj_on_lvl():
    for objec in obj_list:
        objec.update()


screen = pygame.display.set_mode((1000, 800))

# p = player(screen=screen)
# p.scale(100, 100)
# p.make_on_pos(10, 10)        

# g = ground(screen=screen)

# g.scale(1000, 100)
# g.make_on_pos(0, 700)
for lvl in levels[0]:

    objec = lvl["obj"](screen)
    if player.__name__ == lvl["obj"].__name__:
        players.append(objec)
    objec.make_on_pos(*lvl["pos"])
    objec.scale(*lvl["size"])
    obj_list.append(objec)
    objec.update()

running = True

pygame.display.flip()

while running:
    screen.fill("black")
    update_obj_on_lvl()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        for p in players:
            p.velocity[0] = 1
    if key[pygame.K_LEFT]:
        for p in players:
            p.velocity[0] = -1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            for p in players:
                key = pygame.key.get_pressed()
                if p.on_ground:
                    if key[pygame.K_UP]:
                            p.move(y=-0.5)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()


