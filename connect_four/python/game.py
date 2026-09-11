from enum import Enum
from typing import Optional

from board import Board
from player import Player

class GameState(Enum):
    IN_PROGRESS = 1
    WON = 2
    DRAW = 3

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.state = GameState.IN_PROGRESS
        self.winner : Optional[Player] = None

    def make_move(self, player: Player, col: int) -> bool:
        if self.state is not GameState.IN_PROGRESS:
            return False
        
        if player is not self.current_player:
            return False

        row = self.board.place_disk(col, player.color)
        
        if row == -1:
            return False

        if self.board.check_win(row, col):
            self.state = GameState.WON
            self.winner = player
        
        elif self.board.is_full():
            self.state = GameState.DRAW

        else:
            if self.current_player is self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1

        return True

    def get_current_player(self) -> Player:
        return self.current_player

    def get_game_state(self) -> GameState:
        return self.state

    def get_winner(self) -> Optional[Player]:
        return self.winner

    def get_board(self) -> Board:
        return self.board
