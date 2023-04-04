import pygame

from data.classes.Board import Board

pygame.init()
WINDOW_SIZE = (575, 280)
screen = pygame.display.set_mode(WINDOW_SIZE)
black_img = pygame.image.load('data/imgs/b_king.png')
white_img = pygame.image.load('data/imgs/w_king.png')
pygame.display.set_caption("Select Your Pieces")


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


white_button = Button(25, 15, white_img)
black_button = Button(300, 15, black_img)
selectMenu = True
screen.fill("red")
while selectMenu:

    if white_button.draw():
        board = Board(700, 700, 'white')
        board.robot_turn = 'black'
        selectMenu = False
    if black_button.draw():
        board = Board(700, 700, 'black')
        board.robot_turn = 'white'
        selectMenu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selectMenu = False
    pygame.display.update()

WINDOW_SIZE = (700, 700)
screen = pygame.display.set_mode(WINDOW_SIZE)


def draw(display):
    display.fill('white')

    board.draw(display)

    pygame.display.update()


running = True
while running:
    mx, my = pygame.mouse.get_pos()
    board.robot()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.handle_click(mx, my)
    if board.is_in_checkmate('black'):
        if board.is_in_check('black'):
            print('White wins!')
        else:
            print('Stalemate!')
        running = False
    elif board.is_in_checkmate('white'):
        if board.is_in_check('white'):
            print('Black wins!')
        else:
            print('Stalemate!')
        running = False

    draw(screen)
