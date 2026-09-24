number = -50

primes = []

if number <= 1:
    primes = []
elif number == 2:
    primes = [2]
elif number == 3:
    primes = [2, 3]
else:
    primes = [2, 3]
    for i in range(1, number + 1):
        j = 2
        is_prime = False
        while j <= i ** (1 / 2):
            if i % j == 0:
                is_prime = False
                break
            else:
                is_prime = True
            j += 1
        if is_prime == True:
            primes.append(i)

print(primes)
