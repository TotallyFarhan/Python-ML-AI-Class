from hangman_tournament import HangmanTournament
ALL_LETTERS = list('abcdefghijklmnopqrstuvwxyz')
from nltk.corpus import brown

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
    LETTER_LIST = "esiarntolcdugpmhbyfvkwzxjq"
    SMALL_LIST = list(filter(lambda word: word.isalpha()and len(word) >= 7, list(map(lambda word: word.lower(),brown.words()))))

    
    def __init__(self, ai_name):
        super(MyCustomAI, self).__init__(ai_name)
        self.hangman_list = MyCustomAI.SMALL_LIST[:]
        self.letterOccurences = []
        self.previousGameState = []
        self.turn1 = True
        self.guesses = []
        self.guess = ""

    def make_choice(self, game_state):
        if(self.turn1):
            self.hangman_list = list(filter(lambda word: len(word) == len(game_state[0]), self.hangman_list))
            for x in range(26):
                times = 0
                for y in range(len(self.hangman_list)):
                    if(chr(x+97) in self.hangman_list[y]):
                        times += 1
                self.letterOccurences.append(times)

            self.guess = chr(self.letterOccurences.index(max(self.letterOccurences))+97)
            self.guesses.append(self.guess)
            self.previousGameState = game_state[0]
            self.turn1 = False
        else:
            if(self.previousGameState != game_state[0]):
               self.hangman_list = list(filter(lambda word: self.guess in word, self.hangman_list))
            else:
                self.hangman_list = list(filter(lambda word: self.guess not in word, self.hangman_list))
            for x in range(26):
                times = 0
                for y in range(len(self.hangman_list)):
                    if(chr(x+97) in self.hangman_list[y]):
                        times += 1
                self.letterOccurences[x] = times

            for x in range(len(self.guesses)):
                self.letterOccurences[ord(self.guesses[x])-97] = -1

            self.guess = chr(self.letterOccurences.index(max(self.letterOccurences))+97)
            self.guesses.append(self.guess)
            self.previousGameState = game_state[0]
            
        
        return self.guess

    def new_round(self, game_state):
        self.hangman_list = MyCustomAI.SMALL_LIST[:]
        self.letterOccurences = []
        self.previousGameState = []
        self.turn1 = True
        self.guesses = []
        self.guess = ""
        return
