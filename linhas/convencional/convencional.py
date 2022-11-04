from pygame import gfxdraw

def convencional(janela, cor_linha: tuple, posicao_inicial: tuple, posicao_atual: tuple):
    
    # pegando as posições do mouse
    x0_inicial, y0_inicial = posicao_inicial
    x1_atual, y1_atual = posicao_atual

    # se ofrem iguais dá divisão por 0, o que não deve ocorrer
    if posicao_inicial == posicao_atual:
        return

    # Calculando os deltas
    delta_x = x1_atual - x0_inicial
    delta_y = y1_atual - y0_inicial

    # Verificando qual é maior par saber a direção da reta
    if abs(delta_x) > abs(delta_y):
        # Calculando o m
        m = delta_y / delta_x
        # Variáveis auxiliares
        x_0 = x0_inicial
        x_1 = x1_atual

        # Verificando o tipo de incremento
        incremento = 1 if x_1 > x_0 else -1

        # Incrementando o x e pintando os pixels
        while x_0 != x_1:
            pinta_pixel(janela, cor_linha, (x_0, y0_inicial + round((x_0 - x0_inicial) * m)))
            x_0 += incremento

    else:
        # Calculando o m
        m = delta_x / delta_y
        # Variáveis auxiliares
        y_0 = y0_inicial
        y_1 = y1_atual

        # Verificando o tipo de incremento
        incremento = 1 if y_1 > y_0 else -1

        # Incrementando o x e pintando os pixels
        while y_0 != y_1:
            pinta_pixel(janela, cor_linha, (x0_inicial + round((y_0 - y0_inicial) * m), y_0))
            y_0 += incremento



# Pinta os pixels na tela
def pinta_pixel(janela, cor_linha: tuple, pixel: tuple):
    gfxdraw.pixel(janela, pixel[0], pixel[1], cor_linha)