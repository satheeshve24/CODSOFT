import java.util.Scanner;
import java.util.Random;

public class numguess {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        boolean playAgain = true;

        System.out.println("Welcome to the Guess the Number game!");

        while (playAgain) {
            int attempts = 0;
            int targetNumber = random.nextInt(100) + 1;
            while (true) {
                System.out.print("Enter your guess (between 1 and 100): ");
                int userGuess = scanner.nextInt();
                attempts++;

                if (userGuess == targetNumber) {
                    System.out.println("Congratulations! You've guessed the number " + targetNumber + " correctly in " + attempts + " attempts!");
                    break;
                } else if (userGuess < targetNumber) {
                    System.out.println("Too low! Try guessing a higher number.");
                } else {
                    System.out.println("Too high! Try guessing a lower number.");
                }

                if (attempts == 10) {
                    System.out.println("Oops, you've reached the maximum number of attempts. The correct number was " + targetNumber + ".");
                    break;
                }
            }

            System.out.print("Do you want to play again? (yes/no): ");
            String playAgainInput = scanner.next();
            if (!playAgainInput.equalsIgnoreCase("yes")) {
                playAgain = false;
                System.out.println("Thanks for playing!");
            } else {
                System.out.println("\nStarting a new round...\n");
            }
        }
        scanner.close();
    }
}
