num = 600851475143
p = 2 

factors = []

while p < num + 1:
    if num%p == 0:
        num /= p
        factors.append(p)
    else:
        p += 1

print(max(factors))