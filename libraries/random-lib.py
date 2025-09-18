
import random                         #import whole library
from random import choice             #import a specific module from library

# example of a rolling dice using `choice()`
'''coin = choice(["head","tail"])'''

coin = random.choice(["head","tail"])
print(coin)

if coin == "head":
    print("you got it its a head")
else: print("you got it its a tail")

# example of number guesing game using `randint()`

number = random.randint(1,100)
print(number)

# example of shuffle gamecards using `shaffle()`

cards = ["spade","hearts","king","queen"]

random.shuffle(cards)

for card in cards:
    print(card)

#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())