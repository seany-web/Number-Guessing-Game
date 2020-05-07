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
    # print welcome message when a player starts the application
    print('?????????????????????????????????????????????????????\n\n')
    print('         WELCOME TO THE NUMBER GUESSING GAME\n\n')
    print('?????????????????????????????????????????????????????\n\n')

    #set variables to hold the highscore, number of attempts the randomly generated solution number and start the game loop
    high_score = None
    attempts = 0
    solution = random.randrange(1,10)
    game_started = True #used to confirm is game state is active is set to false at the end of the game and only enabled if player plays again
    #print(solution) #used for testing 
    
    #game loop starts here
    while(game_started): 
      try:
        #prompt the player to guess a number between 1 and 10
        guess = input("I'm thinking of a number between 1 and 10... ")
        #game logic starts here
        if int(guess) > solution:
          attempts += 1
          print(f'The number I am thinking of is lower than {guess}\n')
        elif int(guess) < solution:
          attempts += 1
          print(f'The number I am thinking of is higher than {guess}\n')
        elif int(guess) == solution:
          attempts += 1
          game_started = False
          if high_score == None or high_score > attempts:
            high_score = attempts
          print(f"\nThat's it! You answered correctly in {attempts} attempts.\n")
          #repeatedly prompt player to play again until either 'yes' or 'no' are selected
          while(True):
            play_again = input('Would you like to play again? yes/no... ')
            if play_again.upper() == 'YES':
              #reset game variables
              game_started = True
              attempts = 0
              solution = random.randrange(1,10)
              #print(solution) # used for testing
              print(f'\nThe current highscore is {high_score}. Can you beat it?\n')
              break
            elif play_again.upper() == 'NO':
              print('Thanks for playing! See you next time.\n')
              print('Exiting game.\n')
              break
            else:
              print('That is not a recognised value. Please try again\n') 
      except:
        print('That is not a recognised value. Please try again\n')  
        #game logic ends here
    #end of game loop

# Kick off the program by calling the start_game function.
start_game()