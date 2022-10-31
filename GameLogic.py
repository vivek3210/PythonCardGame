import itertools
import random
import pygame

deck = list(itertools.product(range(1,2),['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']))

random.shuffle(deck)
# draws three cards
print("You got:")
for i in range(3):
    print(deck[i][0], "of", deck[i][1])

