import random
def randomizer(value):
    return random.randint(1,value)
     


def userinput():
    no_letters = int(input("how many letters would you like in your password\n"))
    no_symbols = int(input("how many symbols would you like \n"))
    no_numbers = int(input("how many numbers would you like \n"))
    # chr() this is using the ascii codes to generate the corresponding symbols
    capital_letters = [chr(i) for i in range(ord('A'),ord('Z') + 1)]
    small_letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
    numbers = [i for i in range(10)]
    symbols = list("!@#$%^&*()_+-=[]{}|;:'\",.<>?/")
    return ([no_letters,no_numbers,no_symbols,capital_letters,small_letters,numbers,symbols])

def passwordrandomizer(no_letters,no_numbers,no_symbols,capital_letters,small_letters,numbers,symbols):
    
    uppercase_no = randomizer(no_letters)
    random_uppercase = random.sample(capital_letters,uppercase_no)
    lowercase_no = no_letters - uppercase_no
    random_lowercase = random.sample(small_letters,lowercase_no)
    random_numbers = random.sample(numbers,no_numbers)
    random_symbols = random.sample(symbols,no_symbols)
    unmixed_password =random_symbols+random_lowercase+random_numbers+random_uppercase
    random.shuffle(unmixed_password)
    return "".join(map(str,unmixed_password))
values = userinput()
password = passwordrandomizer(*values)
print(password)