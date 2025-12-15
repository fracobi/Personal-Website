import random
import pygame 
import sys

conto = 0 

class Bars:
    def __init__(self, x, y, whidth, height):
        self.x = x
        self.y = y
        self.whidth = whidth
        self.height = height
        
    def draw_bars(self):
        bars = pygame.Rect (self.x, self.y, self.whidth, self.height)
        pygame.draw.rect(win, (255, 255, 255), bars,1)
                
    def draw_pivot(self):
        bars = pygame.Rect (self.x, self.y, self.whidth, self.height)
        pygame.draw.rect(win, (255, 0, 0), bars, 1)


def new_list():
    lista = []
    for i in range(750):
        n  = random.randint(1,750)
        # while n in lista:
        #     n = random.randint(1, 750)
        # else:
        lista.append(n)
    return lista

def quick_sort(list, l, r):
    if l >= r:
        return 
    
    p = partition(list, l, r)
    quick_sort(list, l, p-1)
    quick_sort(list, p+1, r)

    return list, conto

def partition (list, l, r):
    global conto  
    pivot = list[r]  
    i = l-1  
    for j in range(l, r):       
        if list[j] < pivot: 
            i += 1
            (list[j], list[i]) = swap(list[j], list[i])
            conto += 1
            draw_bars()
    (list[i + 1], list[r]) = swap(list[i + 1], list[r])
    return i+1
        
def swap(a, b):
    temp = a 
    a = b 
    b = temp   
    return a, b

def draw_bars():
    for e in range(len(lista)-1): 
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                run = True    
                pygame.quit()
                sys.exit() 
        Bars( (e*CELL_SIZE_W)+10, WINDOW_HEIGHT , CELL_SIZE_H, (lista[e]*CELL_SIZE_H) - WINDOW_HEIGHT).draw_bars()
    pygame.display.flip()
    clock.tick(300)
    win.fill((0, 0, 0))

lista = new_list()
l = 0
r = len(lista)-1


CELL_SIZE_W = 2
CELL_SIZE_H = 1
CELL_NUMBER = 750
WINDOW_WHIDTH = CELL_SIZE_W * CELL_NUMBER
WINDOW_HEIGHT = CELL_SIZE_H * CELL_NUMBER

pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

run = False
while not run:    
    win.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit() 
    if keys[pygame.K_n]:
        lista = new_list()
        l = 0
        r = len(lista)-1
        draw_bars()
        
    if keys[pygame.K_SPACE]:   
        quick_sort(lista, l, r)
