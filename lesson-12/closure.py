# Closure is a function haing access to the scope of its parent
# function after the parent function has returned

# Alex: don't worry if you don't full understand the concept of closure
# I will explain tomorrow, just type it out
# additional resource: https://www.w3schools.com/python/ref_keyword_nonlocal.asp#:~:text=Definition%20and%20Usage,the%20variable%20is%20not%20local.

def parent_function(person):
    coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + "coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + "coin left.")
        else:
            print("\n" + person + " is out of coins.") # this case is zero-coin
            
    return play_game

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()