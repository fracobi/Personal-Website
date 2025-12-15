import pygame 

board = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
size = 3
X = 'X'
O = 'O'

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
WIN_GIOCO_HEIGHT = 600
WIN_GIOCO_WIDTH = 600
COLORE_SFONDO = (255, 255, 255)

### Variabili input_box ###
input_box_1 = pygame.Rect(30 ,WINDOW_HEIGHT-50, 140, 32)
input_box_2 = pygame.Rect(WINDOW_WIDTH -230 ,WINDOW_HEIGHT-50, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_1 = color_inactive
color_2 = color_inactive
active_1 = False
active_2 = False
text_1 = ''
text_2 = ''

linea_vert = pygame.image.load(r'C:\Users\User\AppData\Roaming\Python\Python39\Codici\Pygame\Filetto\Images\linea_vert.png')
linea_oriz = pygame.image.load(r'C:\Users\User\AppData\Roaming\Python\Python39\Codici\Pygame\Filetto\Images\linea_oriz.png')

pygame.init()
win = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))
win_gioco = pygame.Surface((WIN_GIOCO_WIDTH, WIN_GIOCO_HEIGHT))
pygame.display.set_caption('Filetto')
font = pygame.font.Font(None, 32)

run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box_1.collidepoint(event.pos):
                # Toggle the active variable.
                active_1 = not active_1
            if input_box_2.collidepoint(event.pos):
                # Toggle the active variable.
                active_2 = not active_2    
            else:
                active_1 = False
                active_2 = False
            # Change the current color of the input box.
            color_1 = color_active if active_1 else color_inactive
            color_2 = color_active if active_2 else color_inactive
        if event.type == pygame.KEYDOWN:
            if active_1:
                if event.key == pygame.K_RETURN:
                        print(text_1)
                        text_1 = ''
                elif event.key == pygame.K_BACKSPACE:
                        text_1 = text_1[:-1]
                else:
                        text_1 += event.unicode
            if active_2:
                if event.key == pygame.K_RETURN:
                        print(text_2)
                        text_2 = ''
                elif event.key == pygame.K_BACKSPACE:
                        text_2 = text_2[:-1]
                else:
                        text_2 += event.unicode

    win.fill(COLORE_SFONDO)
    win_gioco.fill((255,255,0))

    ### Disegno la superfice del gioco ###
    win.blit(win_gioco, (100, 100))
    
    ### Disegno la tabella ###    
    win.blit(linea_vert, (1/3 * WINDOW_WIDTH +35, 100))              
    win.blit(linea_vert, (2/3 * WINDOW_WIDTH -35, 100))
    win.blit(linea_oriz, (100, 1/3 * WINDOW_HEIGHT +35))             
    win.blit(linea_oriz, (100, 2/3 * WINDOW_HEIGHT -35))

    # Render the current text.
    txt_surface_box1 = font.render(text_1, True, color_1)
    txt_surface_box2 = font.render(text_2, True, color_2)
    # Resize the box if the text is too long.
    width = max(200, txt_surface_box1.get_width()+10)
    input_box_1.w = width
    input_box_2.w = width
    # Blit the text.
    win.blit(txt_surface_box1, (input_box_1.x+5, input_box_1.y+5))
    win.blit(txt_surface_box2, (input_box_2.x+5, input_box_2.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(win, color_1, input_box_1, 3)
    pygame.draw.rect(win, color_2, input_box_2, 3)
 
    # mossa = input(giocatore1.upper() + '-->' + 'Inserisci la mossa (riga, colonna): ')
        
    # #### genero la lista contenente le coordinate della mossa (mossa_list)---->da una stringa tipo (' a , b ') ottengo una lista [a, b]  ####
    # mossa_split = mossa.split(',')
    # mossa_list = []

    # for i in range(len(mossa_split)):
    #     element = int(mossa_split[i].strip()) - 1
    #     mossa_list.append(element)


    # #### rimuovo lo spazio, ed inserisco la mossa del giocatore nella tabella alle coordinate inserite ###
    # for j in range(len(mossa_list)-1):
    #     if board[mossa_list[j]][mossa_list[j+1]] != ' ':
    #         print ('casella gia occupata! \nRIPROVA')
    #         conto +=1
    #     else:
    #         del board[mossa_list[j]][mossa_list[j+1]]
    #         board[mossa_list[j]].insert(mossa_list[j+1], 'X') 



    pygame.display.flip()