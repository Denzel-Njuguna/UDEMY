from resources import resources_left
from resources import coffee_type
from resources import resource_revenue
from resources import coffee_price




def coffee():
    def calculate_resources(type):
        resource_used = coffee_type[type]
        if type == "latte":
            for key in resource_used:
                if resources_left[key] < resource_used[key]:
                    return False  

            for key in resource_used:
                resources_left[key] -= resource_used[key]
            
            return True 
        else:
            for key in resource_used:
                if resources_left[key] < resource_used[key]:
                    return False  
                           
            for key in resource_used:
                resources_left[key] -= resource_used[key]
            
            return True 
    users_choice = input("What would you like (espresso/latte/cappuccino): ").lower().strip()
    # to check remaining resources
    if users_choice == "report":
        for key,value in resources_left.items():
            print(f"{key}:{value}")
        return
    # to refill
    elif users_choice == "refill":
        refill = input('what would you like to refill (water:100)\n').lower().strip()
        key,value = refill.split(':')
        for key in resources_left.keys():
            previous = resources_left[key]
            resources_left[key] = previous + int(value)
        return
    # for an espresso
    elif users_choice == "espresso":
        check = calculate_resources("espresso")
        if check == True:
            print(f"the price of the coffee is {coffee_price['espresso']:.2f}")
            price = coffee_price['espresso']
            quarters = int(input(f"how many quarters: "))
            dimes = int(input(f"how many dimes: "))
            nickels = int(input(f"how many nickels: "))
            pennies = int(input(f"how many pennies: "))
            user_total =((0.25 * quarters)+ (dimes * 0.10)+(nickels * 0.05)+(pennies*0.01)) 
            if user_total >=price:
                change = user_total - price
                resource_revenue["money"] += price
                return(f"your change is {change:.2f}\nhere's your coffee \U00002615 enjoy") 
            else:
                return(f"here is your {user_total:.2f},\nnot enough for an espresso")
        elif check == False:
            return("there was not enough ingredients")
    # for a latte
    elif users_choice == "latte":
        check = calculate_resources("latte")
        if check == True:
            print(f"the price of the coffee is {coffee_price['latte']:.2f}")
            price = coffee_price['latte']
            quarters = int(input(f"how many quarters: "))
            dimes = int(input(f"how many dimes: "))
            nickels = int(input(f"how many nickels: "))
            pennies = int(input(f"how many pennies: "))
            user_total =((0.25 * quarters)+ (dimes * 0.10)+(nickels * 0.05)+(pennies*0.01)) 
            if user_total >=price:
                change = user_total - price
                resource_revenue["money"] += price
                return(f"your change is {change:.2f}\nhere's your coffee \U00002615 enjoy") 
            else:
                return(f"here is your {user_total:.2f},\nnot enough for an latte")
        elif check == False:
            return("there was not enough ingredients")
    # for a cappuccino
    elif users_choice == "cappuccino":
        check = calculate_resources("cappuccino")
        if check == True:
            print(f"the price of the coffee is {coffee_price['cappuccino']:.2f}")
            price = coffee_price['cappuccino']
            quarters = int(input(f"how many quarters: "))
            dimes = int(input(f"how many dimes: "))
            nickels = int(input(f"how many nickels: "))
            pennies = int(input(f"how many pennies: "))
            user_total =((0.25 * quarters)+ (dimes * 0.10)+(nickels * 0.05)+(pennies*0.01)) 
            if user_total >=price:
                change = user_total - price
                resource_revenue["money"] += price
                return(f"your change is {change:.2f}\nhere's your coffee \U00002615 enjoy") 
            else:
                return(f"here is your {user_total:.2f},\nnot enough for an cappuccino")
        elif check == False:
            return("there was not enough ingredients")
def game():
    while True:
        result = coffee()
        print(result)
        
game()