#!/usr/bin/python3
import pygame

solids = []

class obj():
    def __init__(self, img, screen):
        self.IMG = img
        self.screen = screen
        try:
            self.loaded_img = pygame.image.load(img)
        except pygame.error:
            print(f"Error: Image file '{img}' not found.")
            # Handle the error gracefully, e.g. by using a default image or displaying an error message to the user.
        self.H = self.loaded_img.get_height()
        self.W = self.loaded_img.get_width()
        self.x, self.y = 0 ,0
        self.colision = pygame.Rect(self.x, self.y, self.W, self.H)

    def make_on_pos(self, x, y):
        self.screen.blit(self.loaded_img, (x, y))
        self.x, self.y = x, y
        self.colision.topleft = x, y

    def scale(self, width, height):
        self.W, self.H = width, height
        self.loaded_img = pygame.transform.scale(self.loaded_img, (width, height))
        self.colision = pygame.Rect(self.x, self.y, self.W, self.H)

    def check_colision(self, rect_list):
        return self.colision.collidelistall(rect_list)


class player(obj):
    def __init__(self, screen):
        self.screen = screen
        self.velocity = [0, 0]
        self.weight = 8
        self.gravity = 0.05
        self.on_ground = False

        super().__init__(r"./recorces/000080_Navy_Blue_Square.svg" ,screen)
       
    def move(self, x = None, y = None):
        self.velocity[0] = x if x != None else self.velocity[0]
        self.velocity[1] = y if y != None else self.velocity[1]
        pygame.display.flip()
    
    def fall(self):
        if not self.on_ground:
            if self.velocity[1] >= 0:
                if self.velocity[1] <= self.weight:
                    self.move(y = self.velocity[1] + self.gravity)
        else:
            self.move(y = 0)
            if 0 < self.velocity[0]: 
                self.velocity[0] -= .1
            else:
                self.velocity[0] = 0
        
    def update(self):
        self.on_ground = self.check_colision(solids)
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.colision.move(self.velocity[0], self.velocity[1])
        self.fall()
        self.make_on_pos(self.x, self.y)
    
class ground(obj):
    def __init__(self, screen):
        super().__init__(r"./recorces/000080_Navy_Blue_Square.svg" ,screen)
        self.pos_on_list = len(solids)
        solids.append(self.colision)
        
    def update(self):
        solids[self.pos_on_list] = self.colision
        self.make_on_pos(self.x, self.y)
    


pygame.init()

screen = pygame.display.set_mode((1000, 800))

p = player(screen=screen)
p.scale(100, 100)
p.make_on_pos(10, 10)        

g = ground(screen=screen)

g.scale(1000, 100)
g.make_on_pos(0, 700)

running = True

pygame.display.flip()

while running:
    screen.fill("black")
    g.update()
    p.update()
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEMOTION:
            if p.on_ground:
                p.move(2) 
        if event.type == pygame.MOUSEBUTTONUP:
            if p.on_ground:
                p.move(y=-100)
        if event.type == pygame.QUIT:
            running = False

