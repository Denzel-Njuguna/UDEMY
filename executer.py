# Target is the number up to which we count
def fizz_buzz(target):
    all = []
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            all.append("FizzBuzz")
        elif number % 3 == 0:
            all.append("Fizz")
        elif number % 5 == 0:
            all.append("Buzz")
        else:
            all.append(number)
    return all
result = fizz_buzz(15)
print(result)