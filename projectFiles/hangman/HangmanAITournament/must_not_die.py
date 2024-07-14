import string
from hangman_tournament import HangmanTournament
ALL_LETTERS = list('abcdefghijklmnopqrstuvwxyz')

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

    def __init__(self, ai_name):
        super(MyCustomAI, self).__init__(ai_name)
        self.letter_list = list('abcdefghijklmnopqrstuvwxyz')
        self.useLetter = list('abcdefghijklmnopqrstuvwxyz')
        self.repeat = []
        self.record = []
    def make_choice(self, game_state):
        if len(self.useLetter)==1: return "a"
        index = random.randint(0, len(self.useLetter)-1)
        isRight=False
        isWrong = False
        bestSimWord = self.findSimWord(game_state, index)
        if not bestSimWord=="" and not self.makeBetterChoice(self, bestSimWord)=="":
            return makeBetterChoice(self, bestSimWord)
        if self.useLetter[index] in game_state[0]:
            isRight=True
            self.record.append(self.useLetter[index])
        else: isWrong=True
        if isRight:
            self.record.append(self.useLetter[index])
            self.useLetter.remove(self.useLetter[index])
            index = random.randint(0, len(self.useLetter)-1)
        else:
            self.useLetter.remove(self.useLetter[index])
            index = random.randint(0, len(self.useLetter)-1)
        chosenLet = self.useLetter[index]
        
        return chosenLet

    def findSimWord(self, game_state, index):
        count = 0
        similar = {}
        for i in range(0,len(self.repeat)):
            if self.useLetter[index] not in self.repeat[i]: return ""
            for j in range(0,len(self.record)):
                if self.record[j] in self.repeat[i]: count+=1
            similar[self.repeat[i]]=count
            count = 0
        value = max(similar, key=similar.get)
        keyList = list(similar.keys())
        valList = list(similar.values())
        return similar[valList.index(value)]
    def makeBetterChoice(self, word):
        for i in range(0, len(word)):
            for j in range(0,len(self.repeat)):
                if not word[i,i+1]==self.repeat[j]:
                    return word[i,i+1]
        return ""
    def new_round(self, game_state):
        self.useLetter = list('abcdefghijklmnopqrstuvwxyz')
        self.repeat.append(game_state[0])

#AI Setups
ai1 = HangmanAI("Basic Random")
ai2 = HangmanBetterAI("Pick letters in order")
ai3 = MyCustomAI("Hangman must not die")

#Tournament Setup
import random
#make sure you nltk.download('brown') in the shell first
from nltk.corpus import brown
from nltk.corpus import wordnet
from string import punctuation
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


