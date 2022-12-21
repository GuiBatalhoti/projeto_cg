import pygame
from flood_fill import vizinhanca_8


# classe da interface de desenho
class InterfaceDesenho:
    def __init__(self) -> None:
        # iniciando a janela
        self.janela = pygame.display.set_mode((200,200)) #tamanho da Janela
        pygame.display.set_caption("Flood Fill - Vizinhança 4") #título da janela

        #abrindo a imagem 
        imagem = pygame.image.load("flood_fill\Testar_FloodFill.jpg").convert()       

        # loop infinito para verificar de alguém estpa tentando desenhar
        while True:
            # loop pela lista de eventos
            for event in pygame.event.get():
                # se o evento foi de saída, fechar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                # se o evento foi de clique do mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #preenchendo a vizinhança 4
                        vizinhanca_8(imagem, event.pos)

            #definindo a imagem como fundo e atualizando a janela
            self.janela.blit(imagem, (0, 0))
            pygame.display.update()


janela = InterfaceDesenho()