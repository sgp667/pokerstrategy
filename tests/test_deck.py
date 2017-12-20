import pytest
import pokerstrategy

def test_dummy_Success():
    assert True


def test_ranks_exists():
    exists ='ranks' in locals() or 'ranks' in globals()
    assert exists

def test_suites_exists():
    exists ='suites' in locals() or 'suites' in globals()
    assert exists

def test_CardDeck_exists():
    deck = CardDeck()
