import pytest
from pokerstrategy.game.deck import Card
import pokerstrategy.game.hands as hands

@pytest.fixture()
def cardset():
    cards = [Card.code('S2'),Card.code('H2'),Card.code("H3")]
    return hands.CardSet(cards)

def test_can_build_cardset():
    string = hands.CardSet("H2C3")
    cardlist = hands.CardSet([Card.code('H2'),Card.code("C3")])

def test_can_list_ranks(cardset):
    assert cardset.ranks() == ["2","3"]

def test_can_list_suits(cardset):
    assert cardset.suits() == ["Hearts","Spades"]

@pytest.mark.parametrize(["rank","count"],
        [("2",2),("3",1),("4",0),(2,2)])
def test_can_count_ranks(cardset,rank,count):
    assert len(cardset.rank(rank)) == count

@pytest.mark.parametrize(["suit","count"],
        [("Hearts",2),("Spades",1),("Clubs",0)])
def test_can_count_suits(cardset,suit,count):
    assert len(cardset.suit(suit)) == count

def test_can_count_consecutive_cards(cardset):
    consecutive_cards = cardset.consecutive(1)
    assert len(consecutive_cards) == 3
    assert len(consecutive_cards[0]) == 2

def test_can_build_hand():
    cards = [Card.code('S2'),Card.code('S3')]
    cardset = hands.CardSet(cards)
    hand = cardset.hand()
    assert type(hand) is hands.HighcardHand

def test_can_build_pair():
    cards = [Card.code('S2'),Card.code('H2')]
    cardset = hands.CardSet(cards)
    hand = cardset.hand()
    assert type(hand) is hands.PairHand

def test_can_build_threeofkind():
    cards = [Card.code('S2'),Card.code('H2'),Card.code('C2')]
    cardset = hands.CardSet(cards)
    hand = cardset.hand()
    assert type(hand) is hands.ThreeHand
