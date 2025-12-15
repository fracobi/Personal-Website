import pygame 

board = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

icona = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Filetto\Images\icona.png')
icona = pygame.transform.scale(icona, (80, 80))

window_height = 680
window_width = 680
colore_sfondo = (40, 40, 40)
altezza_casella = 200
larghezza_casella = 200 
colore_casella = (255, 255, 255)

casella = pygame.Surface((200, 200))
casella_rect1 = casella.get_rect(topleft = (20, 20))
casella_rect2 = casella.get_rect(topleft = (240, 20))
casella_rect3 = casella.get_rect(topleft = (460, 20))
casella_rect4 = casella.get_rect(topleft = (20, 240))
casella_rect5 = casella.get_rect(topleft = (240, 240))
casella_rect6 = casella.get_rect(topleft = (460, 240))
casella_rect7 = casella.get_rect(topleft = (20, 460))
casella_rect8 = casella.get_rect(topleft = (240, 460))
casella_rect9 = casella.get_rect(topleft = (460, 460))

active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
active6 = False
active7 = False
active8 = False
active9 = False

conto = 1
conto1 = 0 
conto2 = 0
conto3 = 0
conto4 = 0
conto5 = 0
conto6 = 0
conto7 = 0
conto8 = 0
conto9 = 0

pygame.init()
win = pygame.display.set_mode ((window_width, window_height))
pygame.display.set_caption('Filetto')
pygame.display.set_icon(icona)
win.fill(colore_sfondo)

################################################################################

def main():   
    global active1 
    global active2 
    global active3 
    global active4 
    global active5 
    global active6 
    global active7 
    global active8 
    global active9 
    global conto1
    global conto2
    global conto3
    global conto4
    global conto5
    global conto6
    global conto7
    global conto8
    global conto9
    global conto 

    done = False
    while not done: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if casella_rect1.collidepoint(event.pos) and active1 == False :                 
                    active1 = True
                    conto1 = conto 
                    conto += 1
                elif casella_rect2.collidepoint(event.pos) and active2 == False:
                    active2 = True
                    conto2 = conto 
                    conto += 1
                elif casella_rect3.collidepoint(event.pos) and active3 == False:
                    active3 = True
                    conto3 = conto  
                    conto += 1                 
                elif casella_rect4.collidepoint(event.pos) and active4 == False :
                    active4 = True 
                    conto4 = conto  
                    conto += 1                                         
                elif casella_rect5.collidepoint(event.pos) and active5 == False :
                    active5 = True
                    conto5 = conto  
                    conto += 1                                      
                elif casella_rect6.collidepoint(event.pos) and active6 == False :
                    active6 = True
                    conto6 = conto  
                    conto += 1                                          
                elif casella_rect7.collidepoint(event.pos) and active7 == False :
                    active7 = True
                    conto7 = conto  
                    conto += 1                                          
                elif casella_rect8.collidepoint(event.pos) and active8 == False :
                    active8 = True
                    conto8 = conto  
                    conto += 1                                          
                elif casella_rect9.collidepoint(event.pos) and active9 == False :
                    active9 = True
                    conto9 = conto  
                    conto += 1                      

        disegna_tabella()  
        posiziona_mossa(active1, active2, active3, active4, active5, active6, active7, active8, active9)
        pygame.display.flip()
        if controllo_vincitore(board):
            break

################################################################################

def disegna_tabella():
    casella.fill(colore_casella)

    win.blit(casella, (20, 20))
    win.blit(casella, (20, 240))
    win.blit(casella, (20, 460))

    win.blit(casella, (240, 20))
    win.blit(casella, (240, 240))
    win.blit(casella, (240, 460))

    win.blit(casella, (460, 20))
    win.blit(casella, (460, 240))
    win.blit(casella, (460, 460))

################################################################################

