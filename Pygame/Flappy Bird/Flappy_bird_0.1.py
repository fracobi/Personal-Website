import pygame
import random

WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 700
  

### Importo le immagini ###
sfondo = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Flappy Bird\Images\Sfondo.png')
uccello = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Flappy Bird\Images\Uccello1.png')
tubo_su = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Flappy Bird\Images\tubo_su.png')
tubo_giu = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Flappy Bird\Images\tubo_giu.png')
terreno = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Flappy Bird\Images\terreno.png')

### Ridimensiono le immagini ###
uccello = pygame.transform.scale(uccello,(50, 35))
uccello_su = pygame.transform.rotate(uccello, 30 )
uccello_giu = pygame.transform.rotate(uccello, -30 )
terreno = pygame.transform.scale(terreno, (700, 150))

### Inizializzo le variabili ###
x = 150                                     # x iniziale dell'uccello
y = 150                                     # y iniziale dell'uccello

vel_Terreno = 0                             # x Iniziale del terreno

vert_gap = 190   
oriz_gap = 270

vel_tubo_iniz = WINDOW_WIDTH - (412 / 2)         # x iniziale del primo tubo
vel_tubo1 = vel_tubo_iniz + oriz_gap             # x iniziale del secondo tubo
vel_tubo2 = vel_tubo1 + oriz_gap                 # x iniziale del terzo tubo

pos_tubo_su_iniz = random.randint(-430, -100)                              # y iniziale del primo tubo
pos_tubo_giu_iniz = pos_tubo_su_iniz + tubo_su.get_height() + vert_gap    # y iniziale del primo tubo
pos_tubo1_su_iniz = random.randint(-430, -100)                             # y iniziale del secondo tubo
pos_tubo1_giu_iniz = pos_tubo1_su_iniz + tubo_su.get_height() + vert_gap
pos_tubo2_su_iniz = random.randint(-430, -100)                             # y iniziale del terzo tubo 
pos_tubo2_giu_iniz = pos_tubo2_su_iniz + tubo_su.get_height() + vert_gap

isJump = False                              # Variabile del salto
jumpcount = 7                               # Contatore salto salita
const = 7                                   # Contatore salto discesa
punteggio = 0

### Open the PyGame Wdinow
pygame.init()
win = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("First Game")

### Inizializzo il font per il pounteggio ###
font = pygame.font.SysFont(None, 80)                  

#allows fps rate
clock = pygame.time.Clock()


