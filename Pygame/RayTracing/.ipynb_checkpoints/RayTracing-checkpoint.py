import pygame, sys, random
from pygame.math import Vector2
from math import sin, cos, radians

# a = Vector2(100, 100)
# b = Vector2(200, 200)

# c = b.length() - a.length()
# print (a.length())
# print (b.length())
# print (c)

class main ():
    def __init__(self):
        self.walls = []
         
        for j in range (5):
            self.h1 = Wall((0, 0), (WINDOW_WHIDTH, 0))
            self.h2 = Wall((0, WINDOW_HEIGHT), (WINDOW_WHIDTH, WINDOW_HEIGHT))
            self.v1 = Wall((0, 0), (0, WINDOW_HEIGHT))
            self.v2 = Wall((WINDOW_WHIDTH, 0), (WINDOW_WHIDTH, WINDOW_HEIGHT))
            
            self.prova1 = Wall((200, 200), (200, 600))
            self.prova2 = Wall((300, 200), (300, 600))
            
            self.wall = Wall((random.randint(0, WINDOW_WHIDTH), random.randint(0, WINDOW_HEIGHT)), (random.randint(0, WINDOW_WHIDTH), random.randint(0, WINDOW_HEIGHT))  )
            self.walls.append(self.wall)
            # self.walls.append(self.prova1)
            # self.walls.append(self.prova2)
            # self.walls.append(self.h1)
            # self.walls.append(self.h2)
            # self.walls.append(self.v1)
            # self.walls.append(self.v2)
        
        self.rays = []
        for i in range (360):
            if i % 360 == 1:
                angle = radians(i)
                self.ray = Ray(Vector2(cos(angle)*WINDOW_WHIDTH, sin(angle)*WINDOW_HEIGHT))
                self.rays.append(self.ray)
        
    def update(self):
        self.point = Vector2()
        for j in range(len(self.walls)):
            Wall.draw_wall(self.walls[j])

        for i in range (len(self.rays)):
            Ray.draw_ray(self.rays[i])
            self.record = WINDOW_WHIDTH
            for j in range(len(self.walls)):
                if Ray.check(self.rays[i], self.walls[j]):
                    # traslare su self.pos e poi da li vedere la lunghezza del vettore da pos a self.point
                    self.distance = Vector2(Ray.translate(self.rays[i], self.rays[i].pos)).length()            
                    
                    # pygame.draw.line(win, (255, 255, 100), self.rays[i].pos, self.rays[i].point, 1)
                    print (self.distance)
                    if self.distance < self.record:
                        self.point = Vector2(self.rays[i].point)
                        self.record = self.distance 
                        pygame.draw.line(win, (255, 255, 100), self.rays[i].pos, self.point, 1)
                    else:    
                        pygame.draw.line(win, (255, 255, 100), self.rays[i].pos, self.rays[i].point, 1)
                    
                        
class Wall():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def draw_wall(self):
        pygame.draw.line(win, (255, 255, 255), self.a, self.b, 4 )
        

class Ray():
    def __init__(self, Vector2):
        self.dir = Vector2

    def draw_ray(self):
        self.mouseX = pygame.mouse.get_pos()[0]
        self.mouseY = pygame.mouse.get_pos()[1]
        
        self.pos = Vector2(self.mouseX, self.mouseY)
        
        # pygame.draw.line(win, (255, 255, 255, 100), self.pos, self.pos+self.dir, 2)
    
    def check(self, wall):
        
        self.x1 = wall.a[0]
        self.y1 = wall.a[1]
        self.x2 = wall.b[0]
        self.y2 = wall.b[1]
        
        self.x3 = self.pos[0]
        self.y3 = self.pos[1]
        self.x4 = self.pos[0] + self.dir[0]
        self.y4 = self.pos[1] + self.dir[1]

        self.num_t = (self.x1-self.x3)*(self.y3-self.y4)-(self.y1-self.y3)*(self.x3-self.x4)
        self.num_u = (self.x2-self.x1)*(self.y1-self.y3)-(self.y2-self.y1)*(self.x1-self.x3)
        self.denominatore = (self.x1-self.x2)*(self.y3-self.y4)-(self.y1-self.y2)*(self.x3-self.x4)
        
        if self.denominatore == 0:
            return
        
        self.t = self.num_t / self.denominatore
        self.u = self.num_u / self.denominatore 
    
        if 0 <= self.t <= 1:
            self.point = (self.x1 + self.t*(self.x2-self.x1), self.y1+self.t*(self.y2-self.y1))
            return True
        
    def translate(self, coords):
        # Sposta l'origine al centro dello schermo        
        return (self.pos[0]+ coords[0], self.pos[1] + coords[1])
        
    def mapp(self, n, start1, stop1, start2, stop2):
        return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


WINDOW_WHIDTH = 1200
WINDOW_HEIGHT = 800

pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

main = main()

run = False
while not run:
    win.fill((20, 20, 20))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True
            pygame.quit()
            sys.exit()
    
    main.update()
    pygame.display.flip()