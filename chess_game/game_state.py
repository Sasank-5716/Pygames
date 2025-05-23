from board import create_start_board
from constants import WHITE, BLACK
from pieces import King, Queen, Rook, Bishop, Knight, Pawn

class GameState:
    def __init__(self):
        self.board = create_start_board()
        self.turn = WHITE
        self.selected = None
        self.hover = None
        self.move_history = []
        self.checkmate = False
        self.stalemate = False
        self.en_passant_target = None

    def make_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        captured = self.board[end_row][end_col]
        # Handle castling
        if isinstance(piece, King) and abs(start_col - end_col) == 2:
            piece = Queen(piece.color, (end_row, end_col))

            # Kingside
            if end_col == 6:
                rook = self.board[start_row][7]
                self.board[start_row][5] = rook
                self.board[start_row][7] = None
                rook.pos = (start_row, 5)
            # Queenside
            else:
                rook = self.board[start_row][0]
                self.board[start_row][3] = rook
                self.board[start_row][0] = None
                rook.pos = (start_row, 3)

        # Handle en passant
        if isinstance(piece, Pawn) and end == self.en_passant_target:
            captured_pawn_row = end_row + 1 if piece.color == WHITE else end_row - 1
            self.board[captured_pawn_row][end_col] = None

        # Update en passant target
        self.en_passant_target = None
        if isinstance(piece, Pawn) and abs(start_row - end_row) == 2:
            self.en_passant_target = (end_row + (1 if piece.color == WHITE else -1), end_col)

        # Handle pawn promotion
        if isinstance(piece, Pawn) and end_row in [0, 7]:
            piece = Queen(piece.color, (end_row, end_col))

        # Update board state
        self.board[start_row][start_col] = None
        self.board[end_row][end_col] = piece
        piece.pos = (end_row, end_col)
        piece.has_moved = True

         # Switch turns
        self.turn = BLACK if self.turn == WHITE else WHITE
        self.move_history.append((start, end))
        self.check_game_over()

    def in_check(self):
        king_pos = None
        # Find king
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, King) and piece.color == self.turn:
                    king_pos = (r,c)
                    break
            if king_pos: break
        
        # Check if any opponent piece attacks king
        if king_pos:
            for r in range(8):
                for c in range(8):
                    piece = self.board[r][c]
                    if piece and piece.color != self.turn:
                        if piece.attacks(self.board, king_pos):
                            return True
            return False
    
    def get_all_legal_moves(self, color):
        moves = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color == color:
                    for move in piece.get_legal_moves(self.board):
                        if self.is_valid_move((r, c), move):
                            moves.append(((r, c), move))
        return moves
    
    def is_valid_move(self, start, end):
        # Create deep copy of game state for validation
        temp_board = [row.copy() for row in self.board]
        temp_piece = temp_board[start[0]][start[1]]
        
        # Simulate move
        temp_board[end[0]][end[1]] = temp_piece
        temp_board[start[0]][start[1]] = None
        temp_piece.pos = end
        
        original_turn = self.turn
        self.turn = 'white' if self.turn == 'black' else 'black'  # Flip turn
        in_check = self.in_check()
        self.turn = original_turn  # Restore original turn
        return not in_check
    
    def check_game_over(self):
        moves = self.get_all_legal_moves(self.turn)
        if not moves:
            if self.in_check():
                self.checkmate = True
            else:
                self.stalemate = True
