import chess
from chess import pgn


def parse_game(pgn_path):
    with open (pgn_path) as chessgame:
        game = pgn.read_game(chessgame)

    moves = []
    board = game.board()

    for game_moves in game.mainline_moves():
        san_nota = board.san(game_moves)
        board.push(game_moves)
        fen_str = board.fen()
        moves.append( {"SAN" : san_nota , "FEN" : fen_str })

    return moves


if __name__ == "__main__":
    result = parse_game("data/sample.pgn")
    for i, m in enumerate(result, 1):
        print(f"Move {i}: {m['SAN']} , {m['FEN']}")        