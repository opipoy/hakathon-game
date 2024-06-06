#!/usr/bin/python3
import pygame
from objects import *
WIDTH, HEIGHT = 800, 600
players_obj = [
    {'obj': player, 'pos':(0, 250), 'size': (50, 50) ,"options":{"image": r"recorces/p2.png"}},
    {'obj': player, 'pos':(100, 250), 'size': (50, 50), "options":{"image": r"recorces/p1.png"}},
        ]
side_walls = [
               {'obj': ground, 'pos': (WIDTH, 0 ), 'size': (1, HEIGHT)}, #זה חוסם ימני
               {'obj': ground, 'pos': (-1, 0 ), 'size': (1, HEIGHT)}, #זה חוסם ימני
        ]

levels = {0 : [ *players_obj,*side_walls,
               {'obj': ground, 'pos': (550, HEIGHT - 50), 'size': (300, 50)},#ריצפה ימינית
               {'obj': ground, 'pos': (0, HEIGHT-50), 'size': (400, 50)},#ריצפה שמאלית
               {'obj': win_flag, 'pos': (WIDTH-50, HEIGHT-100), 'size': (50, 50), },
               ],
          1 : [ *players_obj, *side_walls,
                {'obj': ground, 'pos': (0, HEIGHT-50), 'size': (300, 50)},#ריצפה שמאלית
                {'obj': ground, 'pos': (420, HEIGHT-120), 'size': (200, 50)},#ריצפה עליונה
               {'obj': ground, 'pos': (700, HEIGHT-180), 'size': (150, 50)},#ריצפה עליונה
               {'obj': ground, 'pos': (400, 0), 'size': (150, HEIGHT), "options":{"btn_id":1}},#ריצפה עליונה
               {'obj': open_button, 'pos': (230, HEIGHT-60-50), 'size': (60, 60), "options":{"btn_id":1}},#ריצפה שמאלית
                {'obj': win_flag, 'pos': (WIDTH-50, HEIGHT-230), 'size': (50, 50), },
               ],
          2: [*players_obj, *side_walls,
                {'obj': ground, 'pos': (0, HEIGHT-50), 'size': (300, 50)},#ריצפה שמאלית
                {'obj': ground, 'pos': (300, HEIGHT-160), 'size': (50, HEIGHT)},#ריצפה עליונה
                {'obj': ground, 'pos': (700, HEIGHT-180), 'size': (150, 50)},#ריצפה עליונה
                {'obj': ground, 'pos': (300, HEIGHT-160), 'size': (150, 50)},#ריצפה עליונה
                {'obj': win_flag, 'pos': (WIDTH-50, HEIGHT-230), 'size': (50, 50), },
              ],
          3: [*players_obj, *side_walls,
                {'obj': ground, 'pos': (0, HEIGHT-200), 'size': (200, 50)},#ריצפה שמאלית
                {'obj': ground, 'pos': (200, HEIGHT-200), 'size': (200, 50), "options":{"btn_id":1}},#ריצפה שמאלית
                {'obj': ground, 'pos': (300, HEIGHT-400), 'size': (50, 200), "options":{"btn_id":2}},#ריצפה שמאלית
                {'obj': ground, 'pos': (300, HEIGHT-265), 'size': (50, 65), },#ריצפה שמאלית
               {'obj': open_button, 'pos': (200, HEIGHT-200-50), 'size': (60, 60), "options":{"btn_id":1}},#ריצפה שמאלית
                {'obj': ground, 'pos': (0, HEIGHT-50), 'size': (300, 50)},#ריצפה שמאלית
                {'obj': ground, 'pos': (300+200, HEIGHT-50), 'size': (50, 50)},#ריצפה שמאלית
                {'obj': ground, 'pos': (300+200+200, HEIGHT-50), 'size': (50, 50)},#ריצפה שמאלית
               {'obj': open_button, 'pos': (300+200+200, HEIGHT-50-50), 'size': (60, 60), "options":{"btn_id":2}},#ריצפה שמאלית
                {'obj': ground, 'pos': (300, HEIGHT-240), 'size': (300, 25), },#ריצפה שמאלית
                {'obj': win_flag, 'pos': (WIDTH-50, HEIGHT-230), 'size': (50, 50), },
              ],
          4: [{"obj" : template_obj ,'pos' : (0,0), 'size':(WIDTH, HEIGHT),"options":{"img":r"recorces/you win.png"}}]

          }

pygame.init()
# init levels on game library
init_game(levels)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# creates start level
load_level(screen, levels[0])
running = True

bg_img = pygame.image.load(r"./recorces/bg.jpg")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

pygame.display.flip()
while running:
    # gets a list of players
    
    players_list = players.sprites()
    # clears screen for next frame

    screen.blit(bg_img, (0,0))
    # draw objects
    update_obj_on_lvl(screen)
    key = pygame.key.get_pressed()

    # for first player

    if key[pygame.K_d]:
        # move right
        players_list[0].velocity[0] = 20/0.6
    if key[pygame.K_a]:
        # move left
        players_list[0].velocity[0] = -20/0.6
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # on key press + get key
            key = pygame.key.get_pressed()
            if players_list[0].on_ground:
                # jump first player + checkes if w is pressed
                if key[pygame.K_w]:
                        players_list[0].velocity[1] = -18
            if players_list[1].on_ground:
                # jump second + checkes if up is pressed
                if key[pygame.K_UP]:
                    players_list[1].velocity[1] = -18
    # second player
    if key[pygame.K_RIGHT]:
        # move right
        players_list[1].velocity[0] = 20/0.6
    if key[pygame.K_LEFT]:
        # move left
        players_list[1].velocity[0] = -20/0.6

    # on player death
    for p in players:
        if p.rect.y > HEIGHT:
            game_over(screen)
            running = False
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(30)
    pygame.display.flip()
