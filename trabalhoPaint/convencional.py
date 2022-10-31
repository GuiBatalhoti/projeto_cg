from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
## nome do programa
pygame.display.set_caption("Drawing Program")

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            ## desenhando o retangulo
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    ## desenhando as linhas
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
                            ## tela, cor, posicao x, posicao y
            pygame.draw.line(win, BLACK, (0, i*PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for j in range(COLS + 1):
                             ## tela, cor, posicao x, posicao y
            pygame.draw.line(win, BLACK, (j*PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw_line(grid, posStart, posNow, drawing_color):
    #print('\n\n\n', posStart, '\n\n', posNow, '\n\n\n')
    x1, y1 = posStart
    x2, y2 = posNow
    #x1, y1 = get_row_col_from_pos(posStart)
    #x2, y2 = get_row_col_from_pos(posNow)
    #print('\n\n\n', x1, y1, '\n\n', x2, y2, '\n\n\n')
    #print(x1, x2, y1, y2)
    #if not (x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0)

    m = (y2 - y1) / (x2 - x1)
    inc = -1
    if x2 > x1:
        inc = 1
    x = x1
    y = y1
    while y2 > y:
        #draw(win, grid, buttons)
        row, col = get_row_col_from_pos((x, y))
        grid[row][col] = drawing_color
        #pygame.draw.line(win, BLACK, (x, y))
        y += inc
        x = int((y-y1) / (m + x1))




def draw(win, grid, buttons):
    ## preenche a tela com a cor de fundo
    win.fill(BG_COLOR)
    ## desenha o estado inicial
    draw_grid(win, grid)  

    for button in buttons:
        button.draw(win)

    ## atualiza a tela
    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    ## pegando a coluna e a linha do pixel
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col 


def init_grid(rows, cols, color):
    '''
    matriz de cores inicial
    [
        [(0,0,0)][(0,0,0)][(0,0,0)]
        [(0,0,0)][(0,0,0)][(0,0,0)]
        [(0,0,0)][(0,0,0)][(0,0,0)]
    ]
    '''
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid


clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
run = True

drawing_line = False
drawing = False
last_pos = None
mouse_position = (0, 0)

## pesquisar isso no video
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25

buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, 'Erase', BLACK),
    Button(310, button_y, 50, 50, WHITE, 'Clear', BLACK),
    Button(370, button_y, 50, 50, WHITE, 'Line', BLACK)
]

while run:
    ## rodando o loop em até 60 fps
    clock.tick(FPS)
    ## evento que verifica se o usuario clicou no x para fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        ## ao pressionar o mouse em algum lugar
        if pygame.mouse.get_pressed()[0]:
            ## pega a posição do mouse
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                ## desenha na posição
                grid[row][col] = drawing_color

            except IndexError:
                ## vendo se clicou no botão
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    if button.text == 'Line':
                        print('chegou aqui')
                        #allow_line(grid, drawing_color)
                        draw_line(grid, (0, 0), (499, 499), drawing_color = BLACK)
                        #grid = init_grid(ROWS, COLS, BG_COLOR)

                    if button.text == 'Clear':
                        ## resetando a tela
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        drawing_line = False
                    ## mudando a cor do desenho
                    drawing_color = button.color
                    break
    
    
    draw(WIN, grid, buttons)

pygame.quit()


