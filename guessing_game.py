"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print('?????????????????????????????????????????????????????\n\n')
    print('         WELCOME TO THE NUMBER GUESSING GAME\n\n')
    print('?????????????????????????????????????????????????????\n\n')

    print("I'm thinking of a number between 1 and 100\n\n")
    game_started = True

    while(True):
      solution = random.randrange(1,100)
      attempts = 0
      
      while(game_started):
        guess = int(input('\nPlease enter a number... '))
        attempts += 1
        if guess > solution:
          print('LOWER!\n')
        elif guess < solution:
          print('HIGHER!\n')
        else:
          print('YOU WIN!\n')
          print(f'Congratulations, you guessed the random number in {attempts} attempts\n')
          game_started = False
      
      
      play_again = input('Would you like to play again? yes/no: ')

      if play_again.upper() == 'NO':
        print('\nThanks for playing. See you next time!\n')
        break
      elif play_again.upper() == 'YES':
        game_started = True
      else:
        print('\nPlease try again\n')


      



# Kick off the program by calling the start_game function.
start_game()