from num2words import num2words

namelist = []


for n in range(1,1001):
    namelist.append(num2words(n))

counter = 0
for item in namelist:
    for letter in item:
        if letter.isalpha():
            counter += 1


print(counter)