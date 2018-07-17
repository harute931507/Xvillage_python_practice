import random
import timeit
import operator as op

def card_machine1(deck):
    result = []
    random.shuffle(deck)
    for i in range(0, 4):
        result.append(list(deck[0 + 12 * i : 12 * (i+1) - 1]))

    return result

def card_machine2(deck):
    
    # 洗牌
    random.shuffle(deck)
    
    # 發牌
    return [list(selector(deck)) for selector in [op.itemgetter(*list(range(x, len(deck), 4))) for x in range(0, 4)]]

Deck = [x+y for x in ["黑桃", "紅心", "鑽石", "梅花"]
        for y in ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]]

print(card_machine1(Deck))
print(card_machine2(Deck))

# t1 = timeit.default_timer()
# for i in range(0,100000):
#     card_machine1(Deck)
# t2 = timeit.default_timer()
# for i in range(0,100000):
#     card_machine2(Deck)
# t3 = timeit.default_timer()

# print(t2-t1)
# print(t3-t2)

