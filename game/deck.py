import random as rnd

suites = ['Clubs','Diamonds','Hearts','Spades']
ranks = range(0,13)

class CardDeck:
    def __init__(self,decks = 1):
        self.cards  = [(suite, rank) for suite in suites for rank in ranks for x in range(0,decks)]
        self.count  = len(self.cards)
        
    def draw(self, index = 0):
        try:
            drawn_card = self.cards.pop(index)
            self.count = len(self.cards)
            return drawn_card
        except IndexError:
            #print(,sys.exc_info()[0])
            raise IndexError("Cannot draw card from an already empty deck")
            
    def draw_random(self):
        drawn_index = rnd.randrange(0,self.count-1,1)
        return self.draw(drawn_index)