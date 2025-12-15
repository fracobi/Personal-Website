import pygame 
import random
import sys

count = 0

def bubble_sort():
    global count                  
    for k in lista_range_meno1:  
        if lista[k] > lista[k+1]:
            temp = lista[k] 
            lista [k] = lista[k+1]  
            lista[k +1] = temp 
            count += 1

    print (count)
def new_list():
    lista = []
    for i in range(130):
        n  = random.randint(1,130)
        while n in lista:
            n = random.randint(1, 130)
        else:
            lista.append(n)
    return lista

lista = new_list()

lista_range = range(130)  
lista_range_meno1 = range(129)  

CELL_SIZE_W = 11
CELL_SIZE_H = 6
CELL_NUMBER = len(lista)

WINDOW_WHIDTH = CELL_SIZE_W * CELL_NUMBER
WINDOW_HEIGHT = CELL_SIZE_H * max(lista) 
SPESSORE = WINDOW_WHIDTH // CELL_NUMBER

pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

conto = -1

run = False
while not run:    
    win.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit() 
        if keys[pygame.K_SPACE]:
            bubble_sort()
            conto -= 1
        if keys[pygame.K_n]:
            lista = new_list()
            
    for i in lista_range: 
        if max(lista[:conto]) == lista[i]:       
            pygame.draw.line(win, (0 , 0, 255), (int( i*CELL_SIZE_W), WINDOW_HEIGHT), ( int(i *CELL_SIZE_W) , WINDOW_HEIGHT - (int(lista[i]*CELL_SIZE_H))  ), SPESSORE)
            pygame.draw.line(win, (0, 0, 0), (int( i *CELL_SIZE_W) -6 , WINDOW_HEIGHT), ( int( i *CELL_SIZE_W)- 6, 0), 2)
        else:
            pygame.draw.line(win, (255, 255, 255), (int( i*CELL_SIZE_W), WINDOW_HEIGHT), ( int(i *CELL_SIZE_W) , WINDOW_HEIGHT - (int(lista[i]*CELL_SIZE_H))  ), SPESSORE)
            pygame.draw.line(win, (0, 0, 0), (int( i *CELL_SIZE_W) -6 , WINDOW_HEIGHT), ( int( i *CELL_SIZE_W)- 6, 0), 2)
    pygame.display.flip()
  

  
                        
