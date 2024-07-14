import rpstournament
import random

#Your class must be called GamePlayer, and it must have these functions
class GamePlayer:
    #Give your AI a name. You can put your name in it or not, depending on whether you want to be anonymous.
    #You can submit multiple AI's with different names for the tournament
    name = 'Dwayne "The Rock" Johnson'

    def __init__(self):
        self.my_choice_list = []
        self.opponent_choice_list = []
        self.valid_rounds = 0
        self.rounds = 0
        self.go_random = False

    def make_choice(self):
        #This function must return 1 of 3 values, 'rock', 'paper', or 'scissors'
        #If it returns anything else, your AI will forfeit the match

        if (self.go_random == True):
            choice = random.choice(['rock', 'paper', 'scissors'])
            self.my_choice_list.append(choice)
            return choice
        else:
            choice = 'rock'
            self.my_choice_list.append(choice)
            return(choice)

    def count_rounds(self):
        #Counts total rounds and valid rounds, rounds where someone won

        if (self.my_choice_list[self.rounds] != self.opponent_choice_list[self.rounds]):
            self.valid_rounds += 1
            self.rounds += 1
        else:
            self.rounds += 1

    def calculate_score(self, my_choices, opponent_choices):
        # the slow lazy way :D
        score = []
        if (len(my_choices) == len(opponent_choices)):
            for i in range(len(my_choices)):
                if (my_choices[i] == 'rock' and opponent_choices[i] == 'scissors'):
                    score.append(True)
                elif (my_choices[i] == 'paper' and opponent_choices[i] == 'rock'):
                    score.append(True)
                elif (my_choices[i] == 'scissors' and opponent_choices[i] == 'paper'):
                    score.append(True)
                else:
                    score.append(False)
            wins = score.count(True)
            losses = score.count(False)
            total = wins + losses
            ratio = round(wins/total, 3)
            return (ratio)
        return
            
    def view_opponent_choice(self, opponent_choice):
        #This function doesn't have to do anything
        #You will be shown your opponent's choice from last round
        #One of 'rock', 'paper', or 'scissors'
        #You are not allowed to access win and loss records from the Tournament code
        #If you want to track your win and loss rate, you will need to compare
        #Your choice to your opponent's choice here.

        self.opponent_choice_list.append(opponent_choice) #Save opponent choice
        self.count_rounds() #count rounds

        #Analyze 50 rounds
        if (self.valid_rounds == 49):
            score = self.calculate_score(self.my_choice_list, self.opponent_choice_list)
            if (score < 0.9):
                self.go_random = True
                return
            
            
        return

    def new_player(self):
        #This function doesn't have to do anything
        #This will be called when you face a new opponent in a new match
        #You might want to use this method to reset your AI's strategy

        self.my_choice_list = []
        self.opponent_choice_list = []
        self.valid_rounds = 0
        self.rounds = 0
        self.go_random = False
        return

tournament_manager = rpstournament.TournamentManager()
example_game_player = GamePlayer()
tournament_manager.run_tournament(example_game_player)
