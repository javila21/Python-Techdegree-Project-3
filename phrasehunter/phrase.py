import re
import copy
from character import Character
from character import correct_guesses

"""A list of the phrase where each character is a string"""
character_list = []
"""The phrase that the player sees"""
consol_output = []

class Phrase():
    def __init__(self,phrase, player_guess, new_game=False, run_extend=True, *args, **kwargs):
        self.phrase = phrase
        self.new_game = new_game
        self.run_extend = run_extend
        self.correct_guesses = correct_guesses
        self.player_guess=player_guess
        """If a 2nd game or any game after that is played lists are cleared"""
        if new_game is True:
            character_list.clear()
            consol_output.clear()
        print(self.phrase)
    """Turns the phrase into a list characters"""           
    def charac_in_phrase(self):
        character_list = list(self.phrase)
        self.consol_output(character_list)
        
    """Generates the initial output to be displayed to player"""   
    def consol_output(self, character_list):
        if self.run_extend is True:
            consol_output.extend(copy.deepcopy(character_list)) 
            for n, char in enumerate(consol_output):
                if char != " ":
                    consol_output[n] = "_"
        """adds corrects guesses to display output"""            
        for n, char in enumerate(character_list):
            if char is self.player_guess:
                consol_output[n] = self.player_guess
                