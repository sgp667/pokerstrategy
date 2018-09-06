import pytest
from pokerstrategy.game.deck import Card

@pytest.fixture()
def ten_of_spades():
    return Card("Spades","10")

@pytest.fixture()
def jack_of_spades():
    return Card("Spades","J")

@pytest.fixture()
def ten_of_clubs():
    return Card("Clubs","10")

def test_card_rank_can_be_compared_to_greater(ten_of_spades,jack_of_spades):
    assert ten_of_spades < jack_of_spades

def test_card_rank_can_be_compared_to_lesser(ten_of_spades,jack_of_spades):
    assert jack_of_spades > ten_of_spades

def test_card_suit_can_be_compared_to_greater(ten_of_spades,ten_of_clubs):
    assert ten_of_spades > ten_of_clubs

def test_card_suit_can_be_compared_to_lesser(ten_of_spades,ten_of_clubs):
    assert ten_of_clubs < ten_of_spades

def test_card_can_be_instansiated():
    coded = Card.code("S10")
    longer = Card("Spades","10")
    assert (coded.rank_index,coded.suit_index) == (longer.rank_index,longer.suit_index)
