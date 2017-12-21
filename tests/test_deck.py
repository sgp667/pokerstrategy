import pytest
import pokerstrategy.game.deck as deck

def test_CardDeck_exists():
    cardeck = deck.CardDeck()
    assert type(cardeck) == deck.CardDeck


# Test that decks always have teh right amount of cards even after you draw a card
def test_singe_CardDeck_has_52_cards():
    cardeck = deck.CardDeck()
    assert len(cardeck.cards) == 52
    assert cardeck.count      == 52

def test_two_CardDeck_has_x_cards():
    cardeck = deck.CardDeck(2)
    assert len(cardeck.cards) == 104
    assert cardeck.count      == 104
    

@pytest.mark.parametrize("init_decks,draws,expected",[
    (1,0,52),
    (2,0,104),
    (1,1,51),
    (1,2,50)])
def test_CardDeck_has_x_cards(init_decks,draws,expected):
    cardeck = deck.CardDeck(init_decks)
    drawncards = list()
    
    for x in range(draws):
        card = cardeck.draw()
        drawncards.append(card)
        
    assert len(cardeck.cards) == expected
    assert cardeck.count      == expected
    assert len(drawncards)    == draws
    
# TODO Write a test case where CardDeck trows an error if you try to draw a card after all cards have been drawn