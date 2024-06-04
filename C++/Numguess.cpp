#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits> 
using namespace std;

int main() {
    cout << "Welcome to the Guess the Number Game!" << endl;
    
    while (true) {
        srand(time(0)); 
        int lower_bound = 1;
        int upper_bound = 100;
        int attempts = 0;
        int target_number = lower_bound + rand() % (upper_bound - lower_bound + 1); // Generate random number
        
        cout << "I'm thinking of a number between " << lower_bound << " and " << upper_bound << ". Can you guess it?" << endl;
        
        while (true) {
            int user_guess;
            cout << "Enter your guess: ";
            cin >> user_guess;
            attempts++;
            
            if (cin.fail()) {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Invalid input. Please enter a valid number." << endl;
                continue;
            }
            
            if (user_guess < lower_bound || user_guess > upper_bound) {
                cout << "Please enter a number between " << lower_bound << " and " << upper_bound << "." << endl;
                continue;
            } else if (user_guess == target_number) {
                cout << "Congratulations! You guessed the number " << target_number << " in " << attempts << " attempts!" << endl;
                break;
            } else if (user_guess < target_number) {
                cout << "Too low! Try again." << endl;
            } else {
                cout << "Too high! Try again." << endl;
            }
        }
        
        char play_again;
        cout << "Do you want to play again? (yes/no): ";
        cin >> play_again;
        if (tolower(play_again) != 'y') {
            cout << "Thanks for playing!" << endl;
            break;
        }
    }
    
    return 0;
}
