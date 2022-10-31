from bresenham import bresenham
import pygame


# classe da interface de desenho
class InterfaceDesenho:
    def __init__(self) -> None:
        # iniciando a janela
        janela = pygame.display.set_mode((320, 240)) #tamanho da Janela

        # lista de pontos para desenhar
        pontos = []

        # variável para indicar se deve fazer a linha em tempo real ou não
        inicia = False

        # loop infinito para verificar de alguém estpa tentando desenhar
        while True:

            # loop pela lista de eventos
            for event in pygame.event.get():
                # se o evento foi de saída, fechar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(1)
            
            #preenchendo a janela apenas com braco no fundo
            janela.fill((255, 255, 255))

            if any(pygame.mouse.get_pressed()) and not inicia:
                posStart = pygame.mouse.get_pos()
                inicia = True

            if inicia:
                posNow = pygame.mouse.get_pos()
                #pygame.draw.line(window, (255, 0, 0), (posStart[0], posStart[1]), (posNow[0], posNow[1]))
                bresenham(janela, (255,0,0), posStart[0], posStart[1], posNow[0], posNow[1])
                #print(pixel, end = '\n\n\n')
                #line_bresenham(window, (255, 0, 0), posStart[0], posStart[1], posNow[0], posNow[1])                                                                                  

            if not any(pygame.mouse.get_pressed()) and inicia:
                pontos.append((posStart, posNow))
                inicia = False

            for i in range(len(pontos)):
                #pygame.draw.line(window, (0, 0, 0), (points[i][0][0], points[i][0][1]), (points[i][1][0], points[i][1][1]))
                #line_bresenham(window, (0, 0, 0), posStart[0], posStart[1], posNow[0], posNow[1])
                bresenham(janela, (0, 0, 0), pontos[i][0][0], pontos[i][0][1], pontos[i][1][0], pontos[i][1][1])                                                                              

            pygame.display.flip()


    def linhas_convencional(slef):
        pass

    
    def linhas_bresenham(self):
        pass


janela = InterfaceDesenho()