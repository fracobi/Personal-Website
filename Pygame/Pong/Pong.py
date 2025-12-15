import pygame
from pygame.math import Vector2
import ctypes
import random
import sys

pygame.font.init()

icon = pygame.image.load(r'C:\Users\Francesco\Documents\07-Codici\Pygame\Pong\Images\pong_icon.png')
icon = pygame.transform.scale(icon, (50, 50))

class Players:
    def __init__(self, x):
        self.width = 25
        self.height = 175
        self.x = x
        self.y = WINDOW_HEIGHT / 2 - (self.height / 2)

    def draw_player(self):
        self.player = pygame.Rect(self.x, self.y , self.width, self.height)
        pygame.draw.rect(win, (255, 255, 255), self.player)
        
    def move_player1(self):
        if keys[pygame.K_w]:  
            self.y -= VEL_PLAYER   
        if keys[pygame.K_s]:
            self.y += VEL_PLAYER     
              
    def move_player2(self):
        if keys[pygame.K_UP]:
            self.y -= VEL_PLAYER
        if keys[pygame.K_DOWN]:
            self.y += VEL_PLAYER        


class Ball:
    def __init__(self):
        self.radius = 13
        self.x = WINDOW_WIDTH / 2 
        self.y = WINDOW_HEIGHT / 2 
        self.ball = Vector2(self.x, self.y)
        self.vel_ball_x = 0 
        self.vel_ball_y = 0
        self.score1 = 0
        self.score2 = 0

    def draw_ball (self):
        self.ball_circle = pygame.draw.circle(win, (255, 255, 255), self.ball, self.radius )
      
    def move_ball (self):    
        self.ball[0] += self.vel_ball_x
        self.ball[1] += self.vel_ball_y
    
        if self.ball_circle.colliderect(main.player1.player):    
            self.vel_ball_x = VEL_BALL
        if self.ball_circle.colliderect(main.player2.player):    
            self.vel_ball_x = -VEL_BALL 
        if self.ball[1] <= self.radius:    
            self.vel_ball_y = VEL_BALL   
        if self.ball[1] >= WINDOW_HEIGHT - self.radius:    
            self.vel_ball_y = -VEL_BALL 
               
    def check_point(self):        
        if self.ball[0] >= WINDOW_WIDTH:    
            self.score1 += 1
        if self.ball[0] <= - self.radius:    
            self.score2 += 1


class main:
    def __init__(self):
        self.player1 = Players(25)
        self.player2 = Players(WINDOW_WIDTH - 50)
        self.ball = Ball()     
        self.font = pygame.font.SysFont(None, 150)   
        
    def update(self):
        self.player1.draw_player()
        self.player2.draw_player()
        self.ball.draw_ball()
        self.ball.move_ball()
        self.ball.check_point()
        self.draw_score()
        self.draw_line()
        
    def check_input(self):
        if keys[pygame.K_SPACE] and main.ball.vel_ball_x == 0 and main.ball.vel_ball_y == 0:
            self.start()
        
        if keys[pygame.K_w] and self.player1.y > 0:   
            self.player1.move_player1()
        if keys[pygame.K_s] and self.player1.y < WINDOW_HEIGHT - self.player1.height:
            self.player1.move_player1()
        if keys[pygame.K_UP] and self.player2.y > 0:    
            self.player2.move_player2()
        if keys[pygame.K_DOWN] and self.player2.y < WINDOW_HEIGHT - self.player2.height :
            self.player2.move_player2()
    
    def check_reset(self):  
        if self.ball.ball[0] <= -self.ball.radius or self.ball.ball[0] >= WINDOW_WIDTH:
            self.reset()
        if keys[pygame.K_n]:
            self.reset()
            
    def reset(self):
        main.ball.ball = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 )
        main.ball.vel_ball_x = 0
        main.ball.vel_ball_y = 0
    
    def start(self):
        main.ball.vel_ball_x = random.choice([+15, -15])
        main.ball.vel_ball_y = random.choice([+15, -15])
     
    def draw_score(self):
        self.score1_shown = self.font.render(str(self.ball.score1), True, (255, 255, 255))
        self.score2_shown = self.font.render(str(self.ball.score2), True, (255, 255, 255))
        self.score1_width = self.score1_shown.get_width()             
        win.blit(self.score1_shown, ( (WINDOW_WIDTH/2) - self.score1_width -100, 100))
        win.blit(self.score2_shown, ( (WINDOW_WIDTH/2) + 100, 100))   
    
    def draw_line (self):
        self.line = pygame.draw.line(win, (255, 255, 255), (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 1) 
        
FPS = 10   
VEL_BALL = 15
VEL_PLAYER = 10
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 750

myappid = 'Pong Game' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('PONG GAME')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

main = main()
 
run = False
while not run:
    win.fill((0,0,0))
    keys = pygame.key.get_pressed() 
    
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            run = True
            pygame.quit()
            sys.exit()
    
    main.check_input()
    main.check_reset()    
    main.update()
    
    pygame.display.flip()
    clock.tick(FPS)

