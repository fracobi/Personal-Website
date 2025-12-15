import pygame
import sys

class Grid:
    def __init__(self):    
        self.size = (CELL_SIZE, CELL_SIZE)
        self.casella = pygame.Surface((self.size))
        self.casella.fill((255, 255,255))
        self.draw_grid()
    
    def draw_grid(self):
        i = 0 
        j = 0
        for j in range(CELL_NUMBER):
            for i in range(CELL_NUMBER):
                if i % 2 == 0 and j % 2 == 0:
                    win.blit(self.casella, (i * CELL_SIZE, j * CELL_SIZE))
                elif i % 2 != 0 and j % 2 != 0: 
                    win.blit(self.casella, (i * CELL_SIZE, j *CELL_SIZE ))

CELL_SIZE = 80
CELL_NUMBER = 10

win = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER)) 
pygame.init()

while True:
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit()
    win.fill ((50, 50, 50))
    Grid().draw_grid()
    pygame.display.flip()