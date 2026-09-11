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
        self.assertEqual(self.game.get_game_state(), GameState.IN_PROGRESS)
        self.assertIs(self.game.get_current_player(), self.player1)
        self.assertIsNone(self.game.get_winner())

    def test_valid_move_switches_turn(self):
        self.assertTrue(self.game.make_move(self.player1, 0))
        self.assertEqual(self.game.get_board().get_cell(5, 0), DiskColor.RED)
        self.assertIs(self.game.get_current_player(), self.player2)

        self.assertTrue(self.game.make_move(self.player2, 0))
        self.assertEqual(self.game.get_board().get_cell(4, 0), DiskColor.YELLOW)
        self.assertIs(self.game.get_current_player(), self.player1)

    def test_wrong_player_is_rejected(self):
        self.assertFalse(self.game.make_move(self.player2, 0))
        self.assertIsNone(self.game.get_board().get_cell(5, 0))
        self.assertIs(self.game.get_current_player(), self.player1)

    def test_invalid_column_keeps_turn(self):
        self.assertFalse(self.game.make_move(self.player1, -1))
        self.assertFalse(self.game.make_move(self.player1, 7))
        self.assertIs(self.game.get_current_player(), self.player1)
        self.assertEqual(self.game.get_game_state(), GameState.IN_PROGRESS)

    def test_winning_game(self):
        for col in [0, 0, 1, 1, 2, 2, 3]:
            player = self.game.get_current_player()
            self.assertTrue(self.game.make_move(player, col))

        self.assertEqual(self.game.get_game_state(), GameState.WON)
        self.assertIs(self.game.get_winner(), self.player1)
        self.assertFalse(self.game.make_move(self.player1, 4))
        self.assertIsNone(self.game.get_board().get_cell(5, 4))
