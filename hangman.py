import random
import nltk
nltk.download('words')

from nltk.corpus import words

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

words = words.words()

def get_random_word(word_list):
    return random.choice(word_list)

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()
    print('Missed letters: ', end = ' ')
    for letter in missed_letters:
        print(letter, end = ' ')
    print()
    print()

    blanks = '_' * len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    print('Secret word:', end = ' ')

    for letter in blanks:
        print(letter, end = ' ')
    print()
    print()

def get_guess(guessed_words):
    while True:
        print("Guess a letter:", end = ' ')
        guess = input().lower()

        if len(guess) != 1:
            print("Enter a single letter only, ")
        elif guess in guessed_words:
            print("Enter a letter you havent guessed. ")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter in a letter.")
        else:
            return guess

def play_again():
    print("Do you wanna play again? (yes or no)")
    return input().lower().startswith('y')
        
print("Hangman!")

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
            print("You won! The word was: " + secret_word)
            game_is_done = True
        
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMANPICS) - 1:
            display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
            print("You ran out of guesses! The word was: " + secret_word)
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
