import random, pygame, sys
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        self.randomize()
        
    def draw_fruit(self):
        win.blit(fruit, (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE))
        # fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # pygame.draw.rect(win, (0, 0, 255), fruit_rect)    
        
    def randomize (self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)     
        self.pos = Vector2(self.x, self.y)        


class Snake:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]    
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            if block == self.body[0]:
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
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
    
    def add_block(self):
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0])
            self.body = body_copy[:]
            
            
class main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        
    def update (self):
        self.snake.move_snake()
        self.ceck_collision()
    
    def draw_elements (self):
        self.draw_grid()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        # print(self.snake.body[0].x)
        
    def ceck_collision (self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        else:   
            for _ in self.snake.body:
                if self.snake.body[0] in self.snake.body[1:]:
                    print ('loose')
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= CELL_NUMBER:
            print('loose')
        if self.snake.body[0].y < 0 or self.snake.body[0].y >= CELL_NUMBER:
            print('Loose')
            
    def draw_grid(self):
        casella = pygame.Surface((CELL_SIZE, CELL_SIZE))
        casella.fill((150, 150, 150))
        x = 0
        y = 0
        for caselle in range(WINDOW_WIDTH):
            if caselle % 20 == 0:
                win.blit(casella, (x, y))
                x += 40
                #y += 20
        
        # for caselle in range(WINDOW_WIDTH):
        #     if caselle % 20 == 0:
        #     win.blit(casella, (x, y))
        #     x += 40
                
            
                
CELL_SIZE = 20 
CELL_NUMBER= 30 

WINDOW_WIDTH  = (CELL_SIZE * CELL_NUMBER)
WINDOW_HEIGHT = (CELL_SIZE * CELL_NUMBER)
COLOR_WIN = (20, 20, 20)
 
fruit = pygame.image.load(r'C:\Users\User\AppData\Roaming\Python\Python39\Codici\Pygame\Snake.py\images\fruit.png')
head_su = pygame.image.load(r'C:\Users\User\AppData\Roaming\Python\Python39\Codici\Pygame\Snake.py\images\snake_head.png')

fruit = pygame.transform.scale(fruit, (CELL_SIZE, CELL_SIZE))
head_giu = pygame.transform.rotate(head_su, 180 )
head_dx = pygame.transform.rotate(head_su, -90)
head_sx = pygame.transform.rotate(head_su, 90)
### Open the PyGame Wdinow
pygame.init()
win = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 140)

main_game = main()

### Main Loop
run = False
while not run:
    # Handle Window Events, etc.
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True    
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_w:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_a:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_s:
                main_game.snake.direction = Vector2(0, 1)
            
    win.fill( COLOR_WIN )
    main_game.draw_elements()
    pygame.display.flip()
    
pygame.quit()