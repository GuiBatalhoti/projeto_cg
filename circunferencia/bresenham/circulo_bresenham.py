import pygame
from math import sqrt, pow


def circulo_bresenham(window, color, posStart, posNow):
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