#-----------------PseudoCode--------------------#
# Start the game
# Ask the player to make a move (r, p, s)
# PC would select a move radomly
# PC == Player -> Tie
# (Player == P and PC == Rock) or (Player == R and PC == Scissors) or (Player == Scissors and PC == Paper)
## User won / You won
# Any other case
## PC won / You lose
#----------------------------------------------#

#------libraries-----------#
import random

#------------Start the game---------------------------#

#------------Ask the player to make a move (r, p, s)------------------------#

print('Welcom to our Rock Paper Scissors Game')

gamer_move = input("Please choose your move and enter r for (rock)  or p for (paper)  or s for (scissors)\n")

print(f"You choosed ({gamer_move})")


choices = ['r', 'p', 's']
computer_choice = random.choice(choices)

print(f"Computer choosed ({computer_choice})")


if(gamer_move == computer_choice):
    print("mmm! It is a tie")
elif( (gamer_move == 'r' and computer_choice == 's') or (gamer_move == 'p' and computer_choice == 'r') or (gamer_move == 's' and computer_choice == 'p') ):
    print("Yaaaaah! You won the game")
else:
    print("Unfortunately! You lost")






#------------After Refactoring ---------------------------#


# import random

# def get_user_choice():
#     """Ask the player to make a move and return it."""
#     while True:
#         gamer_move = input("Please choose your move: 'r' for rock, 'p' for paper, or 's' for scissors: ")
#         if gamer_move in ['r', 'p', 's']:
#             return gamer_move
#         else:
#             print("Invalid choice. Please try again.")

# def get_computer_choice():
#     """Generate a random move for the computer and return it."""
#     return random.choice(['r', 'p', 's'])

# def determine_winner(player, computer):
#     """
#     Determine the winner of the game based on player and computer moves.

#     Args:
#     - player: The player's move ('r', 'p', or 's').
#     - computer: The computer's move ('r', 'p', or 's').

#     Returns:
#     - "tie" if it's a tie, "player" if the player wins, "computer" if the computer wins.
#     """
#     if player == computer:
#         return "tie"
#     elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
#         return "player"
#     else:
#         return "computer"

# def play_game():
#     """Start the Rock, Paper, Scissors game."""
#     print("Welcome to Rock, Paper, Scissors!")
#     while True:
#         player_move = get_user_choice()
#         computer_move = get_computer_choice()
#         print(f"You chose {player_move}. Computer chose {computer_move}.")
#         winner = determine_winner(player_move, computer_move)
#         if winner == "tie":
#             print("It's a tie!")
#         elif winner == "player":
#             print("Congratulations! You won the game.")
#         else:
#             print("Sorry, you lost. Better luck next time.")
#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != "yes":
#             break
#     print("Thank you for playing!")

# # Start the game
# play_game()

