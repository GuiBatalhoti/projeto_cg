import pygame
from pygame import gfxdraw
import time
import numpy as np
from math import cos, sin, sqrt, pow


def draw_circle(window, color, posStart, posNow):
    cx, cy = posStart
    x, y = posNow
    radius = sqrt(pow((x - cx), 2) + pow((y - cy), 2))

    x = 0
    y = int(radius)
    p = 3 - 2*radius
    draw_symmetric(window, color, x, y, cx, cy)

    while x < y:
        if p < 0:
            p += 4 * x + 6
        else:
            p += 4 * (x - y) + 10
            y = y - 1
        x = x + 1
        draw_symmetric(window, color, x, y, cx, cy)

def draw_symmetric(window, color, x, y, cx, cy):
    pygame.draw.line(window, color, ((cx + x), (cy + y)), ((cx + x)+1, (cy + y)+1))
    pygame.draw.line(window, color, ((cx + x), (cy - y)), ((cx + x)+1, (cy - y)+1))
    pygame.draw.line(window, color, ((cx - x), (cy + y)), ((cx - x)+1, (cy + y)+1))
    pygame.draw.line(window, color, ((cx - x), (cy - y)), ((cx - x)+1, (cy - y)+1))
    pygame.draw.line(window, color, ((cx + y), (cy + x)), ((cx + y)+1, (cy + x)+1))
    pygame.draw.line(window, color, ((cx + y), (cy - x)), ((cx + y)+1, (cy - x)+1))
    pygame.draw.line(window, color, ((cx - y), (cy + x)), ((cx - y)+1, (cy + x)+1))
    pygame.draw.line(window, color, ((cx - y), (cy - x)), ((cx - y)+1, (cy - x)+1))



window = pygame.display.set_mode((1200, 600))
points = []
begin = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    window.fill((255, 255, 255))

    if any(pygame.mouse.get_pressed()) and not begin:
        posStart = pygame.mouse.get_pos()
        begin = True

    if begin:
        posNow = pygame.mouse.get_pos()
        draw_circle(window, (255,0,0), posStart, posNow)

    if not any(pygame.mouse.get_pressed()) and begin:
        points.append((posStart, posNow))
        begin = False

    for i in range(len(points)):
        draw_circle(window, (0,0,0), points[i][0], points[i][1])                                                                              

    pygame.display.flip()