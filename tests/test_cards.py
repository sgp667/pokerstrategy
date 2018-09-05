import pytest
from pokerstrategy.game.deck import Card

def test_card_rank_can_be_compared():
    ten_of_spades = Card("Spades",10)
    jack_of_spades = Card("Spades","J")

    assert ten_of_spades < jack_of_spades
    assert jack_of_spades > ten_of_spades
    assert ten_of_spades <= jack_of_spades
    assert jack_of_spades >= ten_of_spades

def test_card_suite_can_be_comapred():
    ten_of_spades = Card("Spades",10)
    ten_of_clubs = Card("Clubs",10)

    assert ten_of_spades > ten_of_clubs
    assert ten_of_clubs < ten_of_spades
    assert ten_of_spades >= ten_of_clubs
    assert ten_of_clubs <= ten_of_spades


@pytest.mark.parametrize(
    ["card"             ,"same_suite"   ,"result"],[
    (Card("Spades","J") ,True           ,True   ),
    (Card("Hearts","J") ,True           ,False  ),
    (Card("Hearts",10 ) ,True           ,False  ),
    (Card("Hearts","Q") ,False          ,False  )])
def test_card_can_compare_consecutive(card,same_suite,result):
    ten_of_spades = Card("Spades",10)
    assert ten_of_spades.is_consecutive(card,same_suite= same_suite) == result
