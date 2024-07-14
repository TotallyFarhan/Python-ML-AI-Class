import random
import re
#make sure you nltk.download('brown') in the shell first
from nltk.corpus import brown
from nltk.corpus import wordnet
my_long_words = list(filter(lambda w: len(w) >= 7, brown.words()))
#tournament_words = ['ant', 'bat', 'boat']
MAX_ALL_GUESSES = 100
ALL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import time

class HangmanTournament():

    def __init__(self, ai_list, word_list, max_wrong_guesses):
        self.ai_list = ai_list
        self.word_list = word_list
        #dictionary of dictionaries
        #{name of AI: {Round: Real data}}
        self.ai_datastores = {}
        self.names_to_ais = {}
        self.max_wrong_guesses = max_wrong_guesses
        for ai in self.ai_list:
            self.names_to_ais[ai.ai_name] = ai

    def run_tournament(self):
        #For each AI:
        #Run a round and record the
        for ai in self.ai_list:
            print(f"Testing AI:{ai.ai_name}...")
            start_time = time.time()
            ai_datastore = {}
            self.ai_datastores[ai.ai_name] = ai_datastore
            for word in self.word_list:
                self.run_round(ai, word, ai_datastore)
            print(f"AI Time taken: {round(time.time() - start_time, 5)} Seconds")

    def show_tournament_results(self, detailed = False):
        for ai_datastore_name in self.ai_datastores.keys():
            words_guessed = []
            words_failed = []
            print(f"AI: {ai_datastore_name}")
            ai_datastore = self.ai_datastores[ai_datastore_name]
            for round_number in ai_datastore.keys():
                if ai_datastore[round_number][2] == True:
                    words_guessed.append(ai_datastore[round_number][0])
                else:
                    words_failed.append(ai_datastore[round_number][0])
                if detailed:
                    print(f"Round Number: {round_number}")
                    print(f"Secret word: {ai_datastore[round_number][0]}")
                    print(f"End Display: {''.join(self.get_word_display(ai_datastore[round_number][1], ai_datastore[round_number][0]))}")
                    print(f"AI Guesses: {ai_datastore[round_number][1]}")
                    print(f"Result(True for win, false for fail): {ai_datastore[round_number][2]}")
                    print()
            print(f"Words Identified: {len(words_guessed)} out of {len(words_guessed) + len(words_failed)}")
            print("")
            

    def show_detailed_tournament_results(self):
        self.show_tournament_results(True)
        
                                        
            
            

    #Runs one round where an AI tries to guess for a word
    #the datastore holds information about how well the AI performed
    #That gets printed out at the end
    def run_round(self, ai, word, ai_datastore):
        all_guesses_list = []
        word_display = []
        correct_letters = []
        current_round = len(ai_datastore)
        won_round = False
        word_display = list(map(lambda letter: letter if letter in correct_letters else '_', word))
        wrong_guesses_remaining = self.max_wrong_guesses
        game_state = [word_display, all_guesses_list, wrong_guesses_remaining]
        ai.new_round(game_state)
        
        while len(all_guesses_list) <= MAX_ALL_GUESSES:
        #If the AI guesses 100 times, it's an automatic lose.
            
            chosen_letter = ai.make_choice(game_state)
            disqualification_check_result = self.disqualification_check(chosen_letter)
            if (disqualification_check_result):
                won_round = False
                #print("Disqualified")
                break
            all_guesses_list.append(chosen_letter)
            if chosen_letter in word and chosen_letter not in correct_letters:
                correct_letters.append(chosen_letter)
            word_display = list(map(lambda letter: letter if letter in correct_letters else '_', word))
            if (chosen_letter not in word):
                wrong_guesses_remaining = wrong_guesses_remaining - 1
            if (wrong_guesses_remaining < 0):
                won_round = False
                #print("Out of guesses")
                break
            if '_' not in word_display:
                won_round = True
                break
            
            game_state = [word_display, all_guesses_list, wrong_guesses_remaining]
        #end of all this, store info back to the datastore, which is a dictionary        

        ai_datastore[current_round] = [word, all_guesses_list, won_round]

    def get_word_display(self, all_guesses, secret_word):
        return list(map(lambda letter: letter if letter in all_guesses else '_', secret_word))

    def disqualification_check(self, letter):
        if letter == None:
            print(f"Disqualified: Failed to make a choice")
            return True
        if len(letter) != 1:
            print(f"Disqualified: {letter} is more than one character")
            return True
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print(f"Disqualified: {letter} is not a letter")
            return True
        else:
            return False







print('Hangman Tournament Begins')

#hangman_ais = [HangmanAI("Name1"), HangmanBetterAI("Name2")]
#hangman_words = tournament_words
#hangman_tournament = HangmanTournament(hangman_ais, hangman_words)
#hangman_tournament.run_tournament()
#hangman_tournament.show_tournament_results()
