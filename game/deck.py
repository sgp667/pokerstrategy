import random as rnd

__ranks__ = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
__suits__ = ["Clubs","Diamods","Hearts","Spades"]

class Card():
    def __init__(self,suit,rank):
        if suit in __suits__:
            self.suit = suit
        else:
            raise ValueError("Cards need to be instansiated with names from __suits__")
    
        if rank in __ranks__:
            self.rank = rank
        else:
            raise ValueError("Cards need to be instansiated with names from __ranks__")

    @classmethod
    def code(cls,code):
        rank = code[1:].upper()
        suit = [suit for suit in __suits__ if suit[0] == code[0]][0]
        return Card(suit,rank)

    def __str__(self):
        return "'" + str(self.rank) + " of " + self.suit + "'"

    def __repr__(self):
        return "<" + self.__str__() + ">"

    @property
    def rank_index(self):
        return __ranks__.index(self.rank)

    @property
    def suit_index(self):
        return __suits__.index(self.suit)

    def __gt__(self,other):
        return (self.rank_index,self.suit_index) > (other.rank_index,other.suit_index)

    def __lt__(self,other):
        return (self.rank_index,self.suit_index) < (other.rank_index,other.suit_index)
