import pygame 


WINDOW_WHIDTH = 800
WINDOW_HEIGHT = 800


pygame.init()
win = pygame.display.set_mode((WINDOW_WHIDTH, WINDOW_HEIGHT ))
clock = pygame.time.Clock()

run = False
while not run:
    win.fill((30, 30, 30))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True
            pygame.quit()
            sys.exit()


    print(pygame.mouse.get_pos())
    
    pygame.display.flip()