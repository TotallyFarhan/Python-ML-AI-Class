import tkinter
from tkinter import *
import random

tk_window = tkinter.Tk()
tk_window.geometry("900x600")
tk_window.title("Rock-Paper-Scissors Game")
human_choices = []
sequence_tracker = [' ',' ',' ']

sequences_rock = [
        ['scissors', 'paper', 'rock']
    ]

sequences_paper = [
        ['rock', 'paper', 'scissors']
    ]

sequences_scissors = [
        ['paper', 'scissors', 'rock']
    ]

sequence_tracker_index = 0

def verify_if_sequence_match(sequence_testing, sequence_tracker) :
    index = 0
    matches_counter = 0
    for i in sequence_testing :
        if (i == sequence_tracker[index]) :
            matches_counter += 1
        index  += 1
    return matches_counter >= 3
    
def computer_choice() :
    global counter_choices
    global sequence_tracker
    global sequence_tracker_index

    print(human_choices)
    
    for i in range(len(sequences_rock)):
        if(verify_if_sequence_match(sequences_rock[i], sequence_tracker)) :
            return 'rock'
    for i in range(len(sequences_paper)):
        if(verify_if_sequence_match(sequences_paper[i], sequence_tracker)) :
            return 'paper'
    for i in range(len(sequences_scissors)):
        if(verify_if_sequence_match(sequences_scissors[i], sequence_tracker)) :
            return 'scissors'

    hc = len(human_choices)
    if(hc > 1 and human_choices[hc-1] == human_choices[hc-2]) :
        if human_choices[hc-1] == 'rock':
            return 'paper'
        if human_choices[hc-1] == 'paper':
            return 'scissors'
        if human_choices[hc-1] == 'scissors':
            return 'rock'
    
    return random.choice(['rock','paper','scissors'])

wins_human_counter = 0
wins_comp_counter = 0

def determine_game_result(human_choice) :
    global wins_human_counter
    global wins_comp_counter
    global human_choices
    global sequence_tracker
    global sequence_tracker_index
    
    comp_choice = computer_choice()

    human_choices.append(human_choice)

    sequence_tracker[sequence_tracker_index] = human_choice
    sequence_tracker_index += 1
    if sequence_tracker_index > 2:
        sequence_tracker_index = 0
    #sequence_tracker_index = sequence_tracker_index % (len(sequence_tracker))

    if(human_choice == comp_choice) :
        winner = "It is a Tie!"
    elif(((human_choice == 'rock') & (comp_choice == 'scissors')) | ((human_choice == 'paper') & (comp_choice == 'rock')) | ((human_choice == 'scissors') & (comp_choice == 'paper'))) :
        winner = "Human wins"
        wins_human_counter += 1
    else :
        winner = "Computer wins"
        wins_comp_counter += 1

    display_game_result(human_choice, comp_choice, winner, wins_human_counter, wins_comp_counter)
     
def display_game_result(human_choice, comp_choice, display_winner, counter_human_wins, counter_comp_wins) :
    game_result = "Human Choice -> " + human_choice +"\nComputer Choice -> " + comp_choice + "\n\nWinner -> " + display_winner +"\n\n\nScore:\n  -> Human: " + str(counter_human_wins) + "\n  -> Computer: " + str(counter_comp_wins)
    text_area = tkinter.Text(height = 12, width = 40)
    text_area.grid(column = 0, row = 5)
    text_area.insert('1.0', game_result)

def rock() :
    user_choice = 'rock'
    determine_game_result(user_choice)
    
def paper() :
    user_choice = 'paper'
    determine_game_result(user_choice)

def scissors() :
    user_choice = 'scissors'
    determine_game_result(user_choice)

photoRock = PhotoImage(file = "img/rock.png")
photoimagerock = photoRock.subsample(40, 45)
button_rock = tkinter.Button(text = "Rock", command = rock, image = photoimagerock)
button_rock.grid(column = 1, row = 0)


photoPaper = PhotoImage(file = "img/paper.png")
photoimagepaper = photoPaper.subsample(12, 18)
button_paper = tkinter.Button(text = "Paper", command = paper, image = photoimagepaper)
button_paper.grid(column = 2, row = 0)

photoScissors = PhotoImage(file = "img/scissors.png")
photoimagescissors = photoScissors.subsample(23, 17)
button_scissors = tkinter.Button(text = "Scissors", command = scissors, image = photoimagescissors)
button_scissors.grid(column = 3, row = 0)

text_area = tkinter.Text(height = 12, width = 40)
text_area.grid(column = 0, row = 5)
text_area.insert('1.0', "Let's play!")

