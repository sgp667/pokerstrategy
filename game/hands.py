
def hand_factory(cards):
    card_count = count_cards(cards)

def build_hand(card_counts,hand,**cond):
    for card_type, count in cond.items():
         if card_counts.get(card_type,0) == count:
             return hand

class CardCounter():
    def __init__(self,cards):
        self.cards = cards
        self.count_ranks()
        self.count_suites()

    def count_ranks(self):
        self.__ranks__ = {}
        for card in self.cards:
            self.__ranks__[card.rank] = self.__ranks__.get(card.rank,0) + 1

    def rank(self,value):
        return self.__ranks__.get(value,0)

    def count_suites(self):
        self.__suites__ = {}
        for card in self.cards:
            self.__suites__[card.suite] = self.__suites__.get(card.suite,0) + 1

    def suite(self,value):
        return self.__suites__.get(value,0)


class HandBase():
    def __init__(self,members):
        self.members = members

class HandPair(HandBase):
    pass
