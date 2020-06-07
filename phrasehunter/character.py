import re


class Character():
    def __init__(self, player_guess, original, was_guessed=False, new_game=False, *args, **kwargs):
        self.player_guess = player_guess
        self.original = str(original)
        self.was_guessed = was_guessed
        if new_game is False:
            self.guess_check(player_guess, original)

    def __str__(self):
        return "{}".format(self.original)

    def guess_check(self, player_guess, original):
        """Checks if player input is a match"""
        if re.search(player_guess, self.original):
            self.was_guessed = True
