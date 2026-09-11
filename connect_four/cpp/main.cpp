#include <iostream>
#include "game.hpp"

int main() {
    Player player1("alice", DiskColor::RED);
    Player player2("bob", DiskColor::YELLOW);
    Game game(&player1, &player2);

    game.makeMove(&player1, 0);
    game.makeMove(&player2, 0);

    game.makeMove(&player1, 1);
    game.makeMove(&player2, 1);

    game.makeMove(&player1, 2);
    game.makeMove(&player2, 2);

    game.makeMove(&player1, 3);
    bool accepted = game.makeMove(&player2, 3);

    std::cout << "Move after game over accepted: " << std::boolalpha << accepted << '\n';

    std::cout << static_cast<int>(game.getGameState()) << std::endl;
    
    if (const Player* winner = game.getWinner()) {
        std::cout << winner->getName() << '\n';
    }

    return 0;
}
