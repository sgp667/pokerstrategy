import game.deck as deck

def test_card_rank_can_be_compared():
    ten_of_spades = deck.Card("Spades",10)
    jack_of_spades = deck.Card("Spades","J")

    assert ten_of_spades < jack_of_spades
    assert jack_of_spades > ten_of_spades

def test_cark_suite_can_be_comapred():
    ten_of_spades = deck.Card("Spades",10)
    ten_of_clubs = deck.Card("Clubs",10)

    assert ten_of_spades > ten_of_clubs
    assert ten_of_clubs < ten_of_spades