### Main Loop
run = False
while not run:
    
    # Handle Window Events, etc. #
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True   

    ### Controllo se l'uccello ha toccato i tubi ###
    
    uccello_rect = uccello.get_rect(topleft = (x,y))
    tubo_su_iniz_rect = tubo_su.get_rect(topleft = (vel_tubo_iniz, pos_tubo_su_iniz - 23))
    tubo_giu_iniz_rect = tubo_giu.get_rect(topleft = (vel_tubo_iniz, pos_tubo_giu_iniz- 8))   
    tubo1_su_rect = tubo_su.get_rect(topleft = (vel_tubo1, pos_tubo1_su_iniz - 23))
    tubo1_giu_rect = tubo_giu.get_rect(topleft = (vel_tubo1, pos_tubo1_giu_iniz - 8))  
    tubo2_su_rect = tubo_su.get_rect(topleft = (vel_tubo2, pos_tubo2_su_iniz - 23))
    tubo2_giu_rect = tubo_giu.get_rect(topleft = (vel_tubo2, pos_tubo2_giu_iniz - 8))      

    if uccello_rect.colliderect(tubo_su_iniz_rect):
        break 
    if uccello_rect.colliderect(tubo1_su_rect):
        break 
    if uccello_rect.colliderect(tubo2_su_rect):
        break 

    if uccello_rect.colliderect(tubo_giu_iniz_rect):
        break 
    if uccello_rect.colliderect(tubo1_giu_rect):
        break 
    if uccello_rect.colliderect(tubo2_giu_rect):
        break            
    
    # Incremento il punteggio di 1 se l'uccello ha superato il tubo #
    if vel_tubo_iniz == 100 or vel_tubo1 == 100 or vel_tubo2 == 100:
        punteggio += 1

    ### Disegno lo sfondo ###
    win.blit(sfondo, (0, 0))

    ### Disegno i tubi ###
    if vel_tubo_iniz <= -50:                                          # Se il tubo esce dallo schermo:
        vel_tubo_iniz = vel_tubo2 + oriz_gap                               # Alla x gli assegno quella dell'ultimo tubo, più la distanza tra i tubi
        pos_tubo_su_iniz = random.randint(-430, -100)                  # Alla y gli assegno un nuovo valore quasuale
        pos_tubo_giu_iniz = pos_tubo_su_iniz + tubo_su.get_height() + vert_gap
        win.blit(tubo_su, (vel_tubo_iniz, pos_tubo_su_iniz))          # Mostro il tubo a schero con i nuovi parametri
        win.blit(tubo_giu, (vel_tubo_iniz, pos_tubo_giu_iniz))
    else:                                                             # Se il tubo è ancora nello schermo: 
        win.blit(tubo_su, (vel_tubo_iniz, pos_tubo_su_iniz))          # Mostro a schermo il tubo con i vecchi parametri
        win.blit(tubo_giu, (vel_tubo_iniz, pos_tubo_giu_iniz))

    if vel_tubo1 <= -50:                                          
        vel_tubo1 = vel_tubo_iniz + oriz_gap                      
        pos_tubo1_su_iniz = random.randint(-430, -100)             
        pos_tubo1_giu_iniz = pos_tubo1_su_iniz + tubo_su.get_height() + vert_gap
        win.blit(tubo_su, (vel_tubo1, pos_tubo1_su_iniz))         
        win.blit(tubo_giu, (vel_tubo1, pos_tubo1_giu_iniz))
    else:                                                         
        win.blit(tubo_su, (vel_tubo1, pos_tubo1_su_iniz))         
        win.blit(tubo_giu, (vel_tubo1, pos_tubo1_giu_iniz))

    if vel_tubo2 <= -50:                                          
        vel_tubo2 = vel_tubo1 + oriz_gap                          
        pos_tubo2_su_iniz = random.randint(-430, -100)             
        pos_tubo2_giu_iniz = pos_tubo2_su_iniz + tubo_su.get_height() + vert_gap
        win.blit(tubo_su, (vel_tubo2, pos_tubo2_su_iniz))         
        win.blit(tubo_giu, (vel_tubo2, pos_tubo2_giu_iniz))
    else:                                                         
        win.blit(tubo_su, (vel_tubo2, pos_tubo2_su_iniz))         
        win.blit(tubo_giu, (vel_tubo2, pos_tubo2_giu_iniz))

    ### Incremento le velocità ###
    vel_tubo_iniz -= 6                                
    vel_tubo1 -= 6 
    vel_tubo2 -= 6
    
    ### Mostro a schermo il terreno ###
    win.blit(terreno, (vel_Terreno, 630))
    
    ### Mostro a schermo l'uccello ###
    if jumpcount >= 6 and  const >= 12  :            # Se sta scendendo (da un po')
        win.blit(uccello_giu, (x, y))                # Mostro uccello_giu
    else:                                     
        win.blit(uccello_su, (x, y))                 # Mostro uccello_su
        
    ### Velocità terreno ###
    vel_Terreno -= 6
    if vel_Terreno <= -94:
        vel_Terreno = 0
   
    # GESTIONE DEI TASTI #
    keys = pygame.key.get_pressed()

    ### Movimenti uccello ###
    if not(isJump):                                 # Se NON ho premuto la barra spaziatrice
        y += (const ** 2) * 0.07                   # Incremento la y di const^2
        const += 0.4                               # Incremento const
        if y >= WINDOW_HEIGHT - 130:                # Se l'uccello tocca il terreno --> BREAK
            break
        if (keys[pygame.K_SPACE]):                  # Se premo la barra spaziatrice --> isJump == True
            isJump = True
    else:                                           # Se HO premuto la barra spaziatrice
        if  jumpcount > 0 and y > 0:                # E se il salto non è ancora terminato, e non sono in cima allo schermo
            y -= (jumpcount ** 2) * 0.6             # Decremento la y di jumpcount^2
            jumpcount -=  1.3                        # Incremento joumpcount 
        else:
            isJump = False                          # Termino il salto 
            jumpcount = 7                           # Reinizializzo le variabili
            const = 7
    
    ### Mostro a schermo la scritta del punteggio ###
    scritta_punteggio = font.render(str(punteggio), True, (40, 40, 40))
    win.blit(scritta_punteggio, ((WINDOW_WIDTH/2) -20, 40))

    ### Aggiorno il display ###
    pygame.display.flip()
    clock.tick(50)

pygame.quit()  