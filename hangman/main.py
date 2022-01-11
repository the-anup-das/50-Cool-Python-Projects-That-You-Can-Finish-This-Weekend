import random
from words_list import word_list

#generate random word
word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

#generate as many blanks as letters in a word
def gen_blanks(word):
    blank = []
    for i in range(len(word)):
        blank += "_"    
    print(blank)
    return blank

def user_input():
    user = input("Guess a letter: ")
    return user.lower()

def check_guess(word, letter, result):
    #result = []
    for i in range(len(word)):
        if letter == word[i]:
            result[i] = letter
    return result

FLAG_END_GAME = False
LIVES = 6

print(logo)
print("Welcome to my game!") 
print("Guess the word...\n")

result = gen_blanks(word)
while not FLAG_END_GAME:
    print(word)
    user_guess = user_input()
    
    if user_guess in result:
        print(f"You already guessed {user_guess}")
        print(result)

    result = check_guess(word,user_guess,result)



    if user_guess not in word:
        LIVES -= 1
        
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        print(stages[LIVES])
        
        if LIVES == 0:
            FLAG_END_GAME = True
            print("\nYou lose!")
        else:
            print(result)
    else:
        print(result)

    if "_" not in result:
        FLAG_END_GAME = True
        print("\nYou win!")