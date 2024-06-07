#include <iostream>
#include <vector>

std::vector<char> board(9, ' ');

void printBoard() {
    std::cout << std::endl;
    for (int i = 0; i < 9; i += 3) {
        std::cout << "| " << board[i] << " | " << board[i + 1] << " | " << board[i + 2] << " |" << std::endl;
    }
    std::cout << std::endl;
}

void playerMove(char icon) {
    int number;
    if (icon == 'X') {
        number = 1;
    } else if (icon == 'O') {
        number = 2;
    }
    std::cout << "Your turn player " << number << std::endl;
    int choice;
    std::cin >> choice;
    choice--;
    if (board[choice] == ' ') {
        board[choice] = icon;
    } else {
        std::cout << std::endl;
        std::cout << "That space is already taken!" << std::endl;
        playerMove(icon);
    }
}

bool victory(char icon) {
    return ((board[0] == icon && board[1] == icon && board[2] == icon) ||
            (board[3] == icon && board[4] == icon && board[5] == icon) ||
            (board[6] == icon && board[7] == icon && board[8] == icon) ||
            (board[0] == icon && board[3] == icon && board[6] == icon) ||
            (board[1] == icon && board[4] == icon && board[7] == icon) ||
            (board[2] == icon && board[5] == icon && board[8] == icon) ||
            (board[0] == icon && board[4] == icon && board[8] == icon) ||
            (board[2] == icon && board[4] == icon && board[6] == icon));
}

bool draw() {
    for (char cell : board) {
        if (cell == ' ')
            return false;
    }
    return true;
}

int main() {
    bool playAgain = true;
    while (playAgain) {
        for (int i = 0; i < 9; ++i) {
            board[i] = ' '; 
        }
        while (true) {
            printBoard();
            playerMove('X');
            printBoard();
            if (victory('X')) {
                std::cout << "X wins" << std::endl;
                break;
            } else if (draw()) {
                std::cout << "Draw" << std::endl;
                break;
            }
            playerMove('O');
            if (victory('O')) {
                printBoard();
                std::cout << "O wins" << std::endl;
                break;
            } else if (draw()) {
                std::cout << "Draw" << std::endl;
                break;
            }
        }
        std::cout << "Do you want to play again? (yes/no): ";
        std::string response;
        std::cin >> response;
        if (response != "yes")
            playAgain = false;
    }
    return 0;
}
