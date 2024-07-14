from hangman_tournament import HangmanTournament
ALL_LETTERS = list('abcdefghijklmnopqrstuvwxyz')
import random
import nltk
#make sure you nltk.download('brown') in the shell first
from nltk.corpus import brown
from nltk.corpus import wordnet
from string import punctuation

class HangmanAI():

    def __init__(self, ai_name):
        self.ai_name = ai_name

    #game state has the list of missing/completed letters,
    #and a list of all your previous guesses, inside of a list
    #do game_state[0] to get the first and game_state[1] to get the second
    #such as: ['_', '_', 't']
    #prev_guesses: ['b', 'e', 'o', 't']
    #also, it tells you how many guesses you have left
    #If you make a total of 100 guesses, you will be disqualified
    #If you make 
    def make_choice(self, game_state):
        return random.choice(ALL_LETTERS)

    #New round will get called when you receive a new word
    #Now is a good time to reset any variables you changed
    #in your class as you were trying to guess the
    #previous word
    def new_round(self, game_state):
        pass

#Example of a different AI implementation
#It simply picks letters starting from a to z
class HangmanBetterAI(HangmanAI):

    def __init__(self, ai_name):
        super(HangmanBetterAI, self).__init__(ai_name)
        self.letter_list = list('abcdefghijklmnopqrstuvwxyz')
        self.letter_current_index = 0
        

    def make_choice(self, game_state):
        #print(f"Word: {game_state[0]}")
        #print(f"Guesses: {game_state[1]}")
        #print(f"chances remaining: {game_state[2]}")
        #chosen_letter = random.choice(['a', 'n', 't', 'b', 'o'])
        chosen_letter = self.letter_list[self.letter_current_index]
        self.letter_current_index += 1
        return chosen_letter
        #print(f"My choice: {chosen_letter}")
        #return chosen_letter

    def new_round(self, game_state):
        self.letter_current_index = 0


class MyCustomAI(HangmanAI):

    def get_list(self):
        my_long_words = list(filter(lambda w: len(w) >= 7, brown.words()))

        cleaned_list = []
        for one_word in my_long_words:
            add = True
            for punctuation_mark in punctuation:
                if (punctuation_mark in one_word):
                    add = False
                    #print(f"Punctuation mark in {one_word}")
            if add == True:  
                cleaned_list.append(one_word)
        return cleaned_list
        

    def __init__(self, ai_name):
        super(MyCustomAI, self).__init__(ai_name)
        self.cleaned_list = self.get_list()

    def make_choice(self, game_state):
        correct_placement = []
        guess = len(game_state[1])


        if guess == 0:
            return 'e'

        if 'u' in game_state[0][2] and 'q' not in game_state[1]:
            return 'q'
        
        if 'q' in game_state[0][1] and 'u' not in game_state[1]:
            return 'u'

        if 'e' in game_state[0][-2:] and 'd' not in game_state[1]:
            return 'd'

        if 'i' in game_state[0][-3:] and 'n' in game_state[0][-2:] and 'g' not in game_state[1]:
            return 'g'

        for letter_index in range(len(game_state[0])):
            if game_state[0][letter_index] == '_':
                continue
            for word in self.correct_length:
                if game_state[0][letter_index] == word[letter_index]:
                    correct_placement.append(word)
        if len(correct_placement) == 0:
            correct_placement = self.correct_length
            
        choices = (list(''.join(correct_placement[0:25]).lower()))
        ordered_letters = nltk.FreqDist(choices).most_common()
        
        
        for letter in ordered_letters:
            
            chosen_letter = letter[0]
            if (chosen_letter not in game_state[1]):
                return chosen_letter
        chosen_letter = random.choice(choices)
        return chosen_letter
                    

    def new_round(self, game_state):
        self.correct_length = []
        for word in self.cleaned_list:
            if len(word) == len(game_state[0]):
                self.correct_length.append(word)
       
                

        

