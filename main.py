from poker import *
from poker_util import *
import random

for i in range(10000):
    deck = list(Card)
    random.shuffle(deck)

    hand = [deck.pop(), deck.pop()]
    #print(hand)

    flop = [deck.pop(),deck.pop(),deck.pop()]

    turn = [deck.pop()]
    river = [deck.pop()]

    avail = flop + turn + river + hand
    avail.sort(key=lambda x: x.rank)

    

    print(avail)
    print(what_i_have(avail))
    if "straight" in what_i_have(avail):
        print("straight")
