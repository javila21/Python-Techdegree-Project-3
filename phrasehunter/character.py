import re

"""Stores all guess made during each game"""
previous_guesses = []
"""Stores all correct guesses to be used by Phrase"""
correct_guesses = []

class Character():
    def __init__(self, player_guess, original, was_guessed=False, new_game=False, *args, **kwargs):
        self.player_guess = player_guess
        self.original = original
        self.was_guessed = was_guessed
        """If a new game is started reset lists"""
        if new_game is True:
            previous_guesses.clear()
            correct_guesses.clear()
        if new_game is False:    
            self.guess_check(player_guess, original)
    """Checks if player guess is correct by comparing to original phrase """
    def guess_check(self, player_guess, original):
        if re.search(player_guess, self.original):
            self.was_guessed = True
            
            """Checks if the guess has been made then before if has not then add to correct_guesses list, if it has then skip"""
            if player_guess not in correct_guesses:
                correct_guesses.append(player_guess)
                print("'{}' is correct!!!".format(player_guess))
                
    """Checks  if guess has already been made if yes then output message"""      
    def new_guess_check(self, player_guess):
        if player_guess in previous_guesses:
            print("You already guessed '{}', please try again".format(player_guess))
        else:
            previous_guesses.append(player_guess)    
            