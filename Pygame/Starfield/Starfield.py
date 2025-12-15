import pygame
import random
import sys

def mapp(n, start1, stop1, start2, stop2):
   return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

def translate( coords):
    # Sposta l'origine al centro dello schermo        
    return (WINDOW_WHIDTH/2 + coords[0], WINDOW_HEIGHT/2 + coords[1])
    # return (pygame.mouse.get_pos()[0] + coords[0], pygame.mouse.get_pos()[1] + coords[1])               

class Starfield():
    def __init__(self):
        self.stars = []
        for i in range (500):
            self.star = Star()
            self.stars.append(self.star)

    def show(self ):    
        for i in range (len(self.stars)):
            Star.update(self.stars[i])
            Star.make_coords(self.stars[i])
            Star.draw_star(self.stars[i])


class Star():
    def __init__(self):
        self.x = random.randint(-WINDOW_WHIDTH/2,  WINDOW_WHIDTH/2)
        self.y = random.randint(-WINDOW_WHIDTH/2, WINDOW_HEIGHT/2)
        self.z = random.randint(1, WINDOW_WHIDTH)   
        self.pre_z = self.z
        
    def update(self):
        self.speed = mapp(pygame.mouse.get_pos()[0], 0, WINDOW_WHIDTH, 0.1, 50)
        
        self.z = self.z - self.speed
        if self.z < 1:
            self.z = WINDOW_WHIDTH
            self.x = random.randint(-WINDOW_WHIDTH/2,  WINDOW_WHIDTH/2)
            self.y = random.randint(-WINDOW_HEIGHT/2, WINDOW_HEIGHT/2)  
            self.pre_z = self.z
        
    def make_coords(self):
        self.sx = mapp(float(self.x / self.z), 0, 1, 0, WINDOW_WHIDTH/2 )
        self.sy = mapp(float(self.y / self.z), 0, 1, 0, WINDOW_HEIGHT/2 )

        self.pre_x = mapp(float(self.x / self.pre_z), 0, 1, 0, WINDOW_WHIDTH/2)
        self.pre_y = mapp(float(self.y / self.pre_z), 0, 1, 0, WINDOW_HEIGHT/2 )
        
        self.coords = translate((self.sx, self.sy))
         
        self.start = translate((self.pre_x, self.pre_y))
        self.end = self.coords
    
    def draw_star(self):        
                 
        self.radius = mapp(self.z, 0, WINDOW_HEIGHT, 3, 0)
        self.star = pygame.draw.circle(win, (255, 255, 255), (self.coords), self.radius )
        self.line = pygame.draw.line(win, (255, 255, 255), (self.start), (self.end))
        
        self.pre_z = self.z
          

WINDOW_WHIDTH = 850
WINDOW_HEIGHT = 850
speed = 50


pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

starfield = Starfield()

run = False
while not run:
    win.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True
            pygame.quit()
            sys.exit()

    starfield.show()
    
    
    pygame.display.flip()