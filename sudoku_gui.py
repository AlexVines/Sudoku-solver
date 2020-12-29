import pygame
import numpy as np
import solver

pygame.init()

window_width, window_height = 450, 450
window = pygame.display.set_mode((window_width, window_height+100))
pygame.display.set_caption('Sudoku Solver')
delay = 27

BACKGROUND_COL = (255, 255, 255)
LINE_COL = (0, 0, 0)
RECT_COL = (200, 0, 0)
SELECTED_COL = (139, 0, 0)
BUTTON_COL = (128, 128, 128)

line_width = 1
cube_size = window_width//9


class Cube:
    def __init__(self, value, row, col):
        self.val = value
        self.row = row
        self.col = col
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont('comicsans', 40)
        text = fnt.render(str(self.val), 1, (0, 0, 0))
        if self.val != 0:
            win.blit(text, (self.row * cube_size+20, self.col * cube_size+10))
        if self.selected:
            pygame.draw.rect(win, SELECTED_COL, (self.row * cube_size, self.col * cube_size, cube_size, cube_size), 5)


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-1, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('timesnewroman', 20)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width//2 - text.get_width()//2),
                            self.y + (self.height//2 - text.get_width()//2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


def draw_game_window():
    window.fill(BACKGROUND_COL)
    draw_grid()
    solve.draw(window)
    clear.draw(window)
    for i in range(9):
        for j in range(9):
            cube[i][j].draw(window)
    pygame.display.update()


def draw_line(x, y, width, height):
    pygame.draw.rect(window, LINE_COL, (x, y, width, height))


def draw_grid():
    for i in range(10):
        if i % 3 != 0:
            draw_line(i * window_width//9, 0, line_width, window_height)
            draw_line(0, i * window_height // 9, window_height, line_width)
        else:
            draw_line(i * window_width // 9, 0, line_width+2, window_height)
            draw_line(0, i * window_height // 9, window_height, line_width + 2)


def clear_screen():
    for i in range(9):
        for j in range(9):
            cube[i][j].val = 0


def get_grid():
    nums = []
    for i in range(9):
        nums.append([cube[i][j].val for j in range(9)])
    print(np.matrix(nums))


def main():
    run = True
    i = 0
    j = 0
    while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                cube[i][j].selected = False
                pos = pygame.mouse.get_pos()
                if pos[1] < window_height:
                    i = pos[0] // 50
                    j = pos[1] // 50
                    cube[i][j].selected = True
                
                elif solve.is_over(pos):
                    get_grid()

                elif clear.is_over(pos):
                    clear_screen()
                # print(mx // 50, my // 50)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    cube[i][j].val = 1
                    cube[i][j].selected = False
                elif event.key == pygame.K_2:
                    cube[i][j].val = 2
                    cube[i][j].selected = False
                elif event.key == pygame.K_3:
                    cube[i][j].val = 3
                    cube[i][j].selected = False
                elif event.key == pygame.K_4:
                    cube[i][j].val = 4
                    cube[i][j].selected = False
                elif event.key == pygame.K_5:
                    cube[i][j].val = 5
                    cube[i][j].selected = False
                elif event.key == pygame.K_6:
                    cube[i][j].val = 6
                    cube[i][j].selected = False
                elif event.key == pygame.K_7:
                    cube[i][j].val = 7
                    cube[i][j].selected = False
                elif event.key == pygame.K_8:
                    cube[i][j].val = 8
                    cube[i][j].selected = False
                elif event.key == pygame.K_9:
                    cube[i][j].val = 9
                    cube[i][j].selected = False
                elif event.key == pygame.K_SPACE:
                    cube[i][j].val = 0
                    cube[i][j].selected = False

        draw_game_window()


if __name__ == '__main__':
    cube = []
    solve = Button(BUTTON_COL, 250, window_height + 50, 100, 50, 'Solve')
    clear = Button(BUTTON_COL, 50, window_height + 50, 100, 50, 'Clear')
    for w in range(9):
        cube_row = [Cube(solver.grid[w][j], w, j) for j in range(9)]
        cube.append(cube_row)
    main()
