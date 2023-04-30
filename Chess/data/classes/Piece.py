import pygame

class Piece:
	def __init__(self, pos, color, board):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.color = color
		self.has_moved = False
		self.leftEP = False
		self.rightEP = False
	def move(self, board, square, force=False):

		for i in board.squares:
			i.highlight = False

		if square in self.get_valid_moves(board) or force:
			prev_square = board.get_square_from_pos(self.pos)
			self.pos, self.x, self.y = square.pos, square.x, square.y

			prev_square.occupying_piece = None
			if square.occupying_piece is not None:
				if self.color == 'white':
					board.whiteCaps.append(square.occupying_piece)
				else: board.blackCaps.append(square.occupying_piece)
			square.occupying_piece = self
			board.selected_piece = None
			self.has_moved = True
	
			# Pawn promotion
			if self.notation == ' ':
				if self.y == 0 or self.y == 7:
					from data.classes.pieces.Queen import Queen
					square.occupying_piece = Queen(
						(self.x, self.y),
						self.color,
						board
					)
					print('pawn promoted')
				#en passant
				if (self.leftEP or self.rightEP):
					if board.side == 'white':
						if self.color == 'white':
							squareBack = board.get_square_from_pos((self.x, self.y + 1))
							if squareBack.occupying_piece.notation == ' ':
								board.whiteCaps.append(squareBack.occupying_piece)
								squareBack.occupying_piece = None

						elif self.color == 'black':
							squareBack = board.get_square_from_pos((self.x, self.y - 1))
							if squareBack.occupying_piece.notation == ' ':
								board.blackCaps.append(squareBack.occupying_piece)
								squareBack.occupying_piece = None
							

					elif board.side == 'black':
						if self.color == 'black':
							squareBack = board.get_square_from_pos((self.x, self.y + 1))
							if squareBack.occupying_piece.notation == ' ':
								board.blackCaps.append(squareBack.occupying_piece)
								squareBack.occupying_piece = None

						elif self.color == 'white':
							squareBack = board.get_square_from_pos((self.x, self.y - 1))
							if squareBack.occupying_piece.notation == ' ':
								board.whiteCaps.append(squareBack.occupying_piece)
								squareBack.occupying_piece = None
					
    
				if abs(prev_square.y - self.y) == 2:
					
					squareleft = board.get_square_from_pos((self.x - 1, self.y))
					squareright = board.get_square_from_pos((self.x + 1, self.y))
					if self.x != 0:
						if squareleft.occupying_piece is not None:
							if squareleft.occupying_piece.notation == ' ':
								squareleft.occupying_piece.rightEP = True
								
								
					if self.x != 7:
						if squareright.occupying_piece is not None:
							if squareright.occupying_piece.notation == ' ':
								squareright.occupying_piece.leftEP = True	
						

				
	
			
			# Move rook if king castles
			if self.notation == 'K':
				if prev_square.x - self.x == 2:
					rook = board.get_piece_from_pos((0, self.y))
					rook.move(board, board.get_square_from_pos((3, self.y)), force=True)
				elif prev_square.x - self.x == -2:
					rook = board.get_piece_from_pos((7, self.y))
					rook.move(board, board.get_square_from_pos((5, self.y)), force=True)
			
			return True
		else:
			board.selected_piece = None
			return False
		


	def get_moves(self, board):
		output = []
		for direction in self.get_possible_moves(board):
			for square in direction:
				if square.occupying_piece is not None:
					if square.occupying_piece.color == self.color:
						break
					else:
						output.append(square)
						break
				else:
					output.append(square)

		return output


	def get_valid_moves(self, board):
		output = []
		for square in self.get_moves(board):
			if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
				output.append(square)

		return output


	# True for all pieces except pawn
	def attacking_squares(self, board):
		return self.get_moves(board)