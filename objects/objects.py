import pygame
solids = pygame.sprite.Group()
players = pygame.sprite.Group()
obj_list = pygame.sprite.Group()
clock = pygame.time.Clock()
dt = 0
show_col = True


class colision(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect

    def update_rect(self, rect):
        self.rect = rect


class template_obj(pygame.sprite.Sprite):
    def make_colisions(self):
        for colision_name in self.template_colisions.keys():
            template = self.template_colisions[colision_name]
            rect = pygame.Rect(self.rect.x + template[0], self.rect.y + template[1], self.rect.w + template[2], self.rect.h + template[3])
            col = colision(rect)
            self.colisions[colision_name] = col

    def update_colisions(self):
        for name, col in self.colisions.items():
            template = self.template_colisions[name]
            rect = pygame.Rect(self.rect.x + template[0], self.rect.y + template[1], self.rect.w + template[2], self.rect.h + template[3])
            pygame.draw.rect(self.screen, "orange", rect)
            col.update_rect(rect)

    def __init__(self, img, screen):
        super().__init__()
        self.IMG = img
        self.screen = screen
        self.image = pygame.image.load(img)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.h = self.image.get_height()
        self.rect.w = self.image.get_width()
        self.rect.x, self.rect.y = 0, 0
        self.colisions = {}
        self.template_colisions = {'sprite': (0, 0 ,0 ,0)}
        self.make_colisions()

    def scale(self, width, height):
        self.rect.w, self.rect.h = width, height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.update_colisions()

    def check_collisions(self, spritegroup):
        colides_with = {}
        for key, item in self.colisions.items():
            for sprite in spritegroup:
                if sprite.rect.colliderect(item):
                    colides_with[key] = sprite
        return colides_with

class player(template_obj):
    def __init__(self, screen, speed = 0, density = 0, gravity = 0,):
        self.jumping = False
        self.screen = screen
        self.velocity = [0, 0]
        self.gravity = gravity or 2
        self.on_ground = False
        self.touching_grounds = []
        self.pos_on_list = len(solids)
        super().__init__(r"./recorces/player.gif", screen)
        col_size = 0.7
        self.template_colisions["vertical"] = ((self.rect.w/col_size)/2, 0, -self.rect.w/col_size, 0)
        self.template_colisions["horizontal"] = (0, (self.rect.h/col_size)/2, 0, -self.rect.h/col_size)
        self.make_colisions()
        self.density = density or 0.1
        self.weight = self.rect.w * self.rect.h * self.density
        players.add(self)
       
    def move(self, x = 0, y = 0):
        self.velocity[0] += x
        self.velocity[1] += y
    
    def fall(self):
        if self.on_ground & ( self.velocity[1] >= 0 ):
            ground_y = self.touching_grounds["vertical"].rect.y
            y = self.rect.y
            h = self.rect.h
            self.rect.y = ground_y - h+0.5
            self.velocity[1] = 0
        elif self.velocity[1] <= self.weight:
            self.move(y= 4*dt^2)
        else:
            self.velocity[1] = self.weight
    
    def friction(self):
        if  abs(self.velocity[0]) > 0.1:
            self.velocity[0] *= 0.6
        else:
            self.velocity[0] = 0
        
    def update(self):
        # solids.add(self.colisions["sprite"])
        self.touching_grounds = self.check_collisions(solids)
        self.on_ground = "vertical" in self.touching_grounds.keys()
        print(self.touching_grounds)
        self.fall()
        self.friction()
        self.weight = self.rect.w * self.rect.h * self.density
        # TODO: for now its moving backwards... mabe make it move the colision first and then check
        if "horizontal" in self.touching_grounds:
            self.rect.x -= self.velocity[0]
        else:
            self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.update_colisions()

class ground(template_obj):
    def __init__(self, screen):
        super().__init__(r"./recorces/player.gif", screen)
        solids.add(self)

    def update(self):
        pygame.draw.rect(self.screen, "yellow", self.colisions["sprite"])

def game_over(screen):
    clear_objects()
    imp = pygame.image.load(r"./recorces/game over.jpg").convert()
    pygame.display.set_mode((imp.get_width(),imp.get_height()))
    screen.blit(imp, (0,0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def clear_objects():
    global solids, players, obj_list
    obj_list.empty()
    solids.empty()
    players.empty()

def load_level(screen, level:dict):
    clear_objects()
    for lvl in level:
        objec = lvl["obj"](screen=screen, **lvl["options"] if "options" in lvl else {})
        objec.rect.x, objec.rect.y = lvl["pos"]
        objec.scale(*lvl["size"])
        obj_list.add(objec)

def update_obj_on_lvl(screen):
    global dt
    obj_list.update()
    obj_list.draw(screen)

