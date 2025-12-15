import pygame
import random
import sys

class Bars:
    def __init__(self, x, y, whidth, height):
        self.x = x
        self.y = y
        self.whidth = whidth
        self.height = height
        
        
    def draw_bars(self, value):
        bars = pygame.Rect (self.x, self.y, self.whidth, self.height)
        pygame.draw.rect(win, (255, value, 200), bars,3)
    
        
    def draw_key(self):
        bars = pygame.Rect (self.x, self.y, self.whidth, self.height)
        pygame.draw.rect(win, (255, 60, 200), bars,3)
        
class main():
    def __init__(self):
        self.A = self.new_array()
        
    def check_input(self):
        if keys[pygame.K_n]:
            self.A = self.new_array()
          
        if keys[pygame.K_SPACE]:
            main.InsertionSort()
            
    def new_array(self):
        A = []
        for i in range(255):
            n  = random.randint(1,255)
            while n in A:
                n = random.randint(1, 255)
            else:
                A.append(n)
        return A

    def show_bars(self, i, key):
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                run = True    
                pygame.quit()
                sys.exit() 
        
        for e in range(len(self.A)-1):

            if self.A[e] == self.A[i]:
                Bars( (e*CELL_SIZE_W)+CELL_SIZE_H, WINDOW_HEIGHT - (key*CELL_SIZE_H), CELL_SIZE_H, (key*CELL_SIZE_H) ).draw_key()
            else:
                Bars( (e*CELL_SIZE_W)+CELL_SIZE_H, WINDOW_HEIGHT - (self.A[e]*CELL_SIZE_H), CELL_SIZE_H, (self.A[e]*CELL_SIZE_H)).draw_bars(self.A[e])
    
        pygame.display.flip()
        clock.tick(20)
        win.fill((30, 30, 30))

    def InsertionSort(self):
        for j in range(1, len(self.A)):
            key = self.A[j]
            i = j-1  
            while i >= 0 and self.A[i] > key:
                self.A[i+1] = self.A[i]
                i -= 1
                self.show_bars(i, key)
            self.A[i+1] = key 


CELL_SIZE_W = 6
CELL_SIZE_H = 3
CELL_NUMBER = 255
WINDOW_WHIDTH = CELL_SIZE_W * CELL_NUMBER
WINDOW_HEIGHT = CELL_SIZE_H * CELL_NUMBER

pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

main = main()

run = False
while not run:    
    win.fill((30, 30, 30, 10))
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit()
    
    main.check_input()      
    main.show_bars(0, 0)

            