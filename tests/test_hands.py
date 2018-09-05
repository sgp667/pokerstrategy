import pytest
from pokerstrategy.game.deck import Card
import pokerstrategy.game.hands as hands

@pytest.mark.parametrize(['cards','rank','expected'],[
    ([Card('Spades',2),Card('Hearts',2)],2,2),
    ([Card('Spades',3),Card('Hearts',3)],2,0)
])
def test_can_count_ranks(cards,rank,expected):
    cardset = hands.CardSet(cards)
    assert len(cardset.rank(rank)) == expected

@pytest.mark.parametrize(['cards','suite','expected'],[
    ([Card('Spades',2),Card('Spades',3)],"Spades",2),
    ([Card('Spades',3),Card('Hearts',3)],"Hearts",1)
])
def test_can_count_suites(cards,suite,expected):
    cardset = hands.CardSet(cards)
    assert len(cardset.suite(suite)) == expected

@pytest.mark.parametrize(['cards','suite','expected'],[
    ([Card('Spades',2),Card('Spades',3)],"Spades",2),
    ([Card('Spades',3),Card('Hearts',3)],"Hearts",1)
])
def test_can_count_suites(cards,suite,expected):
    cardset = hands.CardSet(cards)
    assert len(cardset.suite(suite)) == expected


def test_can_build_hand_from_cardset():
    cards = [Card('Spades',2),Card('Spades',3)]
    cardset = hands.CardSet(cards)
    hand = cardset.hand()
    assert type(hand) is hands.HighcardHand
