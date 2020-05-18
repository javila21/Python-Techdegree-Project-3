# Create your Phrase class logic here.
import re
import copy
from character import Character
from character import correct_guesses

character_list = []
consol_output = []

class Phrase():
    def __init__(self,phrase, player_guess, new_game=False, run_extend=True, *args, **kwargs):
        self.phrase = phrase
        self.new_game = new_game
        self.run_extend = run_extend
        self.correct_guesses = correct_guesses
        self.player_guess=player_guess
        if new_game is True:
            character_list.clear()
            consol_output.clear()
        print(self.phrase)
               
    def charac_in_phrase(self):
        character_list = list(self.phrase)
#        print(character_list)
        self.consol_output(character_list)
        
    def consol_output(self, character_list):
#        print(self.run_extend)
        if self.run_extend is True:
            consol_output.extend(copy.deepcopy(character_list)) 
            for n, char in enumerate(consol_output):
                if char != " ":
                    consol_output[n] = "_"
                    
        for n, char in enumerate(character_list):
            if char is self.player_guess:
                consol_output[n] = self.player_guess
        
                
#Create the Phrase class in the phrase.py file
#The class should include an initializer or def __init__ that receives a phrase parameter and holds this phrase in an instance attribute on the Phrase object. A phrase should be a collection of Character objects, where each letter of the phrase is a Character() instance stored inside a collection such as a List.

#Any additional instance attributes you feel you need to store are up to you.

#The Phrase instance might be responsible for things like: Knowing if the entire phrase has been guessed, Iterating over its collection of Character to allow a guess to be checked using a Character instance method call or to ask the Character object how it should show its letter.

#The instance method names and their implementation are up to you to determine.