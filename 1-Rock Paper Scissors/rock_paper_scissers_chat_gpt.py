import random

def get_user_choice():
    """Get the user's choice for Rock, Paper, Scissors."""
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game.

    Args:
    - user_choice: The user's choice (string).
    - computer_choice: The computer's choice (string).

    Returns:
    - "user" if the user wins, "computer" if the computer wins, or "tie" if it's a tie.
    """
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    """Play a game of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    ties = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
            ties += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}, Ties: {ties}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

play_game()
