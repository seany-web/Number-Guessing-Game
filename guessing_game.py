import random


def start_game():
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
        if int(guess) > 10 or int(guess) < 1:
          attempts += 1
          print(f'{guess} is not in the range of 1 - 10. Please enter a number between 1 and 10.\n')
        elif int(guess) > solution:
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
              print(f"'{play_again}' is not a recognised value. Please enter 'yes' or 'no'.\n") 
      except:
        print(f"'{guess}' is not a recongnised value. Please enter a number between 1 and 10.\n")  
        #game logic ends here
    #end of game loop


start_game()