#pragma once

#include <optional>
#include <tuple>
#include <vector>

enum class DiskColor {
    RED,
    YELLOW
};

class Board {
private:
    int numRows;
    int numCols;
    std::vector<std::vector<std::optional<DiskColor>>> grid;
    bool inBounds(int row, int col) const;    // helper function

public:
    Board(int numRows, int numCols);
    int getNumRows() const;
    int getNumCols() const;
    std::optional<DiskColor> getCell(int row, int col) const;
    bool canPlace(int col) const;
    int placeDisk(int col, DiskColor color);
    bool isFull() const;
    bool checkWin(int row, int col) const;
    void setState(const std::vector<std::tuple<int, int, DiskColor>>& cells);   // for testing
};
