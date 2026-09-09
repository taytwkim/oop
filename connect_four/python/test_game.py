import unittest

from board import DiskColor
from game import Game, GameState
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Alice", DiskColor.RED)
        self.player2 = Player("Bob", DiskColor.YELLOW)
        self.game = Game(self.player1, self.player2)

    def test_initial_state(self):
        self.assertEqual(self.game.getGameState(), GameState.IN_PROGRESS)
        self.assertIs(self.game.getCurrentPlayer(), self.player1)
        self.assertIsNone(self.game.getWinner())

    def test_valid_move_switches_turn(self):
        self.assertTrue(self.game.makeMove(self.player1, 0))
        self.assertEqual(self.game.getBoard().getCell(5, 0), DiskColor.RED)
        self.assertIs(self.game.getCurrentPlayer(), self.player2)

        self.assertTrue(self.game.makeMove(self.player2, 0))
        self.assertEqual(self.game.getBoard().getCell(4, 0), DiskColor.YELLOW)
        self.assertIs(self.game.getCurrentPlayer(), self.player1)

    def test_wrong_player_is_rejected(self):
        self.assertFalse(self.game.makeMove(self.player2, 0))
        self.assertIsNone(self.game.getBoard().getCell(5, 0))
        self.assertIs(self.game.getCurrentPlayer(), self.player1)

    def test_invalid_column_keeps_turn(self):
        self.assertFalse(self.game.makeMove(self.player1, -1))
        self.assertFalse(self.game.makeMove(self.player1, 7))
        self.assertIs(self.game.getCurrentPlayer(), self.player1)
        self.assertEqual(self.game.getGameState(), GameState.IN_PROGRESS)

    def test_winning_game(self):
        for col in [0, 0, 1, 1, 2, 2, 3]:
            player = self.game.getCurrentPlayer()
            self.assertTrue(self.game.makeMove(player, col))

        self.assertEqual(self.game.getGameState(), GameState.WON)
        self.assertIs(self.game.getWinner(), self.player1)
        self.assertFalse(self.game.makeMove(self.player1, 4))
        self.assertIsNone(self.game.getBoard().getCell(5, 4))
