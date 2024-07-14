import tkinter
import random

user_score = 0
comp_score = 0
comp_choices = ['rock', 'paper', 'scissors']
compLast = 'paper'
humanLast = 'paper'
 
tk_window = tkinter.Tk()
tk_window.geometry("400x300")
tk_window.title("Rock-Paper-Scissors Game")
 
def random_computer_choice():
    choice = ''
    if (user_score + comp_score > 20 and user_score < 2 * comp_score):
        choice = random.choice(comp_choices)
    elif (user_score + comp_score > 20 and user_score > 1.5 * comp_score):
        if(compLast == 'paper'):
            choice = random.choice(['rock', 'scissors'])
        elif(compLast == 'rock'):
            choice = random.choice(['paper', 'scissors'])
        else:
            choice = random.choice(['paper', 'rock'])
    else:
        if(humanLast == 'paper'):
            choice = random.choice(['paper', 'scissors'])
        elif(humanLast == 'rock'):
            choice = random.choice(['paper', 'rock'])
        else:
            choice = random.choice(['rock', 'scissors'])
    return choice

def determine_game_result(human_choice):
    global user_score
    global comp_score
    comp_choice = random_computer_choice()
    compLast = comp_choice
    print("Human Player Choice: " + human_choice + " and Computer Player Choice: " + comp_choice)
    if human_choice == comp_choice:
        display_winner = "Result: Tie!"
    elif human_choice == "rock" and comp_choice == "scissors":
        display_winner = "Result: Human Player Wins!"
        user_score += 1
    elif human_choice == "scissors" and comp_choice == "paper":
        display_winner = "Result: Human Player Wins!"
        user_score += 1
    elif human_choice == "paper" and comp_choice == "rock":
        display_winner = "Result: Human Player Wins!"
        user_score += 1
    else:
        display_winner = "Computer Player Wins!"
        comp_score += 1
    humanLast = human_choice
      
    display_game_result(human_choice, comp_choice, display_winner)
 
def display_game_result(human_choice, comp_choice, display_winner):
    game_result = "Human Player Choice: " + human_choice + "\nComputer Player Choice: " + comp_choice + "\n" + display_winner + "\nHuman Score: " + str(user_score) + "\nComputer Score: " + str(comp_score)
    text_area = tkinter.Text(height = 12, width = 40)
    text_area.grid(column = 0, row = 4)
    text_area.insert('1.0', game_result)

text_area = tkinter.Text(height = 12, width = 40)
text_area.grid(column = 0,row = 4)
text_area.insert('1.0', "Ready to Play!")

def rock():
    user_choice = 'rock'
    determine_game_result(user_choice)
 
button_rock = tkinter.Button(text = "Rock", command = rock)
button_rock.grid(column = 0, row = 1)

def paper():
    user_choice = 'paper'
    determine_game_result(user_choice)
 
button_paper = tkinter.Button(text = "Paper", command = paper)
button_paper.grid(column = 0, row = 2)
 
def scissors():
    user_choice = 'scissors'
    determine_game_result(user_choice)
 
button_scissors = tkinter.Button(text = "Scissors", command = scissors)
button_scissors.grid(column = 0, row = 3)
