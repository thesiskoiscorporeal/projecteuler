'''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?'''

'''maximise the number of TERMS added
'''

def primegenerator(num):
    num = int(num)
    lst = [2]
    if num < 3:
        return lst

    for i in range(3, num + 1):       
        if i % 2 == 1:
            for n in range(3, int(i ** 0.5) + 1, 2):
                if i % n == 0:
                    break
            else:
                lst.append(i)

    return lst


prime_list = primegenerator(1000000) # obtain list of primes under 1,000,000

max_n = 0
answer = 0

print(len(prime_list))

for i in range(50): #generate consequetive sums to max prime under 1,000,000 starting from item #iterate over item in prime_list
    answer_list = []
    n_counter = 0 #number of terms counter
    tmp = 0
    print(i)
    while tmp < 1000000:
        tmp += prime_list[i]
        i += 1
        n_counter += 1
        if tmp%2 == 0:
            continue
        elif tmp in prime_list:
            answer_list.append(tmp)
            n = n_counter
    if n > max_n:
        max_n = n
        answer = max(answer_list)

print(answer)