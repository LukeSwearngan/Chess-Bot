import pygame

from data.classes.Square import Square
from data.classes.pieces.Rook import Rook
from data.classes.pieces.Bishop import Bishop
from data.classes.pieces.Knight import Knight
from data.classes.pieces.Queen import Queen
from data.classes.pieces.King import King
from data.classes.pieces.Pawn import Pawn
import random
class Board:
	def __init__(self, width, height, side):
		self.width = width
		self.height = height
		self.square_width = width // 8
		self.square_height = height // 8
		self.selected_piece = None
		self.turn = 'white'
		self.side = side
		if self.side == 'white':
			self.config = [
				['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
				['b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b '],
				['','','','','','','',''],
				['','','','','','','',''],
				['','','','','','','',''],
				['','','','','','','',''],
				['w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w '],
				['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
			]
		self.squares = self.generate_squaresWhite()
		if self.side == 'black':
			self.config = [
				['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR'],
				['w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w '],
				['','','','','','','',''],
				['','','','','','','',''],
				['','','','','','','',''],
				['','','','','','','',''],
				['b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b '],
				['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR'],
			]
		self.squares = self.generate_squaresWhite()
		

		self.setup_board()

	def generate_squaresWhite(self):
		output = []
		for y in range(8):
			for x in range(8):
				output.append(
					Square(
						x,
						y,
						self.square_width,
						self.square_height
					)
				)

		return output

	""" def generate_squaresBlack(self):
		output = []
		for y in range(7,-1,-1):
			for x in range(7,-1,-1):
				output.append(
					Square(
						x,
						y,
						self.square_width,
						self.square_height
					)
				)

		return output """


	def setup_board(self):
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '':
					square = self.get_square_from_pos((x, y))

					if piece[1] == 'R':
						square.occupying_piece = Rook(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'N':
						square.occupying_piece = Knight(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'B':
						square.occupying_piece = Bishop(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'Q':
						square.occupying_piece = Queen(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'K':
						square.occupying_piece = King(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == ' ':
						square.occupying_piece = Pawn(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

	def robot(self):
		moves = {}
		pieces = []
		if self.turn == self.robot_turn:
			for piece in [i.occupying_piece for i in self.squares]:
				if piece != None and piece.color == self.turn and not piece.get_valid_moves(self) == []:
					moves[piece] = piece.get_valid_moves(self)
					pieces.append(piece)
					#piece.move(self, piece.get_valid_moves(self)[0])
					#self.turn = 'white'
					#return
			p = random.randint(0, len(pieces) - 1)
			pieces[p].move(self, pieces[p].get_valid_moves(self)[random.randint(0, len(pieces[p].get_valid_moves(self))-1)])
			if self.turn == 'white':
				self.turn = 'black'
			else:
				self.turn = 'white'
			#print(self.squares)

	def handle_click(self, mx, my):
		x = mx // self.square_width
		y = my // self.square_height
		clicked_square = self.get_square_from_pos((x, y))
		if self.selected_piece is None:
			if clicked_square.occupying_piece is not None:
				if clicked_square.occupying_piece.color == self.turn:
					self.selected_piece = clicked_square.occupying_piece

		elif self.selected_piece.move(self, clicked_square):
			self.turn = 'white' if self.turn == 'black' else 'black'

		elif clicked_square.occupying_piece is not None:
			if clicked_square.occupying_piece.color == self.turn:
				self.selected_piece = clicked_square.occupying_piece

	def eval(self):

		wValue = 0
		bValue = 0
	
		for piece in [i.occupying.piece for i in self.squares]:
				if piece[1] == 'R':
						if piece[0] == 'w':
							wValue += 525
						else:
							bValue += 525

				elif piece[1] == 'N':
						if piece[0] == 'w':
							wValue += 300
						else:
							bValue += 300
						

				elif piece[1] == 'B':
						if piece[0] == 'w':
							wValue += 300
						else:
							bValue += 300
						

				elif piece[1] == 'Q':
						if piece[0] == 'w':
							wValue += 1000
						else:
							bValue += 1000
						

				elif piece[1] == 'K':
						if piece[0] == 'w':
							wValue += 10000
						else:
							bValue += 10000
						


				elif piece[1] == ' ':
						if piece[0] == 'w':
							wValue += 100
						else:
							bValue += 100

	def is_in_check(self, color, board_change=None): # board_change = [(x1, y1), (x2, y2)]
		output = False
		king_pos = None
		changing_piece = None
		old_square = None
		new_square = None
		new_square_old_piece = None

		if board_change is not None:
			for square in self.squares:
				if square.pos == board_change[0]:
					changing_piece = square.occupying_piece
					old_square = square
					old_square.occupying_piece = None
			for square in self.squares:
				if square.pos == board_change[1]:
					new_square = square
					new_square_old_piece = new_square.occupying_piece
					new_square.occupying_piece = changing_piece

		pieces = [
			i.occupying_piece for i in self.squares if i.occupying_piece is not None
		]

		if changing_piece is not None:
			if changing_piece.notation == 'K':
				king_pos = new_square.pos
		if king_pos == None:
			for piece in pieces:
				if piece.notation == 'K':
					if piece.color == color:
						king_pos = piece.pos
		for piece in pieces:
			if piece.color != color:
				for square in piece.attacking_squares(self):
					if square.pos == king_pos:
						output = True

		if board_change is not None:
			old_square.occupying_piece = changing_piece
			new_square.occupying_piece = new_square_old_piece
		return output


	def is_in_checkmate(self, color):
		output = False
		moves = []
		for piece in [i.occupying_piece for i in self.squares]:
			if piece != None and piece.color == color and not piece.get_valid_moves(self) == []:
					moves.append(piece.notation)


		if moves == []:
			output = True
		return output


	def get_square_from_pos(self, pos):
		for square in self.squares:
			if (square.x, square.y) == (pos[0], pos[1]):
				return square


	def get_piece_from_pos(self, pos):
		return self.get_square_from_pos(pos).occupying_piece


	def draw(self, display):
		if self.selected_piece is not None:
			self.get_square_from_pos(self.selected_piece.pos).highlight = True
			for square in self.selected_piece.get_valid_moves(self):
				square.highlight = True

		for square in self.squares:
			square.draw(display)
	def copy(self, new):
		new.squares = self.squares.copy()
		new.turn = self.turn
		return new
