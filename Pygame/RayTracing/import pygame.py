import pygame
import sys
import random
from pygame.math import Vector2
from math import sin, cos, radians

class Main:
    def __init__(self):
        self.screen_walls = []
        self.walls = []
        self.rays = []

        # Rileva dimensioni iniziali della finestra
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = pygame.display.get_surface().get_size()

        # Eventuali muri random (attualmente 0)
        for _ in range(0):
            a = (random.randint(0, self.WINDOW_WIDTH), random.randint(0, self.WINDOW_HEIGHT))
            b = (random.randint(0, self.WINDOW_WIDTH), random.randint(0, self.WINDOW_HEIGHT))
            self.walls.append(Wall(a, b))

        # Crea i raggi in tutte le direzioni
        for i in range(0, 360, 5):
            angle = radians(i)
            direction = Vector2(cos(angle), sin(angle))
            ray = Ray(direction)
            self.rays.append(ray)

    def update(self):
        # Ottieni dimensioni aggiornate della finestra
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = pygame.display.get_surface().get_size()

        # Ricrea i bordi dello schermo
        self.screen_walls = [
            Wall((0, 0), (self.WINDOW_WIDTH, 0)),  # top
            Wall((0, self.WINDOW_HEIGHT), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)),  # bottom
            Wall((0, 0), (0, self.WINDOW_HEIGHT)),  # left
            Wall((self.WINDOW_WIDTH, 0), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))  # right
        ]

        total_walls = self.walls + self.screen_walls

        # Disegna i muri
        for wall in total_walls:
            wall.draw()

        # Calcola raggi
        for ray in self.rays:
            ray.update_pos()
            closest_point = None
            min_distance = float('inf')

            for wall in total_walls:
                hit, point = ray.check(wall)
                if hit:
                    dist = Vector2(point).distance_to(ray.pos)
                    if dist < min_distance:
                        min_distance = dist
                        closest_point = point

            if closest_point:
                pygame.draw.line(win, (255, 255, 100), ray.pos, closest_point, 2)


class Wall:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        pygame.draw.line(win, (255, 255, 255), self.a, self.b, 3)


class Ray:
    def __init__(self, direction):
        self.dir = direction
        self.pos = Vector2(0, 0)

    def update_pos(self):
        self.pos = Vector2(pygame.mouse.get_pos())

    def check(self, wall):
        x1, y1 = wall.a
        x2, y2 = wall.b
        x3, y3 = self.pos
        x4 = self.pos.x + self.dir.x * 10000
        y4 = self.pos.y + self.dir.y * 10000

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return False, None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 <= t <= 1 and u >= 0:
            px = x1 + t * (x2 - x1)
            py = y1 + t * (y2 - y1)
            return True, (px, py)

        return False, None


# === Inizializzazione ===

pygame.init()
win = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
pygame.display.set_caption("Raycasting Demo")
clock = pygame.time.Clock()

main = Main()

# === Loop principale ===

running = True
while running:
    win.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
