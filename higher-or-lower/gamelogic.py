import random 
from names import people
current_score = 0
chosen_people= []
current_people = []
def choose_people():
    chosen_person = (random.choice(people))
    while len(current_people)<3:
        if chosen_person not in chosen_people :
            chosen_people.append(chosen_person)
            current_people.append(chosen_person)
        else:
            choose_people()


def score(choice):
    global current_score
    followers_0 = int(current_people[0]["follower_count"])
    followers_1 = int(current_people[1]["follower_count"])
    if choice == "a":
        if followers_0>followers_1:
            current_score+=1
            current_people.pop(1)
            return game_logic()
        else:
            return f"you have lost with a score of {current_score}"
    else:
        if followers_1>followers_0:
            current_score+=1
            current_people.pop(0)
            return game_logic()
        else:
            return f"you have lost with a score of {current_score}"

def game_logic():
    choose_people()
    print(f"your current score is {current_score}\nA. {current_people[0]['name']},{current_people[0]['description']}, from {current_people[0]['country']}\n")
    print(f"vs\nB. {current_people[1]['name']},{current_people[1]['description']},from {current_people[1]['country']}\n")
    choice = input("who has more followers \"A\" or \"B\": ").lower().strip()
    return score(choice)
    
def game():
    global current_score
    print(f"welcome to a game of \"HIGHER\" or \"LOWER\" \n you current score is {current_score}")
    choose_people()
    result = game_logic()
    print(result)
    current_score=0
    return
game()