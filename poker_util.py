from poker import *

def what_i_have(avail):
    flush = False
    straight = False
    straighthc = list(Rank)[0]
    foak = False
    toak = False
    pair = False
    pairr = []

    allranks = list(Rank)
    allsuits = list(Suit)

    for i in range(len(avail)-4):
        start_idx = allranks.index(avail[i].rank)
        temp = True
        try:
            for j in range(5):
                if allranks[start_idx+j] != avail[i+j]:
                    temp = False
        except:
            pass
        if temp:
            straight = True
    
    for suit in allsuits:
        count = 0
        for card in avail:
            if card.suit == suit:
                count+=1
        if count == 5:
            flush = True
            flushs = suit
        
    for rank in allranks:
        count = 0
        for card in avail:
            if card.rank == rank:
                count+=1
        if count == 4:
            foak = True
            foakr = rank
        if count == 3:
            toak = True
            toakr = rank
        if count == 2:
            pair = True
            pairr.append(rank)


    ##Royal flush
    if flush and straight and straighthc.rank == allranks[len(allranks-1)]:
        return "Royal flush"
    ##straight flush
    if flush and False:
        return "straight flush " + flushs.suit
    ##four of a kind
    if foak:
        return "Four of " + str(foakr)
    ##full house
    if toak and pair:
        return str(pairr[0]) + "s full of " + str(toakr)+"s"
    ##flush
    if flush:
        return "Flush of " + str(flushs)
    ##straight
    if straight:
        return "straight with high card " + str(straighthc)
    ##three of a kind
    if toak:
        return "Three of " + str(toakr)
    ##two pairs
    if len(pairr) == 2:
        return "pair of " + str(pairr[0]) + " pair of " + str(pairr[1])
    ##one pair
    if len(pairr) == 1:
        return "pair of " + str(pairr[0])

    return "high_card"







