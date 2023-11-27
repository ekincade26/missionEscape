## word jumble

import random


rword = 'physics'
word = list(rword)

#word = ['s','k','u','l','l']
print(word)

num = len(word)
print(num)

i = 0
j = 0
scram = []
helper = len(word)
#print(random.randint(0,num-1))
while i<num:
    popThis = random.randint(0,helper-1)
    print(popThis)
    scram.append(word.pop(popThis))
    #scram[j]
    #print(let)
    i = i+1
    j = j+1
    helper = len(word)

print(scram)


for ii in range(0,3):
    guess = input('what is your guess: ')
    if guess == rword:
        print('correct!')
        break
    else:
        print('incorrect')







