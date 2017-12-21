import pytest
import pokerstrategy.game.deck as deck

def test_CardDeck_exists():
    cardeck = deck.CardDeck()
    assert type(cardeck) == deck.CardDeck

def test_singe_CardDeck_has_52_cards():
    cardeck = deck.CardDeck()
    assert len(cardeck.cards) == 52

def test_two_CardDeck_has_x_cards():
    cardeck = deck.CardDeck(2)
    assert len(cardeck.cards) == 104