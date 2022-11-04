# biblioteca para desenhar os pixels
from pygame import gfxdraw
 

def bresenham(janela, cor_linha, x0, y0, x1, y1):
    # deltas
    delta_x = x1 - x0
    delta_y = y1 - y0

    #verificando o sinal de X e de Y
    sinal_x = 1 if delta_x > 0 else -1
    sinal_y = 1 if delta_y > 0 else -1

    # pegando o valor absoluto dos deltas
    delta_x = abs(delta_x)
    delta_y = abs(delta_y)

    # verificando qual delta é maior
    if delta_x > delta_y:
        multiplicador_x, multiplicador_x_para_y, multiplicador_y_para_x, multiplicador_y = sinal_x, 0, 0, sinal_y
    else:
        delta_x, delta_y = delta_y, delta_x
        multiplicador_x, multiplicador_x_para_y, multiplicador_y_para_x, multiplicador_y = 0, sinal_y, sinal_x, 0

    D = 2*delta_y - delta_x
    y = 0

    for x in range(delta_x + 1):
        pinta_pixel(janela, cor_linha, (x0 + x*multiplicador_x + y*multiplicador_y_para_x, y0 + x*multiplicador_x_para_y + y*multiplicador_y))
        if D >= 0:
            y += 1
            D -= 2*delta_x
        D += 2*delta_y
    

def pinta_pixel(janela, cor: tuple, pixel: tuple):
    gfxdraw.pixel(janela, pixel[0], pixel[1], cor)