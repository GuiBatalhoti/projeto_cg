import pygame
import time
import numpy as np

def line_bresenham(window, lineColor, x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    D = 2*dy - dx
    y = y1
    for x in range(x1+1, x2+1):
        if D > 0:
            y += 1
            pygame.draw.line(window, lineColor, (x1, y1), (x2, y2))
            D += (2*dy-2*dx)
        else:
            pygame.draw.line(window, lineColor, (x1, y1), (x2, y2))
            D += 2*dy
    pygame.display.flip()
 

def bresenham(window, lineColor, x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        pygame.draw.line(window, lineColor, (x0, y0), (x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        #print(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
        #yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy





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
        #pygame.draw.line(window, (255, 0, 0), (posStart[0], posStart[1]), (posNow[0], posNow[1]))
        bresenham(window, (255,0,0), posStart[0], posStart[1], posNow[0], posNow[1])
        #print(pixel, end = '\n\n\n')
        #line_bresenham(window, (255, 0, 0), posStart[0], posStart[1], posNow[0], posNow[1])                                                                                  

    if not any(pygame.mouse.get_pressed()) and begin:
        points.append((posStart, posNow))
        begin = False

    for i in range(len(points)):
        #pygame.draw.line(window, (0, 0, 0), (points[i][0][0], points[i][0][1]), (points[i][1][0], points[i][1][1]))
        #line_bresenham(window, (0, 0, 0), posStart[0], posStart[1], posNow[0], posNow[1])
        bresenham(window, (0, 0, 0), points[i][0][0], points[i][0][1], points[i][1][0], points[i][1][1])                                                                              

    pygame.display.flip()