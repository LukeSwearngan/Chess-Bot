import chess
import numpy as np

fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQ - 0 1'

# Convert FEN string to a chess.Board object
final = ""
fil = open('out.txt')
fil = fil.read().split('\n')
for fen_str in fil:
    if fen_str == 'start':
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    board = chess.Board(fen_str)

    # Create a 2D numpy array to represent the board state
    board_array = np.zeros((8, 8), dtype=np.int8)

    # Map piece types to numeric values
    piece_values = {
        'p': -1,
        'n': -3,
        'b': -3,
        'r': -5,
        'q': -9,
        'k': -100,
        'P': 1,
        'N': 3,
        'B': 3,
        'R': 5,
        'Q': 9,
        'K': 100,
    }

    # Iterate over each square on the board and set the corresponding value in the array
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            piece_value = piece_values[piece.symbol()]
            board_array[chess.square_rank(square)][chess.square_file(square)] = piece_value

    # Add additional features for game state information (e.g. player to move, castling rights, etc.)
    player_to_move = 1 if board.turn == chess.WHITE else -1
    castling_rights = [
        int(board.has_kingside_castling_rights(chess.WHITE)),
        int(board.has_queenside_castling_rights(chess.WHITE)),
        int(board.has_kingside_castling_rights(chess.BLACK)),
        int(board.has_queenside_castling_rights(chess.BLACK))
    ]
    en_passant_square = board.ep_square
    halfmove_clock = board.halfmove_clock
    fullmove_number = board.fullmove_number

    # Concatenate all features into a single input vector
    input_vector = np.concatenate([
        board_array.flatten(),
        [player_to_move],
        castling_rights,
        [en_passant_square],
        [halfmove_clock],
        [fullmove_number]
    ])

    final += str(input_vector) + '\n'
print("fin")
f = open("output.txt", "w")
f.write(final)
f.close()