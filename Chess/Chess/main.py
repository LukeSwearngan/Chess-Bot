import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (700, 700)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')

	board.draw(display)

	pygame.display.update()


running = True
while running:
	mx, my = pygame.mouse.get_pos()
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