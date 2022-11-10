from bresenham import bresenham
import pygame


# classe da interface de desenho
class InterfaceDesenho:
    def __init__(self) -> None:
        # iniciando a janela
        self.janela = pygame.display.set_mode((640, 480)) #tamanho da Janela
        pygame.display.set_caption("Linhas Bresenham")


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
            self.janela.fill((255, 255, 255))

            #pegando a posição atual quando o mouse é pressionado
            if any(pygame.mouse.get_pressed()) and not desenhando:
                #retorno da posição de quando foi pressionado
                posicao_inicial = pygame.mouse.get_pos() 
                # agora pode desenhar
                desenhando = True

            if desenhando is True:
                posicao_atual = pygame.mouse.get_pos()
                bresenham(self.janela, (255,0,0), posicao_inicial[0], posicao_inicial[1], posicao_atual[0], posicao_atual[1])                                                                                 

            if not any(pygame.mouse.get_pressed()) and desenhando:
                posicao_atual = pygame.mouse.get_pos()
                pontos.append((posicao_inicial, posicao_atual))
                desenhando = False

            for i in range(len(pontos)):
                bresenham(self.janela, (0, 0, 0), pontos[i][0][0], pontos[i][0][1], pontos[i][1][0], pontos[i][1][1])                                                                              

            pygame.display.flip()


janela = InterfaceDesenho()