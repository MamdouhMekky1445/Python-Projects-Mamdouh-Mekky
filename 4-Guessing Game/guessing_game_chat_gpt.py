import random

def get_player_guess():
    """
    Prompt the player to enter a number between 1 and 10.
    
    Returns:
        int: The number guessed by the player, guaranteed to be between 1 and 10.
    """
    while True:
        player_input = input("Pick a number between 1 and 10: ")
        try:
            player_number = int(player_input)
            if 1 <= player_number <= 10:
                return player_number
            else:
                print("Please pick a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

def play_round(pc_number):
    """
    Play a round of the guessing game where the player tries to guess the pc's number.
    
    Args:
        pc_number (int): The number chosen by the pc.
        
    Returns:
        int: The number of attempts it took the player to guess correctly.
    """
    attempts = 0
    while True:
        player_number = get_player_guess()
        attempts += 1
        if player_number == pc_number:
            print("Congratulations! You've guessed the correct number!")
            return attempts
        elif player_number < pc_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

def guessing_game():
    """
    Main function to run the guessing game. The player is greeted and the game
    continues in rounds until the player chooses to stop. The minimum number of
    attempts across all rounds is tracked and displayed.
    """
    print("Welcome to the Guessing Game!")
    min_attempts = float('inf')
    
    while True:
        pc_number = random.randint(1, 10)
        attempts = play_round(pc_number)
        
        if attempts < min_attempts:
            min_attempts = attempts
        
        print(f"It took you {attempts} attempts to guess the number.")
        print(f"The minimum number of attempts so far is {min_attempts}.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    guessing_game()
