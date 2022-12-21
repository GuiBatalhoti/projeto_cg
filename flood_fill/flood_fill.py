import pygame

def vizinhanca_4(imagem, posicao_mouse):
    #flood fill utilizando a vizinhança 4

    cor = imagem.map_rgb((0, 0, 0))
    #pegando a imagem em array
    imagem_array = pygame.surfarray.pixels2d(imagem)
    #pegando a cor do pixel clicado
    cor_pixel = imagem_array[posicao_mouse]

    #criando uma lista de pixels a serem preenchidos
    pixels_a_preencher = [posicao_mouse]

    #loop para preencher os pixels
    while len(pixels_a_preencher) > 0:
        #pegando o pixel atual
        x,y = pixels_a_preencher.pop(0)
        try:  # Add a try-except block in case the position is outside the surface.
            if imagem_array[x, y] != cor_pixel:
                continue
        except IndexError:
            continue

        imagem_array[x,y] = cor
        #adicionando os pixels vizinhos a lista de pixels a serem preenchidos
        pixels_a_preencher.append((x + 1, y))
        pixels_a_preencher.append((x - 1, y))
        pixels_a_preencher.append((x, y + 1))
        pixels_a_preencher.append((x, y - 1))

    pygame.surfarray.blit_array(imagem, imagem_array)


def vizinhanca_8(imagem, posicao_mouse):
    #flood fill utilizando a vizinhança 4

    cor = imagem.map_rgb((0, 0, 0))
    #pegando a imagem em array
    imagem_array = pygame.surfarray.pixels2d(imagem)
    #pegando a cor do pixel clicado
    cor_pixel = imagem_array[posicao_mouse]

    #criando uma lista de pixels a serem preenchidos
    pixels_a_preencher = [posicao_mouse]

    #loop para preencher os pixels
    while len(pixels_a_preencher) > 0:
        #pegando o pixel atual
        x,y = pixels_a_preencher.pop(0)
        try:  # Add a try-except block in case the position is outside the surface.
            if imagem_array[x, y] != cor_pixel:
                continue
        except IndexError:
            continue

        imagem_array[x,y] = cor
        #adicionando os pixels vizinhos a lista de pixels a serem preenchidos
        pixels_a_preencher.append((x + 1, y))
        pixels_a_preencher.append((x - 1, y))
        pixels_a_preencher.append((x, y + 1))
        pixels_a_preencher.append((x, y - 1))
        pixels_a_preencher.append((x + 1, y + 1))
        pixels_a_preencher.append((x - 1, y - 1))
        pixels_a_preencher.append((x + 1, y - 1))
        pixels_a_preencher.append((x - 1, y + 1))
        

    pygame.surfarray.blit_array(imagem, imagem_array)