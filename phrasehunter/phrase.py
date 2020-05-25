import re
import copy
from character import Character

"""A list of the phrase where each character is a string"""
character_list = []
"""The phrase that the player sees"""
consol_output = []

class Phrase():
    def __init__(self,phrase, player_guess, new_game=False, run_extend=True, *args, **kwargs):
        self.phrase = phrase
        self.phrase = []
        for char in self.phrase:
            self.phrase.append(Character(char, phrase)) 
        self.new_game = new_game
        self.run_extend = run_extend
        self.player_guess = player_guess
        self.consol_output(phrase)
        """
        If a 2nd game or any game after that is played lists are cleared and 
        List is of phrases is shuffled 
        """
        if new_game is True:
            character_list.clear()
            consol_output.clear()
            random.shuffle(phrase_list)
    
    def consol_output(self, character_list):
        """Generates the initial output to be displayed to player"""
        if self.run_extend is True:
            consol_output.extend(copy.deepcopy(character_list)) 
            for n, char in enumerate(consol_output):
                if char != " ":
                    consol_output[n] = "_"
        """adds corrects guesses to display output"""            
        for n, char in enumerate(character_list):
            if char == self.player_guess:
                consol_output[n] = self.player_guess
                