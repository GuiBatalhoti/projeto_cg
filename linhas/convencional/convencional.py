from pygame import gfxdraw

def convencional(janela, cor_linha: tuple, posicao_inicial: tuple, posicao_atual: tuple):
    x0, y0 = posicao_inicial
    x1, y1 = posicao_atual

    if posicao_inicial == posicao_atual:
        return

    delta_x = x1 - x0
    delta_y = y1 - y0

    if abs(delta_x) > abs(delta_y):
        m = delta_y / delta_x
        x_0 = x0
        x_1 = x1
        incremento = 1 if x_1 > x_0 else -1

        while x_0 != x_1:
            pinta_pixel(janela, cor_linha, (x_0, y0 + round((x_0 - x0) * m)))
            x_0 += incremento

    else:
        m = delta_x / delta_y
        y_0 = y0
        y_1 = y1
        incremento = 1 if y_1 > y_0 else -1

        while y_0 != y_1:
            pinta_pixel(janela, cor_linha, (x0 + round((y_0 - y0) * m), y_0))
            y_0 += incremento



def pinta_pixel(janela, cor_linha: tuple, pixel: tuple):
    gfxdraw.pixel(janela, pixel[0], pixel[1], cor_linha)