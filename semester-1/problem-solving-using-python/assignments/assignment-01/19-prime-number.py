number = 7

is_prime = False

if number <= 1:
    pass
elif number == 2 or number == 3:
    is_prime = True
else:
    i = 2
    while i <= number ** (1 / 2):
        if number % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
        i = i + 1

if is_prime == True:
    print("The number is prime.")
else:
    print("The number is not prime.")
