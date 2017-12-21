suites = ['Clubs','Diamonds','Hearts','Spades']
ranks = range(0,13)

class CardDeck:
    def __init__(self,decks = 1):
        self.cards  = [(suite, rank) for suite in suites for rank in ranks for x in range(0,decks)]
        self.count  = len(self.cards)
        
    def draw(self):
        deck = self.cards
        drawn_card = deck.pop
        self.cards = deck
        self.count = len(deck)
        return drawn_card
     