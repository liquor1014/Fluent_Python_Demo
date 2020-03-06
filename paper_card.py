import collections
from random import choice

Card = collections.namedtuple('card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank , suit) for suit in self.suits
                                        for rank in self.ranks
                      ]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

deck = FrenchDeck()
# print(len(deck))
# print(choice(deck))
# print(deck[:3])
# print(deck[0::13])


list1 = deck[:13]
# for i in list1:
#     print(i)
for card in reversed(deck):
    print(card)