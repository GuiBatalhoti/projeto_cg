import pygame

# Método alternativo para o desenho de linhas com Bresenham, mas o outro está melhor

# def line_bresenham(window, lineColor, x1,y1,x2,y2):
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)
#     D = 2*dy - dx
#     y = y1
#     for x in range(x1+1, x2+1):
#         if D > 0:
#             y += 1
#             pygame.draw.line(window, lineColor, (x1, y1), (x2, y2))
#             D += (2*dy-2*dx)
#         else:
#             pygame.draw.line(window, lineColor, (x1, y1), (x2, y2))
#             D += 2*dy
#     pygame.display.flip()
 

def bresenham(window, lineColor, x0, y0, x1, y1):
    #Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    #Input coordinates should be integers.
    #The result will contain both the start and the end point.
    
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