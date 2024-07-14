from tkinter import *
import random

USER_SCORE = 0
COMP_SCORE = 0
COMP_CHOICES = ['rock', 'paper', 'scissors']

tk_window = Tk()
tk_window.geometry("400x300")
tk_window.title("Rock-Paper-Scissors Game")
		
def random_computer_choice():
    global COMP_CHOICES
    return random.choice(COMP_CHOICES)

def result(human_choice):
    global USER_SCORE
    global COMP_SCORE  
    comp_choice=random_computer_choice()
    print("Human Player Choice: " + human_choice + " and Computer Player Choice: " + comp_choice)
    if(human_choice==comp_choice):
        winner = "Result: Tie!"
    elif(human_choice=="rock" and comp_choice=="scissors"):
        winner = "Result: Human Player Wins!"
        USER_SCORE += 1
    elif(human_choice=="scissors" and comp_choice=="paper"):
        winner = "Result: Human Player Wins!"
        USER_SCORE += 1
    elif(human_choice=="paper" and comp_choice=="rock"):
        winner = "Result: Human Player Wins!"
        USER_SCORE += 1
    else:
        winner = "Computer Player Wins!"
        COMP_SCORE += 1
    text_area = Text(height=12, width=40)
    text_area.grid(column=0,row=4)
    game_result = "Human Player Choice: " + human_choice + "\nComputer Player Choice: " + comp_choice + "\n" + winner + "\nHuman Score: " + str(USER_SCORE) + "\nComputer Score: " + str(COMP_SCORE)
    text_area.insert(END, game_result)
    global COMP_CHOICES
    if (human_choice == 'rock'):
        COMP_CHOICES.append('paper')
    elif (human_choice == 'paper'):
        COMP_CHOICES.append('scissors')
    else:
        COMP_CHOICES.append('rock')
				  
def rock():
    user_choice='rock'
    result(user_choice)

button_rock = Button(text="Rock",command=rock)
button_rock.grid(column=0,row=1)

def paper():
    user_choice='paper'
    result(user_choice)

button_paper = Button(text="Paper",command=paper)
button_paper.grid(column=0,row=2)
    
def scissors():
    user_choice='scissors'
    result(user_choice)

button_scissors = Button(text="Scissors",command=scissors)
button_scissors.grid(column=0,row=3)
