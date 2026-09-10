from enum import Enum
from typing import Optional

class DiskColor(Enum):
    RED = 1
    YELLOW = 2

class Board:
    def __init__(self, numRows: int = 6, numCols: int = 7):
        self.numRows = numRows
        self.numCols = numCols
        self.grid : list[list[Optional[DiskColor]]] = [
            [None for _ in range(numCols)] for _ in range(numRows) 
        ]
    
    def getNumRows(self) -> int:
        return self.numRows

    def getNumCols(self) -> int:
        return self.numCols
    
    def getCell(self, row: int, col: int) -> Optional[DiskColor]:
        if not self._inBounds(row, col):
            return None

        return self.grid[row][col]

    def canPlace(self, col: int) -> bool:
        if col < 0 or col >= self.numCols:
            return False

        return self.grid[0][col]is None

    def placeDisk(self, col: int, color: DiskColor) -> int:
        if not self.canPlace(col):
            return -1

        for row in range(self.numRows - 1, -1, -1):
            if self.grid[row][col] is None:
                self.grid[row][col] = color
                return row
            
        return -1

    def isFull(self) -> bool:
        for col in range(self.numCols):
            if self.canPlace(col):
                return False
        
        return True

    def checkWin(self, row: int, col: int) -> bool:
        directions = [[0, 1], [1, 0], [1, 1], [1, -1]] # → ↑ ↗ ↘

        for dr, dc in directions:
            count = 1
            r, c = row + dr, col + dc

            # scan in direction
            while self._inBounds(r, c) and self.grid[r][c] and self.grid[r][c] == self.grid[row][col]:
                r += dr
                c += dc
                count += 1

            r, c = row - dr, col - dc

            # scan in opposite direction
            while self._inBounds(r, c) and self.grid[r][c] and self.grid[r][c] == self.grid[row][col]:
                r -= dr
                c -= dc
                count += 1

            if count >= 4:
                return True
        
        return False

    def _inBounds(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.numRows:
            return False

        if col < 0 or col >= self.numCols:
            return False

        return True

    # Used only for testing purposes.
    def _setState(self, cells: list[list[int | DiskColor]]) -> None:
        grid = [[None for _ in range(self.numCols)] for _ in range(self.numRows)]

        for cell in cells:
            if len(cell) != 3:
                raise ValueError("Each cell must contain row, col, and color")

            row, col, color = cell

            if type(row) is not int or type(col) is not int:
                raise ValueError("Row and column must be integers")

            if not self._inBounds(row, col):
                raise ValueError("Cell coordinates are out of bounds")

            if not isinstance(color, DiskColor):
                raise ValueError("Color must be a DiskColor")

            grid[row][col] = color

        self.grid = grid