import random

HANGMANPICS = ['''



 +---+

 |   |

     |

     |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

     |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

 |   |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

/|   |

     |

     |

  =========''', '''



 +---+

 |   |

 O   |

/|\  |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

/|\  |

/    |

     |

=========''', '''



 +---+

 |   |

 O   |

/|\  |

/ \  |

     |

=========''']

words = 'ant badger bat bear deer dog'.split()

def get_random_word(word_list):
  return random.choice(word_list)

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
  print(hangman_pics[len(missed_letters)])
  print()
  
  print('Missed letters:', end = ' ')

  for letter in missed_letters:
    print(letter, end = ' ')
  print()
  print()

  blanks = '_' * len(secret_word)

  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

  print('Secret Word:', end = ' ')

  for letter in blanks:
    print(letter, end = ' ')
  print()
  print()

def get_guess(already_guessed):
  while True:
    print('Guess a letter:', end = ' ')
    guess = input()
    guess = guess.lower()

    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in already_guessed:
      print('You have already guessed that letter. Please choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print('Please enter a letter.')
    else:
      return guess

def playAgain():
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

print('HANGMAN')
 
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
  display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
  
  guess = get_guess(missed_letters + correct_letters)

  if guess in secret_word:
    correct_letters = correct_letters + guess

    found_all_letters = True
    for letter in secret_word:
      if letter not in correct_letters:
        found_all_letters = False
        break
    if found_all_letters:
      print('You have won!!! The secret word is ' + secret_word)
      game_is_done = True
  else:
    missed_letters = missed_letters + guess

    if len(missed_letters) == len(HANGMANPICS) - 1:
      display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
      print('You have run out of guesses and lose! The secret word was: ' + secret_word)
      game_is_done = True

  if game_is_done:
    if playAgain():
      missed_letters = ''
      correct_letters = ''
      game_is_done = False
      secret_word = get_random_word(words)
    else:
      break