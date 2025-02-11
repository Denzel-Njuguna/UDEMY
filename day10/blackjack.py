import random
computers_cards = []
users_cards = []
users_tally = 0
computers_tally = 0
blackjack_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": [1, 11]  # Ace can be either 1 or 11
} 

def game_logic():
    deal_again = input("would you like to hit\n")
    if deal_again == "y":
        return play_again()
    else:
        return calculating_winner()
    
def play_again():
    global users_tally
    card_dealt_touser = random.choice(list(blackjack_values.keys()))
    cards_dealt_tocomp = random.choice(list(blackjack_values.keys()))
    if card_dealt_touser == "A":
        users_cards.append("A")
        choice = input("what would you like the value of your ace to be\n")
        if choice == "1":
           users_tally+=int(blackjack_values["A"][0])
        else:
           users_tally+=int(blackjack_values["A"][1])
    else:
        users_cards.append(card_dealt_touser)
        users_tally +=int(blackjack_values[card_dealt_touser])
    if cards_dealt_tocomp == "A":
        defining_ace()
    else:
        computers_cards.append(cards_dealt_tocomp)
        users_tally +=int(blackjack_values[cards_dealt_tocomp])
    print(f"computers face up : {computers_cards[0]}")
    print(f"player's cards are: {','.join(users_cards)}")
    return game_logic()
def defining_ace():
    global computers_tally
    computers_cards.append("A")
    if computers_tally>11:
        computers_tally += int(blackjack_values["A"][0])
    else:
        computers_tally+= int(blackjack_values["A"][1])

def calculating_winner():
    global users_tally
    global computers_tally

    if  users_tally>computers_tally and users_tally<=21:
        return f"the winner is player whose cards were {','.join(users_cards)} with a total of {users_tally}"
    elif users_tally==computers_tally:
        return "it was a tie"
    else:
        return f"computer is the winner"
def game():
    global users_tally
    global computers_tally
    users_tally = 0
    computers_tally = 0
    users_cards.clear()
    computers_cards.clear()
    start_game = input("would you like to play game of blackjack\n")
    if start_game == "y":
        for each in range(2):
            cards_dealt_touser = random.choice(list(blackjack_values.keys()))
            cards_dealt_tocomp = random.choice(list(blackjack_values.keys()))
            if cards_dealt_touser == "A":
                users_cards.append("A")
                choice = input("what would you like the value of your ace to be\n")
                if choice == "1":
                    users_tally += int(blackjack_values["A"][0])
                else:
                    users_tally +=int(blackjack_values["A"][1])
            else:
                users_cards.append(cards_dealt_touser)
                users_tally += int(blackjack_values[cards_dealt_touser])
            if cards_dealt_tocomp == "A":
                defining_ace()
            else:   
                computers_cards.append(cards_dealt_tocomp)
                users_tally += int(blackjack_values[cards_dealt_tocomp])
        print(f"computers face up : {computers_cards[0]}")
        print(f"player's cards are: {','.join(users_cards)}")
        result = game_logic()
        print(result)
    else:
       return print("fuck you")
    
        
    
game()

        