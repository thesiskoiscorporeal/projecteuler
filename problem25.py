a = 1
b = 1 
n = 2

while len(str(a)) < 1000 and len(str(b)) < 1000:
    a += b
    n += 1
    if len(str(a)) < 1000:
        b += a
        n += 1

print()