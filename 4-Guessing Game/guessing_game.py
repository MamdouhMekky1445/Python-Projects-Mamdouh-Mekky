import random

attempt_list = []
no_of_attempts = 0
rand_num = random.randint(1, 10)

def show_number_of_attempts():
    if not attempt_list:
        print('There is currently no high score, you can start playing now.')
    else:
        print(f"The current high score is {min(attempt_list)} attempts.")

print('Hello! Welcome to our guessing game.')
player_name = input('What is your name? ')

wanna_play = input(f"Would you like to play our guessing game, {player_name}? Choose Yes/No: ").strip().lower()

if wanna_play == 'yes':
    print('WOW! COOL Thank you')
    
    while wanna_play == 'yes':
        try:
            guess = int(input('Please enter a number between 1 and 10: '))
            if guess > 10 or guess < 1:
                raise ValueError("Please enter a number within the range (1 - 10)")

            no_of_attempts += 1

            if guess == rand_num:
                print(f"Congratulations {player_name}! You've guessed the right number {rand_num} in {no_of_attempts} attempts.")
                attempt_list.append(no_of_attempts)
                wanna_play = input(f'Would you like to play again, {player_name}? Choose Yes/No: ').strip().lower()
                if wanna_play == 'yes':
                    no_of_attempts = 0
                    rand_num = random.randint(1, 10)
                    show_number_of_attempts()
                else:
                    print('That is cool! Have a good day')
                    break
            elif guess > rand_num:
                print('You should try lower.')
            else:
                print('You should try higher.')
        except ValueError as err:
            print(err)
            
show_number_of_attempts()
print("Thanks for being with us!")

