#include "board.hpp"
#include <stdexcept>
#include <utility>

Board::Board(int numRows, int numCols)
    : numRows(numRows),
      numCols(numCols),
      grid(numRows, std::vector<std::optional<DiskColor>>(numCols)) {}

bool Board::inBounds(int row, int col) {
    if (row < 0 || row >= numRows) {
        return false;
    }
    
    if (col < 0 || col >= numCols) {
        return false;
    }

    return true;
}

int Board::getNumRows() {
    return numRows;
}

int Board::getNumCols() {
    return numCols;
}

std::optional<DiskColor> Board::getCell(int row, int col) {
    if (!inBounds(row, col)) {
        return std::nullopt;
    }

    return grid[row][col];
}

bool Board::canPlace(int col) {
    if (col < 0 || col >= numCols) {
        return false;
    }

    return grid[0][col] == std::nullopt;
}

int Board::placeDisk(int col, DiskColor color) {
    if (!canPlace(col)) {
        return -1;
    }
    
    for (int row = numRows-1; row >= 0; --row) {
        if (grid[row][col] == std::nullopt) {
            grid[row][col] = color;
            return row;
        }
    }

    return -1;
}

bool Board::isFull() {
    for (int col = 0; col < numCols; ++col) {
        if (canPlace(col)) {
            return false;
        }
    }

    return true;
}

bool Board::checkWin(int row, int col) {
    if (!inBounds(row, col) || !grid[row][col].has_value()) {
        return false;
    }

    std::vector<std::pair<int, int>> directions = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};

    for (auto& [dr, dc] : directions) {
        int count = 1;
        int r = row + dr;
        int c = col + dc;

        // scan in direction
        while (inBounds(r, c) && grid[r][c] != std::nullopt && grid[r][c] == grid[row][col]) {
            ++count;
            r = r + dr;
            c = c + dc;
        }

        r = row - dr;
        c = col - dc;

        // scan in opposite direction
        while (inBounds(r, c) && grid[r][c] != std::nullopt && grid[r][c] == grid[row][col]) {
            ++count;
            r = r - dr;
            c = c - dc;
        }

        if (count >= 4) {
            return true;
        }
    }

    return false;
}

void Board::setState(const std::vector<std::tuple<int, int, DiskColor>>& cells) {
    std::vector<std::vector<std::optional<DiskColor>>> newGrid(
        numRows, std::vector<std::optional<DiskColor>>(numCols));

    for (const auto& [row, col, color] : cells) {
        if (!inBounds(row, col)) {
            throw std::invalid_argument("Cell coordinates are out of bounds");
        }
        if (color != RED && color != YELLOW) {
            throw std::invalid_argument("Color must be RED or YELLOW");
        }
        newGrid[row][col] = color;
    }

    grid = std::move(newGrid);
}
