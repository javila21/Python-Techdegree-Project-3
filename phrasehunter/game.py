import sys
from phrase import Phrase
from phrase import consol_output
from character import Character

class Game():
    
    def __init__(self,total_lives = 5, *args, **kwargs): 
        self.total_lives = total_lives
        self.consol_output = consol_output
        """Sets the phrase for the games"""
        self.player_guess = None
        phrase = Phrase(self.player_guess)
        self.phrase = phrase.phrases
#        print(phrase_list[1])
        self.welcome_message()
        self.start_game()
        
    
    """Starts Game"""
    def start_game(self):

        """Sets the number of guesses"""
        used_lives = self.total_lives
        """Game loop"""
        while True:
            
            self.phrase_output(self.phrase)
            """If no "_" in output then game is won"""
            if "_" not in self.consol_output:
                self.you_won()   
            self.guess_input()
            """Checks if guess input matches phrase in Character file and then counts down if not correct
"""
            true_guess = Character(self.player_guess, self.phrase)
            if true_guess.was_guessed is False:
                used_lives -= 1
                """If all 5 lives are used then end game"""
            if used_lives <= 0 :
                self.better_luck()
                """Output how many lives are left"""
            print('You have {} out of {} lives remaining!'.format(used_lives,self.total_lives))
    """Welcome message Method"""    
    def welcome_message(self):
        print("Welcome to Phrase Hunter!")
        print("-----------------------------") 
        print("You get 5 lives, to guess the phrase.""\n""For each incorrect guess 1 life is lost. Good Luck!!!""\n")
        
    """Output the phrase to be guessed against and adds correct guess to output"""
    def phrase_output(self, phrase):
        self.phrase = phrase
        Phrase(self.player_guess, run_extend=False)
        print('{}'.format(''.join(self.consol_output)))
        
    """Input request for player with expections"""    
    def guess_input(self):
        try:
            self.player_guess = input('Guess a letter: ').lower()
            Character(self.player_guess, self.phrase)
        except ValueError: 
            print("That was not a valid input. Please pick a number between 1 and 10")
        if self.player_guess == "":
            print ("Please enter a letter,try again.")
        if not self.player_guess.isalpha(): 
            print ("Please only enter a letter(a-z),try again.")
        if len(self.player_guess) > 1:
            print("Please enter only one letter at a time.")
            
    """Winning Message"""    
    def you_won(self):
        print("Congratualtions you won the Game!!!!")
        self.end_of_game()
        
    """Losing Message"""    
    def better_luck(self):
        print("Better luck next time.")
        self.end_of_game()
        
    """End of Game Method with option to exit or play again"""    
    def end_of_game(self):
        try:
            play_again = input("Would you like to play again?[y]es/[n]o: ").lower()
        except ValueError:
            print("That is is not a valid value please use either y or n.")
            self.end_of_game()
        if play_again == "y":
            Phrase(self.player_guess, new_game=True, run_extend=True)
            Character(self.player_guess, self.phrase, life_check=True, new_game=True)
            Game()
        elif play_again == "n":    
            print("\n""Thank you for playing, see y'all next time.""\n")
            sys.exit()
        else:
            print("That is is not a valid value please use either y or n.")
            self.end_of_game()
        