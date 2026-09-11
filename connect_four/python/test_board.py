import unittest

from board import Board, DiskColor

class TestBoard(unittest.TestCase):
    def test_is_full(self):
        board = Board(num_rows=2, num_cols=2)
        self.assertFalse(board.is_full())

        board._set_state([
            [0, 0, DiskColor.RED],
            [0, 1, DiskColor.YELLOW],
            [1, 0, DiskColor.YELLOW],
            [1, 1, DiskColor.RED],
        ])

        self.assertTrue(board.is_full())

    def test_can_place(self):
        board = Board()
        self.assertTrue(board.can_place(0))
        self.assertFalse(board.can_place(-1))
        self.assertFalse(board.can_place(7))

        for _ in range(6):
            board.place_disk(0, DiskColor.RED)

        self.assertFalse(board.can_place(0))
        self.assertEqual(board.place_disk(0, DiskColor.YELLOW), -1)

    def test_place_disk(self):
        board = Board()
        self.assertEqual(board.place_disk(0, DiskColor.RED), 5)
        self.assertEqual(board.place_disk(0, DiskColor.YELLOW), 4)
        self.assertEqual(board.get_cell(5, 0), DiskColor.RED)
        self.assertEqual(board.get_cell(4, 0), DiskColor.YELLOW)

    def test_new_board_is_empty(self):
        board = Board()
        for row in range(board.get_num_rows()):
            for col in range(board.get_num_cols()):
                self.assertIsNone(board.get_cell(row, col))

    def test_check_win(self):
        board = Board()
        board._set_state([
            [5, 0, DiskColor.RED],
            [5, 1, DiskColor.RED],
            [5, 2, DiskColor.RED],
        ])

        self.assertFalse(board.check_win(5, 1))

        board.place_disk(3, DiskColor.RED)
        self.assertTrue(board.check_win(5, 1))
