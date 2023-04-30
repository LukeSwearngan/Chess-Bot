import tensorflow as tf
import chess
import numpy as np
from data.classes.Board import Board
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(8, 8, 12)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(4096, activation='softmax')
])
def convert_fen_to_array(fen):
    board = chess.Board(fen)
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

# Convert a move to a numerical array
def convert_move_to_array(move):
    array = np.zeros((8, 8, 2), dtype=np.int8)
    array[chess.square_rank(move.from_square)][chess.square_file(move.from_square)][0] = 1
    array[chess.square_rank(move.to_square)][chess.square_file(move.to_square)][1] = 1
    return array
def get_move(prev, curr):
    pass
def generate_training_data(fen_list):
    positions = []
    moves = []
    board = None
    x = []
    y = []
    prev = ''
    for fen in fen_list:
        if fen == 'start':
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        else:
            moves.append(get_move(prev, fen))
        board = chess.Board(fen)
        positions.append(str(board))

    for position in positions:
        x.append(convert_fen_to_array(position))
        print(x)
        x = np.array(x)
        # Convert the moves to numerical arrays
    for move in moves:
        y.append(convert_move_to_array(move))
        y = np.array(y)

           # for move in legal_moves:
            #    positions.append(convert_fen_to_array(board))
             #   moves.append(convert_move_to_array(move))
             #   board.push(move)
    return x, y

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

X_train, y_train = generate_training_data(open('out.txt').read().split('\n'))
model.fit(X_train, y_train, epochs=10, batch_size=32)