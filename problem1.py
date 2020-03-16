
# construct list of multiples of 3 under 1000, multiples of 5 under 1000
listof3 = range(0, 1000, 3)
listof5 = range(0, 1000, 5)

answer = 0 

# iterate over integers from 1 to 1000, increment answer BY integer if integer is IN either list
for i in range(1000):
    if i in listof3 or i in listof5:
        answer += i

print(answer)
