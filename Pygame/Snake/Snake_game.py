import random, pygame, sys
from pygame.math import Vector2
import ctypes


class Fruit:
    def __init__(self):
        self.randomize()
        
    def draw_fruit(self):
        win.blit(fruit, (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE))

    def randomize (self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)     
        self.pos = Vector2(self.x, self.y)   
               
             
class Snake:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]    
        self.direction = Vector2(0,0)
        self.new_block = False
        
              
    def draw_snake(self):
        for block in self.body:
            if block == self.body[0]:
                if  self.direction == (0, 0):
                    win.blit(head_dx, (block.x * CELL_SIZE, block.y * CELL_SIZE)) 
                if self.direction == (-1, 0):
                    win.blit(head_sx, (block.x * CELL_SIZE, block.y * CELL_SIZE))
                elif self.direction == (1, 0):
                    win.blit(head_dx, (block.x * CELL_SIZE, block.y * CELL_SIZE))
                elif self.direction == (0, 1):
                    win.blit(head_giu, (block.x * CELL_SIZE, block.y * CELL_SIZE))
                elif self.direction == (0, -1):
                    win.blit(head_su, (block.x * CELL_SIZE, block.y * CELL_SIZE))
            else:                  
                snake_block = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(win, (110, 255, 50), snake_block, 0)
                pygame.draw.rect(win, (0 , 0, 0), snake_block, 3)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:            
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
      
    def add_block(self):
        self.new_block = True
        
    def reset(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]    
        self.direction = Vector2(0,0)
        
    def check_fail (self):
        for block in self.body[1:]:
            if block == self.body[0]:
                self.reset()
                
        
class main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.conto = 0
      
    def update (self):
        self.snake.move_snake()
        self.check_collision()     
        
    def draw_elements (self):
        self.draw_grid()
        self.snake.draw_snake()
        self.snake.check_fail()
        self.fruit.draw_fruit()
        self.ceck_fruit_position()
        self.score()
          
    def check_collision (self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
              
        if  self.snake.body[0].x >= CELL_NUMBER:
            self.snake.body[0] = Vector2(-1 , self.snake.body[0].y ) + self.snake.direction 
        if self.snake.body[0].x < 0:  
            self.snake.body[0] = Vector2(CELL_NUMBER ,self.snake.body[0].y ) + self.snake.direction 
        if self.snake.body[0].y < 0:
            self.snake.body[0] = Vector2(self.snake.body[0].x , CELL_NUMBER) + self.snake.direction         
        if self.snake.body[0].y >= CELL_NUMBER:
            self.snake.body[0] = Vector2(self.snake.body[0].x , -1) + self.snake.direction        

    def draw_grid (self):
        i = 0 
        j = 0
        for i in range(CELL_NUMBER):
            for j in range(CELL_NUMBER):
                pygame.draw.line(win, (0, 0, 0),((i * CELL_SIZE)-1, 0), ((i*CELL_SIZE)-1, WINDOW_HEIGHT), 2)
                pygame.draw.line(win, (0, 0, 0),(0, (i * CELL_SIZE)-1), (WINDOW_HEIGHT, (i*CELL_SIZE)-1), 2)
       
    def ceck_fruit_position (self):
        if self.fruit.pos in self.snake.body:
            self.fruit.randomize()
            
    def score(self):
        self.punteggio = str(len(self.snake.body) - 3)
        self.font_score = pygame.font.SysFont(None, 40)       # Posso importare nuovi font da un file ttf su siti come 'Dafont.com'
        self.scritta_punteggio = self.font_score.render(self.punteggio, True, (255, 255, 255))
        win.blit(self.scritta_punteggio, (20, 20))
        win.blit(fruit_icon, (40, 19))

        self.hs_list = open('C:\Codici\Python\Pygame\Snake\HighScore.txt')
        self.hs_string = self.hs_list.readlines()[-1:]
        self.hs_int = int(self.hs_string[0])
        self.hs_list.close()

        self.scritta_high_score = self.font_score.render(str(self.hs_int), True, (255, 255, 255))
        win.blit(self.scritta_high_score, (WINDOW_WIDTH - 50, 20))
        win.blit(coppa_score , (WINDOW_WIDTH - 100, 20))
        
        if int(self.punteggio) > self.hs_int:
            self.high_score = self.hs_int
            
            self.hs_list = open('Pygame\Snake\Snake\HighScore.txt', 'a')
            self.hs_list.write('\n' + str(self.punteggio) + '\n')    
            self.hs_list.close()     

            
CELL_SIZE = 30 
CELL_NUMBER= 17

WINDOW_WIDTH  = (CELL_SIZE * CELL_NUMBER)
WINDOW_HEIGHT = (CELL_SIZE * CELL_NUMBER)
COLOR_WIN = (50, 50, 50)
 
fruit = pygame.image.load(r'C:\Codici\Python\Pygame\Snake\images\fruit.png')
head_su = pygame.image.load(r'C:\Codici\Python\Pygame\Snake\images\snake_head.png')
icona = pygame.image.load(r'C:\Codici\Python\Pygame\Snake\images\snake_icon.png')
coppa_score = pygame.image.load(r'C:\Codici\Python\Pygame\Snake\images\coppa.png')

fruit = pygame.transform.scale(fruit, (CELL_SIZE, CELL_SIZE))
fruit_icon = pygame.transform.scale(fruit, (CELL_SIZE - 7, CELL_SIZE - 7)) 
head_su = pygame.transform.scale(head_su, (CELL_SIZE, CELL_SIZE))
head_giu = pygame.transform.rotate(head_su, 180 )
head_dx = pygame.transform.rotate(head_su, -90)
head_sx = pygame.transform.rotate(head_su, 90)
coppa_score = pygame.transform.scale(coppa_score, (50,30))

myappid = 'Snake' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

### Open the PyGame Wdinow
pygame.init()
win = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("Snake")
pygame.display.set_icon(icona)
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 140)

main_game = main()

### Main Loop
run = False
while not run:
    win.fill( COLOR_WIN )
    main_game.draw_elements()
    
    # Handle Window Events, etc.
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if main_game.snake.direction != Vector2(-1, 0):
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if main_game.snake.direction != Vector2(0, 1):
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if main_game.snake.direction != Vector2(1, 0):
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if main_game.snake.direction != Vector2(0, -1):
                    main_game.snake.direction = Vector2(0, 1)
 

    pygame.display.flip()
    
pygame.quit()