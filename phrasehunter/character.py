import re


class Character():
    def __init__(self, player_guess, original, was_guessed=False, new_game=False, *args, **kwargs):
        self.player_guess = player_guess
        self.original = original
        self.was_guessed = was_guessed
        self.guess_check(player_guess, original)
    
    def guess_check(self, player_guess, original):
        if re.search(player_guess, self.original):
            self.was_guessed = True
            
            