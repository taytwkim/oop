#pragma once

#include "board.hpp"
#include "player.hpp"

enum class GameState {
    IN_PROGRESS,
    WON,
    DRAW
};

class Game {
private:
    Board board;
    const Player* player1;
    const Player* player2;
    const Player* currPlayer;
    GameState state;
    const Player* winner;

public:
    Game(const Player* player1, const Player* player2);
    bool makeMove(const Player* player, int col);
    const Player* getCurrentPlayer() const;
    GameState getGameState() const;
    const Player* getWinner() const;
    Board& getBoard();
};
