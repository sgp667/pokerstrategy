import random as rnd

suites = ['Clubs','Diamonds','Hearts','Spades']
ranks = range(0,13)
__ranks__ = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
__suites__ = ["Clubs","Diamods","Hearts","Spades"]

class Card():
    def __init__(self,suite,rank):
        if suite in __suites__ and rank in __ranks__:
            self.suite = suite
            self.rank = rank
        else:
            raise ValueError("Cards need to be instansiated with names from __ranks__ and __suites")
    
    @property
    def rank_index(self):
        return __ranks__.index(self.rank)

    def is_consecutive(self,other,same_suite=False):
        if same_suite and self.suite != other.suite:
               return False 
        return self.rank_index + 1 == other.rank_index

    def __str__(self):
        return "'" + str(self.rank) + " of " + self.suite + "'"

    def __repr__(self):
        return "<" + self.__str__() + ">"

    def __gt__(self,other):
        return self._compare_cards_(other,-1)

    def __lt__(self,other):
        return self._compare_cards_(other,1)

    def __ge__(self,other):
        return self._compare_cards_(other,-1) or self.__eq__(other)

    def __le__(self,other):
        return self._compare_cards_(other,1) or self.__eq__(other)

    def __eq__(self,other):
        return self._compare_cards_(other,0)
    
    def __ne__(self,other):
        return not self.__eq__(other)

    def _compare_cards_(self,other,expect):
        rank_comp = self._compare_ranks_(other.rank,self.rank)
        if rank_comp == 0:
            return self._compare_suites_(other.suite,self.suite) == expect
        return rank_comp == expect

    def _compare_ranks_(self,rank1,rank2):
        return self._compare_attributes_("rank",rank1,rank2)

    def _compare_suites_(self,suite1,suite2):
        return self._compare_attributes_("suite",suite1,suite2)
    
    def _compare_attributes_(self,name,attr1,attr2):
        attr_list = eval("__{}s__".format(name))

        if attr_list.index(attr1) < attr_list.index(attr2):
            return -1
        if attr_list.index(attr1) == attr_list.index(attr2):
            return 0
        if attr_list.index(attr1) > attr_list.index(attr2):
            return 1
