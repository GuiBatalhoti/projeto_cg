from utils import *
import pygame

def avaliarCodigo(x, y): 
    codigo = DENTRO 
    if x < X_MIN:      # a esquerda do retangulo 
        codigo |= ESQUERDA 
    elif x > X_MAX:    # a direita do retangulo 
        codigo |= DIREITA 
    if y < Y_MIN:      # abaixo do retangulo 
        codigo |= BAIXO 
    elif y > Y_MAX:    # acima do retangulo 
        codigo |= TOP 
    return codigo 

# cortando uma linha de P1 = (x1, y1) para P2 = (x2, y2) 
def cohenSutherland(janela, cor, posInicial, posFinal): 
    x1,y1 = posInicial
    x2,y2 = posFinal
    listaPontos = []
    # avaliar o codigo das regioes p1 e p2
    codigo1 = avaliarCodigo(x1, y1) 
    codigo2 = avaliarCodigo(x2, y2) 
    aceitar = False
    while True: 
        # se ambas as extremidades estiverem dentro do retangulo
        if codigo1 == 0 and codigo2 == 0: 
            aceitar = True
            break
        # se ambas as extremidades estiverem fora do triangulo 
        elif (codigo1 & codigo2) != 0: 
            break
        # Algum segmento está dentro do retângulo 
        else: 
            # a linha precisa ser cortada 
            # ao menos um dos pontos esta fora,  
            x = 1.0
            y = 1.0
            if codigo1 != 0: 
                codigoFora = codigo1 
            else: 
                codigoFora = codigo2 
            # achar o ponto de interseccao usando a formula y = y1 + declinio * (x - x1),  
            # x = x1 + (1 / declinio) * (y - y1) 
            if codigoFora & TOP: 
                # o ponto está acima do corte 
                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1) 
                y = Y_MAX 
            elif codigoFora & BAIXO: 
                # ponto esta abaixo do corte 
                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1) 
                y = Y_MIN 
            elif codigoFora & DIREITA: 
                # ponto esta a direita do corte 
                y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1) 
                x = X_MAX 
            elif codigoFora & ESQUERDA: 
                # ponto esta a esquerda do corte 
                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1) 
                x = X_MIN 
            # a interseccao foi achada 
            # Substituímos o ponto fora do retângulo de recorte pelo ponto de interseccao
            if codigoFora == codigo1: 
                x1 = x 
                y1 = y 
                codigo1 = avaliarCodigo(x1,y1)
             
            if codigoFora == codigo2: 
                x2 = x 
                y2 = y 
                codigo2 = avaliarCodigo(x2, y2) 
            #listaPontos.append(aceitar)
            #pygame.draw.line(janela, cor, (x1,y1), (x2,y2))
            #return aceitar
    #listaPontos.append(aceitar)
    pygame.draw.line(janela, cor, (x1,y1), (x2,y2))
    #return listaPontos

