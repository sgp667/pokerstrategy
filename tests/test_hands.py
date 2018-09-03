import pytest
from pokerstrategy.game.deck import Card
import pokerstrategy.game.hands as hands

@pytest.mark.parametrize(['cards','rank','expected'],[
    ([Card('Spades',2),Card('Hearts',2)],2,2),
    ([Card('Spades',3),Card('Hearts',3)],2,0)
])
def test_can_count_ranks(cards,rank,expected):
    counts = hands.CardCounter(cards)
    assert counts.rank(rank) == expected

@pytest.mark.parametrize(['cards','suite','expected'],[
    ([Card('Spades',2),Card('Spades',3)],"Spades",2),
    ([Card('Spades',3),Card('Hearts',3)],"Hearts",1)
])
def test_can_count_suites(cards,suite,expected):
    counts = hands.CardCounter(cards)
    assert counts.suite(suite) == expected

@pytest.mark.parametrize(['cards','suite','expected'],[
    ([Card('Spades',2),Card('Spades',3)],"Spades",2),
    ([Card('Spades',3),Card('Hearts',3)],"Hearts",1)
])
def test_can_count_suites(cards,suite,expected):
    counts = hands.CardCounter(cards)
    assert counts.suite(suite) == expected

def test_can_match_card_counts():
    class HandDummy():
        pass

    card_count = {'dummy': 2}
    assert card_count.get('dummy') == 2

    hand = hands.build_hand(card_count,HandDummy,dummy = 2) 
    assert hand is HandDummy

@pytest.mark.skip()
def test_can_build_pair():
    cards = [
            Card('Spades',2),
            Card("Hearts",2)
            ]

    assert len(cards) == 2
    assert type(cards) == list

    hand = hands.hand_factory(cards)

    assert hand is hands.HandPair
