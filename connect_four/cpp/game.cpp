#include "game.hpp"
#include <stdexcept>

Game::Game(const Player* player1, const Player* player2)
    : board(6, 7),
      player1(player1),
      player2(player2),
      currPlayer(player1),
      state(IN_PROGRESS),
      winner(nullptr)
{
    if (player1 == nullptr || player2 == nullptr || player1 == player2) {
        throw std::invalid_argument("Two distinct, non-null players are required");
    }
}

bool Game::makeMove(const Player* player, int col) {
    if (state != IN_PROGRESS) {
        return false;
    }

    if (player != currPlayer) {
        return false;
    }

    int row = board.placeDisk(col, currPlayer->getColor());

    if (row == -1) {
        return false;
    }

    if (board.checkWin(row, col)) {
        state = WON;
        winner = currPlayer;
    }

    else if (board.isFull()) {
        state = DRAW;
    }
    
    else {
        if (currPlayer == player1) {
            currPlayer = player2;
        }
        else {
            currPlayer = player1;
        }
    }

    return true;
}

const Player* Game::getCurrentPlayer() {
    return currPlayer;
}

GameState Game::getGameState() {
    return state;
}

const Player* Game::getWinner() {
    return winner;
}

Board& Game::getBoard() {
    return board;
}
