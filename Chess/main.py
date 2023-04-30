import pygame
import random
from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (700,400)
pygame_icon = pygame.image.load('data/imgs/chessterhead.png')
pygame.display.set_icon(pygame_icon)

screen = pygame.display.set_mode(WINDOW_SIZE)
black_img = pygame.image.load('data/imgs/b_king.png')
white_img = pygame.image.load('data/imgs/w_king.png')

pygame.display.set_caption("Select Your Pieces")


class Button():

	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
		self.clicked = False
        
	def draw(self):
		action = False
		pos = pygame.mouse.get_pos()
		
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked == True
				action = True
		screen.blit(self.image, (self.rect.x, self.rect.y))
		return action
  
  
white_button = Button(50,25, white_img)
black_button = Button(400,25, black_img)
whitet = "Play as White"
blackt = "Play as Black"
font = pygame.font.SysFont(None, 40)
whitete = font.render(whitet, True, (255, 255, 255))
blackte = font.render(blackt, True, (255, 255, 255))
whiterec = whitete.get_rect()
blackrec = blackte.get_rect()
whiterec.topleft = (85, 315)
blackrec.topleft = (435, 315)


selectMenu = True
screen.fill("antiquewhite2")
while selectMenu:

	screen.blit(whitete, whiterec)
	screen.blit(blackte, blackrec)
	if white_button.draw():
		board = Board(700,700,'white')
		board.robot_turn = 'black'
		selectMenu = False
	if black_button.draw():
		board = Board(700,700,'black')
		board.robot_turn = 'white'
		selectMenu = False
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			selectMenu = False
	pygame.display.update()
 
WINDOW_SIZE = (1050, 900)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Good Luck!")

openerTalk = ["Get ready to meet your demise.",
			"Checkmate is inevitable, my friend.",
			"Your pieces are going down!",
			"Hope you've practiced your losing face.",
			"This game will be over in a jiffy.",
			"You'll be singing a different tune soon.",
			"You're in for a royal beatdown.",
			"I'm about to school you, fool.",
			"Brace yourself for a defeat.",
			"You'll be bowing down to the king soon."]
		
lineOne = random.choice(openerTalk)
font = pygame.font.SysFont(None, 24)
chatte = font.render(lineOne, True, (255, 255, 255))
chatrec = chatte.get_rect()
chatrec.topleft = (700, 150)

def draw(display):

	display.fill('antiquewhite2')
	
	chessterhead = pygame.image.load('data/imgs/chessterhead.png')
	chessterhead.get_rect().topleft = (700,0)
	screen.blit(chessterhead,(700,0))
	screen.blit(chatte, chatrec)
	board.draw(display)
	
	pygame.display.update()


    pygame.display.update()

running = True
while running:
	mx, my = pygame.mouse.get_pos()
	
	
 
	#board.robot()
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
  
	x = 1
 
	for i in board.blackCaps:
		board.capSquares[x].occupying_piece = i
		x += 2
  
	x = 0
 
	for i in board.whiteCaps:
		
		board.capSquares[x].occupying_piece = i
		x += 2
  
	for i in board.capSquares:
		if  not (i.occupying_piece is  None):
			i.occupying_piece.img = pygame.transform.scale(i.occupying_piece.img, (40,40))
	draw(screen)

