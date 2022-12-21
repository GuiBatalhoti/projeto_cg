from cohen_sutherland import cohen_sutherland
from utils import *
import pygame


# classe da interface de desenho
class InterfaceDesenho:
    def __init__(self) -> None:
        # iniciando a janela
        self.janela = pygame.display.set_mode(TAM_JANELA) #tamanho da Janela
        pygame.display.set_caption("Cohen-Sutherland")


        # lista de pontos para desenhar, inclui os pontos já desenhados
        # e inclui os pontos que estão sendo desenhados
        pontos = []
        posicao_inicial = None

        # variável para indicar se deve fazer a linha em tempo real ou não
        desenhando = False

        # loop infinito para verificar de alguém estpa tentando desenhar
        while True:
            # loop pela lista de eventos
            for event in pygame.event.get():
                # se o evento foi de saída, fechar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(1)
            
            #preenchendo a janela apenas com braco no fundo
            self.janela.fill(BRANCO)

            #pegando a posição atual quando o mouse é pressionado
            if any(pygame.mouse.get_pressed()) and not desenhando:
                #retorno da posição de quando foi pressionado
                posicao_inicial = pygame.mouse.get_pos() 
                # agora pode desenhar
                desenhando = True

<<<<<<< HEAD:Cohen-Sutherland/interface_desenho.py
            ## desenhando a retangulo
            pygame.draw.line(self.janela, (0,0,0), (X_MIN, Y_MIN), (X_MAX, Y_MIN), width= 5)
            pygame.draw.line(self.janela, (0,0,0), (X_MAX, Y_MIN), (X_MAX, Y_MAX), width = 5)
            pygame.draw.line(self.janela, (0,0,0), (X_MAX, Y_MAX), (X_MIN, Y_MAX), width = 5)
            pygame.draw.line(self.janela, (0,0,0), (X_MIN, Y_MAX), (X_MIN, Y_MIN), width = 5)
=======
            ## desenhando o retângulo de limites
            pygame.draw.line(self.janela, (0,0,0), (X_MIN, Y_MIN), (X_MAX, Y_MIN), width = 3)
            pygame.draw.line(self.janela, (0,0,0), (X_MAX, Y_MIN), (X_MAX, Y_MAX), width = 3)
            pygame.draw.line(self.janela, (0,0,0), (X_MAX, Y_MAX), (X_MIN, Y_MAX), width = 3)
            pygame.draw.line(self.janela, (0,0,0), (X_MIN, Y_MAX), (X_MIN, Y_MIN), width = 3)
>>>>>>> e866ed176371824f8964d5b2715678629b435bc6:cohen_sutherland/interface_desenho.py

            if desenhando is True:
                posicao_atual = pygame.mouse.get_pos(self.janela, ) 
                pygame.draw.line(self.janela, CORQUALQUER, posicao_inicial, posicao_atual )
            
            if not any(pygame.mouse.get_pressed()) and desenhando:
                posicao_atual = pygame.mouse.get_pos()
                pontos.append((posicao_inicial, posicao_atual))
                desenhando = False

            for i in range(len(pontos)):
                cohen_sutherland(self.janela, PRETO, pontos[i][0], pontos[i][1])
            
            pygame.display.flip()


janela = InterfaceDesenho()