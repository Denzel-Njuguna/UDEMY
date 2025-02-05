import nltk
from nltk.corpus import words
import random 
word_list = words.words()
random_word = (random.choice(word_list)).lower()
char_no = len(random_word)
dashes = list(("_") * char_no)
name = '''                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
lives = 6 

def char_checker(lives,dashes):
    user_input = input("please enter your guess \n").strip().lower()
    if len(user_input) > 1:
        lives-=1
        return lives
    if user_input in random_word:
        letter_indices = [index for index, letter in enumerate(random_word) if letter == user_input]
    
        finished = True
        for index in letter_indices:
            if dashes[index] == "_":
                dashes[index] = user_input
                finished = False
                break
        updated_word =''.join(dashes)
        print(f"these are the letters you have filled in {updated_word}")
        if finished:
            lives-=1
            print(f"you have already filled all instances of letter {user_input}")
        return lives
    else:
        print("this letter is not in the word")
        lives -=1
        return lives
def game():
    global random_word
    print("welcome to a game of hangman\n" + name )
    print(random_word)
    global lives
    while lives > 0:
        print(dashes)
        if "_" not in dashes:
            print(f"you have won the game and the word is {random_word}")
            return
        else:
            lives = char_checker(lives,dashes)
            print(f"you have {lives} lives left")
    else:
        print("you have lost the game")
        return
if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print("the user has ended the game ")