import sys
import random


def guess_number(name='Player'):
    game_count = 0
    player_wins = 0
    
    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        
        playerchoice = input(
            f"\n{name}, guess which number I'm thinking...\n 1, 2, or 3\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
          print(f"{name}, please enter 1, 2, or 3.")
          return play_guess_number
    
        computerchoice = random.choice("123")
       
        print(f"\n{name}, you chose {playerchoice}")
        print(
            f"I was thinking about the number {computerchoice}\n"
        )
       
        player = int(playerchoice)
        
        computer = int(computerchoice)
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            
            if player == computer:
                player_wins += 1
                return f"{name}, you won!🎉🎉"
            else:
                return f"Sorry {name}, you lost."
            
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\n Game count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"/nYour winning percentage: {player_wins/game_count:.2%}")
        
        print(f"\nPlay again, {name}?")
        
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
            return play_guess_number
        else:
            print(f"Thank you for playing, {name}!")
            
    return play_guess_number