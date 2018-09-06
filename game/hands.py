import re
from pokerstrategy.game.deck import Card

class CardSet():
    def __init__(self,cards):
        if isinstance(cards,str):
            card_names = re.split("[CDHS][^CDHS]+",cards)
            cards = []
            for card in card_names:
                cards.append(Card.code(card))
        cards.sort()
        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self,item):
        return self.cards[item]

    def __len__(self):
        return len(self.cards)

    def append(self,card):
        self.cards.append(card)

    def rank(self, rank):
        return CardSet([card for card in self.cards if card.rank == str(rank)])

    def ranks(self):
        ranks = []
        for card in self.cards:
            if card.rank in ranks:
                continue
            ranks.append(card.rank)
        return ranks

    def suit(self, suit):
        return CardSet([card for card in self.cards if card.suit == suit])

    def suits(self):
        suits = []
        for card in self.cards:
            if card.suit in suits:
                continue
            suits.append(card.suit)
        return suits

    def consecutive(self,lowest):
        chains = []
        for card in self.cards:
            for cursor, chain in enumerate(chains):
                highest_card = max(chain)
                if highest_card.rank_index + 1 == card.rank_index:
                    chains[cursor].append(card)
            chains.append(CardSet([card]))
        return [chain for chain in chains if len(chain) >= lowest]
    
    def hand(self):
        pairs = [ self.rank(rank) for rank in self.ranks() if len(self.rank(rank)) == 2]
        triplets = [ self.rank(rank) for rank in self.ranks() if len(self.rank(rank)) == 3]
        if False:
            pass
        elif len(triplets) == 1:
            return ThreeHand(self.cards)
        elif len(pairs) == 1:
            return PairHand(self.cards)
        else:
            return HighcardHand(self.cards)

class BaseHand():
    def __init__(self,members):
        members.sort()
        self.members = members

class HighcardHand(BaseHand):
    pass

class PairHand(BaseHand):
    pass

class ThreeHand(BaseHand):
    pass
