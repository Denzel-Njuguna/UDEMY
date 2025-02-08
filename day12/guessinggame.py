import random
level_difficulty = ""
no_hints = 0
target_no = 0
guess = 0

def generate_random():
    global target_no
    target_no = random.randint(0,101)
    print(target_no)

# this is the function to handle when the user fails
def hinter():
    global guess
    global no_hints
    if target_no>guess:
        print ("the target number is greater")
        no_hints-=1
    elif guess>target_no:
        print ("the target number is lesser")
        no_hints-=1
    else:
        return f"correct the number was {target_no}"
    return check_winner()

def check_winner():
    global guess
    global target_no
    while no_hints>0:
        guess = int(input(f"what is you guess and you have {no_hints} hints remaining\n"))
        return hinter()
    else:
        return f"you have lost the target number was {target_no}"    
    
def game():
    global level_difficulty
    global no_hints
    global guess
    level_difficulty = input("welcome to the guessing game \n what difficulty would you like \"easy\" or \"hard\" \n").lower().strip()
    if level_difficulty == "easy":
        no_hints = 10
    elif level_difficulty == "hard":
        no_hints = 5
    generate_random() 
    guess = int(input("what number are you going to guess\n"))
    if guess == target_no:
        print( f"correct the number was {target_no}")
    else:
        result = hinter()
        print (result)
        game()
game()