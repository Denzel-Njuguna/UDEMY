bidders_dictionary = {

}
highest_bidder_value = [0]

def auction_input():
    users_name = input("welcome to the secret auction program\n what is your name?:").capitalize().strip()
    users_bid = int(input('what\'s you bid?:').strip())
    auction_logic(users_name,users_bid)
    
    # reverse_dictionary = {

    # }
def auction_logic(users_name,users_bid):   
    if users_bid > highest_bidder_value[0]:
        highest_bidder_value[0] = users_bid

    bidders_dictionary[users_name] = users_bid
    # reverse_dictionary[users_bid] = users_name
def get_user():
    highest_bid = highest_bidder_value[0]
    winner = [k for k, v in bidders_dictionary.items() if v  == highest_bid]
    
    return f"{','.join(winner)} with a bid of {highest_bid}"

def silent_auction():
    auction_input()
    next = input("are the any more bidders \"yes\" or \"no\"\n").strip().lower()
    if next == 'no':
        result = get_user()
        print(f"{result}")
    else:
        silent_auction()
if __name__ == "__main__":
    try:
        silent_auction()
    except KeyboardInterrupt:
        print("a user has terminated the contract")