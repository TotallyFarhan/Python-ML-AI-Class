from hangman_tournament import HangmanTournament
ALL_LETTERS = list('abcdefghijklmnopqrstuvwxyz')
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
    #len(game_state[0]) gets the length of the word
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

class Hahnburger(HangmanAI):

    def __init__(self, ai_name):
        super(Hahnburger, self).__init__(ai_name)
        #ordered by wikipedia's letter frequency list
        #https://en.wikipedia.org/wiki/Letter_frequency
        self.letter_list = list('etaoinshrdlucwmfygpbvkxjqz')

    def make_choice(self, game_state):
        #print(game_state)
        #make guesses from the list in order
        return self.letter_list[len(game_state[1])]
        

    def new_round(self, game_state):
        pass



#Tournament Setup
import random
#make sure you nltk.download('brown') in the shell first
from nltk.corpus import words




def get_new_words():
    #nltk words
    #my_long_words = list(filter(lambda w: len(w) >= 7, words.words()))
    #brown words
    my_long_words = list(filter(lambda w: len(w) >= 7, brown.words()))
    my_long_words = list(map(lambda w: w.lower(), my_long_words))

    cleaned_list = []
    for one_word in my_long_words:
        add = True
        for punctuation_mark in punctuation:
            if (punctuation_mark in one_word):
                add = False
                #print(f"Punctuation mark in {one_word}")
        if add == True:  
            cleaned_list.append(one_word)

    #print(cleaned_list)
    random.shuffle(cleaned_list)
    tournament_words = cleaned_list[0:100]
    return tournament_words

def run_tournaments(number_of_tournaments):
    print("\nNew Round Begins\n")
    for tournament in range(number_of_tournaments):
        hangman_words = get_new_words()
        hangman_tournament = HangmanTournament(hangman_ais, hangman_words, max_wrong_guesses)
        hangman_tournament.run_tournament()
        hangman_tournament.show_tournament_results()

def run_basic_tourney():
    hangman_words = get_new_words()
    print("Words Used:", hangman_words)
    
    hangman_tournament = HangmanTournament(hangman_ais, hangman_words, max_wrong_guesses)
    hangman_tournament.run_tournament()
    #Uncomment this if you want to see really detailed results of each round
    hangman_tournament.show_detailed_tournament_results()
    hangman_tournament.show_tournament_results()
    
import greg_oden
import must_not_die
import shreksophone2
#AI Setups
hangman_ais = []

hangman_ais.append(Hahnburger("HahnburgerAI"))
hangman_ais.append(greg_oden.MyCustomAI(" Greg Oden"))
hangman_ais.append(must_not_die.MyCustomAI("Hangman must not die"))
hangman_ais.append(shreksophone2.MyCustomAI("Shreksophone II"))

#Normal mode
max_wrong_guesses = 6
#Relaxed mode
#max_wrong_guesses = 12


run_basic_tourney()

#run_tournaments(2)
