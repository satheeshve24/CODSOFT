import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


print("Welcome to Rock-Paper-Scissors Game")

choices = {1: 'rock', 2: 'paper', 3: 'scissors'}

play_again = 'yes'
user_score = 0
computer_score = 0

while play_again.lower() == 'yes':
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

       
    user_choice_num = int(input("Enter your choice (1/2/3): "))

    if user_choice_num not in choices:
        print("Invalid choice. Please try again.")
        continue

    user_choice = choices[user_choice_num]

    computer_choice = random.choice(list(choices.values()))

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"\nYour score: {user_score}")
    print(f"Computer's score: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ")

print("Thanks for playing!")

