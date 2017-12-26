import pytest
import pokerstrategy.game.deck as deck

def test_CardDeck_exists():
    cardeck = deck.CardDeck()
    assert type(cardeck) == deck.CardDeck


# Test that decks always have the right amount of cards even after you draw a card
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


def test_empty_CardDeck_throws_an_error_on_draw():
    cardeck = deck.CardDeck()
    
    while cardeck.count > 0:
        cardeck.draw()
    
    with pytest.raises(IndexError) as execinfo:
        drawn_card = cardeck.draw()
    
    assert "empty deck" in str(execinfo) 
    
    with pytest.raises(UnboundLocalError) as execinfo:
        drawn_card 
    
    assert "UnboundLocalError" in str(execinfo) 


# Test that deck can return correct cards
def test_CardDeck_can_return_random_card():
    cardeck = deck.CardDeck()
    
    topcard   = cardeck.cards[0]
    drawncard = cardeck.draw_random()
    assert "tuple" in str(type(drawncard))
    assert topcard[0] != drawncard[0] or topcard[1] != drawncard[1]