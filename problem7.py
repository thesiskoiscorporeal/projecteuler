
primes = [2]
n = 1
i = 2

while True:
    i += 1
    if n == 10001:
        break
    elif i%2 == 0: #if i divisible by 2
        continue
    elif 0 in [i%prime for prime in primes]:
        continue
    else:
        primes.append(i)
        n += 1

'''
COULD HAVE SOLVED THE BREAKING OUT OF NESTED LOOP LOGIC BY DEFINING A FUNCTION THAT RETURNED SOMETHING
'''

print(primes[10000])