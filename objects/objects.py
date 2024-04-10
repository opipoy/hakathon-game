
import pygame
solids = []
obj_list = []
players = []


class template_obj():
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


class player(template_obj):
    def __init__(self, screen):
        self.jumping = False
        self.screen = screen
        self.velocity = [0, 0]
        self.gravity = 0.003
        self.on_ground = False

        super().__init__(r"./recorces/player.gif" ,screen)
       
    def move(self, x = None, y = None):
        self.velocity[0] += x if x != None else self.velocity[0]
        self.velocity[1] += y if y != None else self.velocity[1]
    
    def fall(self):
        if self.on_ground & ( self.velocity[1] > 0 ):
            self.velocity[1] = 0
        else:
            self.move(y= self.gravity)
    
    def friction(self):
        if  abs(self.velocity[0]) > 0.01:
            self.velocity[0] *= 0.3
        else:
            self.velocity[0] = 0
        
    def update(self):
        self.on_ground = len( self.check_colision(solids) ) > 0
        self.friction()
        self.fall()
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.colision.move(self.velocity[0], self.velocity[1])
        self.make_on_pos(self.x, self.y)
    
    
class ground(template_obj):
    def __init__(self, screen):
        super().__init__(r"./recorces/player.gif" ,screen)
        self.pos_on_list = len(solids)
        solids.append(self.colision)
        
    def update(self):
        solids[self.pos_on_list] = self.colision
        self.make_on_pos(self.x, self.y)