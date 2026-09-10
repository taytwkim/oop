#pragma once

#include "board.hpp"
#include "player.hpp"

enum GameState {
    IN_PROGRESS,
    WON,
    DRAW
};

class Game {
private:
    Board board;
    // Non-owning pointers: players must outlive the game.
    const Player* player1;
    const Player* player2;
    const Player* currPlayer;
    GameState state;
    const Player* winner;

public:
    Game(const Player* player1, const Player* player2);
    bool makeMove(const Player* player, int col);
    const Player* getCurrentPlayer();
    GameState getGameState();
    const Player* getWinner();
    Board& getBoard();
};
