from enum import Enum
from typing import Optional

class DiskColor(Enum):
    RED = 1
    YELLOW = 2

class Board:
    def __init__(self, num_rows: int = 6, num_cols: int = 7):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid : list[list[Optional[DiskColor]]] = [
            [None for _ in range(num_cols)] for _ in range(num_rows) 
        ]
    
    def get_num_rows(self) -> int:
        return self.num_rows

    def get_num_cols(self) -> int:
        return self.num_cols
    
    def get_cell(self, row: int, col: int) -> Optional[DiskColor]:
        if not self._in_bounds(row, col):
            return None

        return self.grid[row][col]

    def can_place(self, col: int) -> bool:
        if col < 0 or col >= self.num_cols:
            return False

        return self.grid[0][col]is None

    def place_disk(self, col: int, color: DiskColor) -> int:
        if not self.can_place(col):
            return -1

        for row in range(self.num_rows - 1, -1, -1):
            if self.grid[row][col] is None:
                self.grid[row][col] = color
                return row
            
        return -1

    def is_full(self) -> bool:
        for col in range(self.num_cols):
            if self.can_place(col):
                return False
        
        return True

    def check_win(self, row: int, col: int) -> bool:
        directions = [[0, 1], [1, 0], [1, 1], [1, -1]] # → ↑ ↗ ↘

        for dr, dc in directions:
            count = 1
            r, c = row + dr, col + dc

            # scan in direction
            while self._in_bounds(r, c) and self.grid[r][c] and self.grid[r][c] == self.grid[row][col]:
                r += dr
                c += dc
                count += 1

            r, c = row - dr, col - dc

            # scan in opposite direction
            while self._in_bounds(r, c) and self.grid[r][c] and self.grid[r][c] == self.grid[row][col]:
                r -= dr
                c -= dc
                count += 1

            if count >= 4:
                return True
        
        return False

    def _in_bounds(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.num_rows:
            return False

        if col < 0 or col >= self.num_cols:
            return False

        return True

    # Used only for testing purposes.
    def _set_state(self, cells: list[list[int | DiskColor]]) -> None:
        grid = [[None for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        for cell in cells:
            if len(cell) != 3:
                raise ValueError("Each cell must contain row, col, and color")

            row, col, color = cell

            if type(row) is not int or type(col) is not int:
                raise ValueError("Row and column must be integers")

            if not self._in_bounds(row, col):
                raise ValueError("Cell coordinates are out of bounds")

            if not isinstance(color, DiskColor):
                raise ValueError("Color must be a DiskColor")

            grid[row][col] = color

        self.grid = grid