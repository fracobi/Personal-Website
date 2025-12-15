import pygame, sys, random
from pygame.math import Vector2
from math import sin, cos, radians


class main ():
    def __init__(self):
        self.screen_walls = []
        self.walls = []
        self.rays = []
        
        # Gets Initial Screen Cordinatates
        WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.get_surface().get_size()

        # Build random walls    
        for j in range (10):
            a = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
            b = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))

            self.wall = Wall(a,b)
            self.walls.append(self.wall)

            self.screen_walls.append(Wall((0, 0), (WINDOW_WIDTH, 0)))
            self.screen_walls.append(Wall((0, WINDOW_HEIGHT), (WINDOW_WIDTH, WINDOW_HEIGHT)))
            self.screen_walls.append(Wall((0, 0), (0, WINDOW_HEIGHT)))
            self.screen_walls.append(Wall((WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)))

        # Build the rays
        for i in range(0, 360, 5):
            angle = radians(i)
            dir = Vector2(cos(angle), sin(angle))
            ray = Ray(dir)
            self.rays.append(ray)
            
    # Updating function 
    def update(self):
        self.screen_walls = [] # Empty the screen's wall list
        # Get live screen coordinates
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = pygame.display.get_surface().get_size()
        
        # Updating screen wall list
        self.screen_walls = [
            Wall((0, 0), (self.WINDOW_WIDTH, 0)),  # top
            Wall((0, self.WINDOW_HEIGHT), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)),  # bottom
            Wall((0, 0), (0, self.WINDOW_HEIGHT)),  # left
            Wall((self.WINDOW_WIDTH, 0), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))  # right
        ]   

        tot_walls = self.walls + self.screen_walls # All walls 
        
        # Draw the walls
        for wall in tot_walls:
            Wall.draw_wall(wall)

        # Computing distances (iterating over the whole ray's list)
        for ray in self.rays:
            ray.update_pos() # Update mouse position
            closest_point = None # Initialize the closest point to the mouse
            min_distance = float('inf') # Initialize the distance variable between the mouse and the closest point
            
            for wall in tot_walls: # iterating over the whole ray's list               
                hit, point= Ray.check(ray, wall) # Check if wall and ray intersect, and getting the point of intersection
                if hit:
                    dist = Vector2(point).distance_to(ray.pos) # Computing the distance between the mouse and the point of intersection
                    # Selecting the shortest distances between the mouse and all the walls
                    if dist < min_distance: 
                        min_distance = dist
                        closest_point = point

            # Draw the ray
            if closest_point:
                pygame.draw.line(win, (255, 255, 100), ray.pos, closest_point, 2)
                

                            
class Wall():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw_wall(self):
        pygame.draw.line(win, (255, 255, 255), self.a, self.b, 4 )
        

class Ray():
    def __init__(self, dir):
        self.dir = dir
           
    def update_pos(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.pos = Vector2(self.mouseX, self.mouseY)
  
    # Verify if a segment intersect an infinite line 
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
            self.point = (0,0)
            return False, None
        
        self.t = self.num_t / self.denominatore
        self.u = self.num_u / self.denominatore 
    
        if 0 <= self.t <= 1 and self.u >= 0:
            self.point = (self.x1 + self.t*(self.x2-self.x1), self.y1+self.t*(self.y2-self.y1))
            
            return True, self.point
        return False, None
       
# === Initialization===

pygame.init()
win = pygame.display.set_mode((1200, 650 ), pygame.RESIZABLE) # Open a new window and make it resizable
pygame.display.set_caption("Ray-tracing")


# === Main Loop ===

main = main()


run = True
while run:
    
    win.fill((20, 20, 20))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = False
    
    main.update()
    pygame.display.flip()

pygame.quit()
sys.exit()