from convencional import convencional
import pygame


# classe da interface de desenho
class InterfaceDesenho:
    def __init__(self) -> None:
        # iniciando a janela
        self.janela = pygame.display.set_mode((640, 480)) #tamanho da Janela
        pygame.display.set_caption("Linhas Convencionais")

        # lista de pontos para desenhar, inclui os pontos já desenhados
        # e inclui os pontos que estão sendo desenhados
        pontos = []

        posicao_inicial = None
        posicao_atual = None

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

            #pegando a posição inicial quando o mouse é pressionado
            if any(pygame.mouse.get_pressed()) and desenhando is False:
                #retorno da posição de quando foi pressionado
                posicao_inicial = pygame.mouse.get_pos() 
                # agora pode desenhar
                desenhando = True

            #desenhando o linha vermelha de posição
            if desenhando is True:
                posicao_atual = pygame.mouse.get_pos()
                convencional(self.janela, (0,0,255), posicao_inicial, posicao_atual)                                                                               

            #salvando os pixels de posição inicial e final da reta
            if not any(pygame.mouse.get_pressed()) and desenhando is True:
                posicao_atual = pygame.mouse.get_pos()
                pontos.append((posicao_inicial, posicao_atual))
                desenhando = False
            
            # traçando as retas já feitas
            for i in range(len(pontos)):
                convencional(self.janela, (0,0,0), pontos[i][0], pontos[i][1])                                                                       

            pygame.display.flip()


janela = InterfaceDesenho()