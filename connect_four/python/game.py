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
        self.currPlayer = player1
        self.state = GameState.IN_PROGRESS
        self.winner : Optional[Player] = None

    def makeMove(self, player: Player, col: int) -> bool:
        if self.state is not GameState.IN_PROGRESS:
            return False
        
        if player != self.currPlayer:
            return False

        row = self.board.placeDisk(col, player.getColor())
        
        if row == -1:
            return False

        if self.board.checkWin(row, col):
            self.state = GameState.WON
            self.winner = player
        
        elif self.board.isFull():
            self.state = GameState.DRAW

        else:
            if self.currPlayer == self.player1:
                self.currPlayer = self.player2
            else:
                self.currPlayer = self.player1

        return True

    def getCurrentPlayer(self) -> Player:
        return self.currPlayer

    def getGameState(self) -> GameState:
        return self.state

    def getWinner(self) -> Optional[Player]:
        return self.winner

    def getBoard(self) -> Board:
        return self.board
