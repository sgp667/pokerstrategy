class CardSet():
    def __init__(self,cards):
        cards.sort()
        self.cards = cards

    def __getitem__(self,item):
        return self.cards[cards]

    def __len__(self):
        return len(self.cards)

    def rank(self, rank):
        return CardSet([card for card in self.cards if card.rank == rank])

    def suite(self, suite):
        return CardSet([card for card in self.cards if card.suite == suite])

    def consecutive(self,lowest):
        chains = []
        for card in self.cards:
            for cursor, chain in enumerate(chains):
                higest_card = max(chain)
                if highest.rank_index + 1 == card.rank_index:
                    chains[cusor].append(card)
                else:
                    chains.append(CardSet(card))
        return [chain for chain in chains if len(chain) >= lowest]
    
    def hand(self):
        if False:
            pass
        else:
            cards = self.cards
            return HighcardHand(cards)

class BaseHand():
    def __init__(self,members):
        self.members = members

class HighcardHand(BaseHand):
    pass
class PairHand(BaseHand):
    pass
