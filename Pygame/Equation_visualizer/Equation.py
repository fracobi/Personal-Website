import pygame   
import sys
import math

class main:
    def __init__(self):
        self.y_start = (0, WINDOW_HEIGHT/2)
        self.y_end = (WINDOW_WHIDTH, WINDOW_HEIGHT/2)
        self.x_start = (WINDOW_WHIDTH/2, 0)
        self.x_end = (WINDOW_WHIDTH/2, WINDOW_HEIGHT)
        self.scale = 100
                
    def draw_graph(self):
        pygame.draw.line(win, (255, 255, 255), self. x_start, self.x_end, 2)
        pygame.draw.line(win, (255, 255, 255), self. y_start, self.y_end, 2)
        
    def draw_dot(self, x, y):
        bars = pygame.Rect (x + CENTER[0] , y + CENTER[1], 5, 5)
        pygame.draw.rect(win, (255, 0, 0), bars)
        
        
    def draw_equation(self):
        for y in range ( -WINDOW_HEIGHT, WINDOW_HEIGHT):
            for x in range (-WINDOW_WHIDTH, WINDOW_WHIDTH):
                for event in pygame.event.get():
                    if ( event.type == pygame.QUIT ):
                        run = True    
                        pygame.quit()
                        sys.exit()
            
                (x, y) = (x, -x**2 )
                # print (x, y)
                self.draw_dot(x, y)

WINDOW_WHIDTH = 1200
WINDOW_HEIGHT = 800
CENTER = (WINDOW_WHIDTH/2, WINDOW_HEIGHT/2)


pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

main = main()

run = False
while not run:    
    win.fill((30, 30, 30))
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit()
    
    main.draw_graph()
    main.draw_equation()
    pygame.display.flip()
        