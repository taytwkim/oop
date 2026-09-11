#pragma once

#include <optional>
#include <tuple>
#include <vector>

enum DiskColor {
    RED,
    YELLOW
};

class Board {
private:
    int numRows;
    int numCols;
    std::vector<std::vector<std::optional<DiskColor>>> grid;
    bool inBounds(int row, int col);    // helper function

public:
    Board(int numRows, int numCols);
    int getNumRows();
    int getNumCols();
    std::optional<DiskColor> getCell(int row, int col);
    bool canPlace(int col);
    int placeDisk(int col, DiskColor color);
    bool isFull();
    bool checkWin(int row, int col);
    void setState(const std::vector<std::tuple<int, int, DiskColor>>& cells);   // for testing
};
