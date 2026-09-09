import unittest

from board import Board, DiskColor

class TestBoard(unittest.TestCase):
    def test_isFull(self):
        board = Board(numRows=2, numCols=2)
        self.assertFalse(board.isFull())

        board._setState([
            [0, 0, DiskColor.RED],
            [0, 1, DiskColor.YELLOW],
            [1, 0, DiskColor.YELLOW],
            [1, 1, DiskColor.RED],
        ])

        self.assertTrue(board.isFull())

    def test_canPlace(self):
        board = Board()
        self.assertTrue(board.canPlace(0))
        self.assertFalse(board.canPlace(-1))
        self.assertFalse(board.canPlace(7))

        for _ in range(6):
            board.placeDisk(0, DiskColor.RED)

        self.assertFalse(board.canPlace(0))
        self.assertEqual(board.placeDisk(0, DiskColor.YELLOW), -1)

    def test_placeDisk(self):
        board = Board()
        self.assertEqual(board.placeDisk(0, DiskColor.RED), 5)
        self.assertEqual(board.placeDisk(0, DiskColor.YELLOW), 4)
        self.assertEqual(board.getCell(5, 0), DiskColor.RED)
        self.assertEqual(board.getCell(4, 0), DiskColor.YELLOW)

    def test_new_board_is_empty(self):
        board = Board()
        for row in range(board.getNumRows()):
            for col in range(board.getNumCols()):
                self.assertIsNone(board.getCell(row, col))

    def test_checkWin(self):
        board = Board()
        board._setState([
            [5, 0, DiskColor.RED],
            [5, 1, DiskColor.RED],
            [5, 2, DiskColor.RED],
        ])

        self.assertFalse(board.checkWin(5, 1))

        board.placeDisk(3, DiskColor.RED)
        self.assertTrue(board.checkWin(5, 1))
