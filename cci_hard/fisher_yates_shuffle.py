import random

def shuffle():
    n_cards = 52
    deck = range(52)
    for i in range(52):
        k = random.randint(i, 52)
        deck[i], deck[k] = deck[k], deck[i]


