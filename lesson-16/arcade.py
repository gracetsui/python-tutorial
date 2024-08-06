import sys
from rps import rps
from guess_number import guess_number

def play_game(name='Player'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back!")
            
        playerchoice = input("\nPlease choose a game: /n1 = ROck Paper Scissors \n2 = Guess My Number \n\n Or press \"x\" to exit.")
        
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game
        
        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_number = guess_number(name)
            guess_number()
        else:
            print(f"\nSee you next time, {name}!👋👋")