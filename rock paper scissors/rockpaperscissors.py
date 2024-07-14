import tkinter
import random

tk_window = tkinter.Tk()
tk_window.geometry("286x300")
tk_window.title("Rock Paper Scissors")

human_wins = 0
comp_wins = 0

comp_choices = ['rock', 'paper', 'scissors']

def comp_choice():
    return random.choice(comp_choices)

def rock():
    human = 'rock'
    determine_winner(human)
def paper():
    human = 'paper'
    determine_winner(human)
def scissors():
    human = 'scissors'
    determine_winner(human)

def determine_winner(human):
    global human_wins
    global comp_wins
    
    comp = comp_choice()
    print("Human Choice: " + human + " Computer Choice: " + comp)

    if human == comp:
        display_winner = "Tie"
    elif human == "scissors" and comp == "paper":
        display_winner = "Human Wins"
        human_wins += 1
    elif human == "paper" and comp == "rock":
        display_winner = "Human Wins"
        human_wins += 1
    elif human == "rock" and comp == "scissors":
        display_winner = "Human Wins"
        human_wins += 1
    else:
        display_winner = "Computer Wins"
        comp_wins += 1

    if human == 'rock':
        comp_choices.append("paper")
    elif human == 'paper':
        comp_choices.append("scissors")
    else:
        comp_choices.append("rock")
        
    display_game_winner(human, comp, display_winner)

def display_game_winner(human, comp, display_winner):
    game_result = "Human Choice: " + human + "\nComputer Choice: " + comp + "\n" + display_winner + "\n Human Score: " + str(human_wins) + "\n Computer Score: " + str(comp_wins) 
    text_area = tkinter.Text(height = 12, width = 40)
    text_area.grid(column = 0, row = 4)
    text_area.insert('1.0', game_result)

button_rock = tkinter.Button(text = "Rock", command = rock)
button_rock.grid(column = 0, row = 1)

button_paper = tkinter.Button(text = "Paper", command = paper)
button_paper.grid(column = 0, row = 2)

button_scissors = tkinter.Button(text = "Scissors", command = scissors)
button_scissors.grid(column = 0, row = 3)

text_area = tkinter.Text(height = 12, width = 40)
text_area.grid(column = 0, row = 4)
text_area.insert('1.0', "Play the Game")


input("Press enter to exit;")

