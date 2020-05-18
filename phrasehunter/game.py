# Create your Game class logic in here.
import os 
import random
import sys
from phrase import Phrase
from phrase import consol_output
from character import Character

phrase_list = ['keep your chin up', 'wild at heart', 'hello world', 'embrace the journey', 'be the change', 'focus and win', 'do it now', 'never give up']
total_lives = 5
random.shuffle(phrase_list)
class Game():
    
    def __init__(self, whole_phrase=False,*args, **kwargs): 
        self.consol_output = consol_output
        self.phrase = phrase_list[1]
        self.player_guess = None
        self.welcome_message()
        self.start_game()
        
    
    
    def start_game(self):
        Phrase(phrase_list[1],self.player_guess, new_game=False, run_extend=True).charac_in_phrase()
        random.shuffle(phrase_list)
        used_lives = total_lives
        while True:
            
            self.phrase_output(self.phrase)
            if "_" not in self.consol_output:
                self.you_won()   
            self.guess_input()
            true_guess = Character(self.player_guess, self.phrase, life_check=True)
            if true_guess.was_guessed is False:
                used_lives -= 1
            if used_lives <= 0 :
                self.better_luck()
            print('You have {} out of {} lives remaining!'.format(used_lives,       total_lives))
        
    def welcome_message(self):
        print("Welcome to Phrase Hunter!")
        print("-----------------------------") 
        print("You get 5 lives, to guess the phrase.""\n""For each incorrect guess 1 life is lost. Good Luck!!!""\n")
    
    def phrase_output(self, phrase):
        self.phrase = phrase
        Phrase(phrase, self.player_guess, run_extend=False).charac_in_phrase()
        print('{}'.format(''.join(self.consol_output)))
        
    def guess_input(self):
        try:
            self.player_guess = input('Guess a letter: ')
            Character(self.player_guess, self.phrase, life_check=False)
        except ValueError: 
            print("That was not a valid input. Please pick a number between 1 and 10")
        if self.player_guess == "":
            print ("Please enter a letter,try again.")
        if not self.player_guess.isalpha(): 
            print ("Please only enter a letters,try again.")
        if len(self.player_guess) > 1:
            print("Please enter only one letter at a time.")
        
    def you_won(self):
        print("Congratualtions you won the Game!!!!")
        self.end_of_game()
        
    def better_luck(self):
        print("Better luck next time.")
        self.end_of_game()
        
    def end_of_game(self):
        try:
            play_again = input("Would you like to play again?[y]es/[n]o: ")
        except ValueError:
            print("That is is not a valid value please use either y or n.")
            self.end_of_game()
        if play_again == "y":
            Phrase(phrase_list[1], self.player_guess, new_game=True, run_extend=True)
            Character(self.player_guess, self.phrase, life_check=True, new_game=True)
            Game()
        elif play_again == "n":    
            print("\n""Thank you for playing, see y'all next time.""\n")
            sys.exit()
        else:
            print("That is is not a valid value please use either y or n.")
            self.end_of_game()
        
#Create the Game class in the game.py file
#The class should include an initializer or def __init__ method that receives a phrases parameter and holds these phrases in an instance attribute on the game object.

#You will need at least 1 instance attribute to start the game:

#An instance attribute that stores the current Phrase object and starts the game. You may think of this as the Active phrase being guessed against by the player while the game is running.
#The Game instance might be responsible for things like: starting the game loop, getting player's input() guesses to pass to a Phrase object to perform its responsibilities against, determining if a win/loss happens after the player runs out of turns or the phrase is completely guessed.