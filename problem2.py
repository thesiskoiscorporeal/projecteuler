ans = 2
a = 1
b = 2

while b < 4000000:
    a += b
    if a % 2 == 0 and a < 4000000:
        ans += a
    b += a
    if b % 2 == 0 and b < 4000000:
        ans += b

print(ans)