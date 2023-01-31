# import the necessary libraries
class Chess:
    def __init__(self):
        self.board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
        self.turn = 'white'
    def move(self, start, end):
        start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
        end_x, end_y = ord(end[0]) - ord('a'), int(end[1]) - 1
        piece = self.board[start_x][start_y]
        if piece.isupper() != (self.turn == 'white'):
            print("It's not your turn!")
            return
        if not self.valid_move(start_x, start_y, end_x, end_y):
            print("Invalid move!")
            return
        self.board[end_x][end_y] = piece
        self.board[start_x][start_y] = '.'
        self.turn = 'black' if self.turn == 'white' else 'white'
    def valid_move(self, start_x, start_y, end_x, end_y):
        piece = self.board[start_x][start_y]
        if piece == '.':
            return False
        if piece.upper() == 'P':
            return self.valid_pawn_move(start_x, start_y, end_x, end_y)
        elif piece.upper() == 'R':
            return self.valid_rook_move(start_x, start_y, end_x, end_y)
        # Add more elif statements for other pieces
    def valid_pawn_move(self, start_x, start_y, end_x, end_y):
        if self.turn == 'white':
            if start_x == 1 and end_x == 3 and start_y == end_y:
                return True
            elif start_x == end_x - 1 and start_y == end_y:
                return True
        else:
            if start_x == 6 and end_x == 4 and start_y == end_y:
                return True
            elif start_x == end_x + 1 and start_y == end_y:
                return True
    def valid_rook_move(self, start_x, start_y, end_x, end_y):
        if start_x != end_x and start_y != end_y:
            return False
        if start_x == end_x:
            for i in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                if self.board[start_x][i] != '.':
                    return False
        else:
            for i in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                if self.board[i][start_y] != '.':
                    return False
        return True
    def display(self):
        for row in self.board:
            print(' '.join(row))

game = Chess()
game.move("e2", "e4")
game.move("e7", "e5")
game.move("d2", "d4")
game.display()