def posiziona_mossa(active1, active2, active3, active4, active5, active6, active7, active8, active9 ):
    global board
    
    if active1 == True:
        if conto1 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (120, 120), 80, 10)
            del board[0][0]
            board[0].insert(0, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (40, 40), (200, 200), 20)
            pygame.draw.line(win, (0, 0, 180), (40, 200), (200, 40), 20) 
            del board[0][0]
            board[0].insert(0, 'X')
    if active2 == True:
        if conto2 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (340, 120), 80, 10)
            del board[0][1]
            board[0].insert(1, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (260, 40), (420, 200), 20)
            pygame.draw.line(win, (0, 0, 180), (260, 200), (420, 40), 20)
            del board[0][1]
            board[0].insert(1, 'X')
    if active3 == True:
        if conto3 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (560, 120), 80, 10)
            del board[0][2]
            board[0].insert(2, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (480, 40), (640, 200), 20)
            pygame.draw.line(win, (0, 0, 180), (480, 200), (640, 40), 20)
            del board[0][2]
            board[0].insert(2, 'X')
    if active4:
        if conto4 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (120, 340), 80, 10)
            del board[1][0]
            board[1].insert(0, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (40, 260), (200, 420), 20)
            pygame.draw.line(win, (0, 0, 180), (40, 420), (200, 260), 20)
            del board[1][0]
            board[1].insert(0, 'X')
    if active5:
        if conto5 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (340, 340), 80, 10)
            del board[1][1]
            board[1].insert(1, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (260, 260), (420, 420), 20)
            pygame.draw.line(win, (0, 0, 180), (260, 420), (420, 260), 20)
            del board[1][1]
            board[1].insert(1, 'X')
    if active6:
        if conto6 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (560, 340), 80, 10)
            del board[1][2]
            board[1].insert(2, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (480, 260), (640, 420), 20)
            pygame.draw.line(win, (0, 0, 180), (480, 420), (640, 260), 20)
            del board[1][2]
            board[1].insert(2, 'X')
    if active7:
        if conto7 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (120, 560), 80, 10)
            del board[2][0]
            board[2].insert(0, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (40, 480), (200, 640), 20)
            pygame.draw.line(win, (0, 0, 180), (40, 640), (200, 480), 20)
            del board[2][0]
            board[2].insert(0, 'X')
    if active8:
        if conto8 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (340, 560), 80, 10)
            del board[2][1]
            board[2].insert(1, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (260, 480), (420, 640), 20)
            pygame.draw.line(win, (0, 0, 180), (260, 640), (420, 480), 20)
            del board[2][1]
            board[2].insert(1, 'X')
    if active9:
        if conto9 % 2 == 0:
            pygame.draw.circle(win, (255,0,0), (560, 560), 80, 10)
            del board[2][2]
            board[2].insert(2, 'O')
        else:
            pygame.draw.line(win, (0, 0, 180), (480, 480), (640, 640), 20)
            pygame.draw.line(win, (0, 0, 180), (480, 640), (640, 480), 20)
            del board[2][2]
            board[2].insert(2, 'X')

################################################################################

def controllo_vincitore(board):

    ## controllo righe##
        if board [0] == ['X', 'X', 'X'] or board [1] == ['X', 'X', 'X'] or board [2] == ['X', 'X', 'X']:
            return ('giocatore X vince!')
        elif board [0] == ['O', 'O', 'O'] or board [1] == ['O', 'O', 'O'] or board [2] == ['O', 'O', 'O']:
            return ('giocatore O vince!')

        ## controllo colonne##
        if board [0][0] == 'X' and board [1][0] == 'X' and board [2][0] == 'X':
            return ('giocatore X vince!')
        elif board [0][1] == 'X' and board [1][1] == 'X' and board [2][1] == 'X':
            return('giocatore X vince! ')
        elif board [0][2] == 'X' and board [1][2] == 'X' and board [2][2] == 'X':
            return ('giocatore X vince!')

        if board [0][0] == 'O' and board [1][0] == 'O' and board [2][0] == 'O':
            return ('giocatore O vince!')
        elif board [0][1] == 'O' and board [1][1] == 'O' and board [2][1] == 'O':
            return('giocatore O vince!' )
        elif board [0][2] == 'O' and board [1][2] == 'O' and board [2][2] == 'O':
            return ('giocatore O vince!')
        
        ## controllo diagonali##
        if board [0][0] == board [1][1] == board [2][2] == 'X':
            return ('giocatore X vince!')
        if board [0][0] == board [1][1] == board [2][2] == 'O':
            return ('giocatore O vince!')

        if board [0][2] == board [1][1] == board [2][0] == 'X':
            return ('giocatore X vince!')
        if board [0][2] == board [1][1] == board [2][0] == 'O':
            return ('giocatore O vince!')   

################################################################################

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()