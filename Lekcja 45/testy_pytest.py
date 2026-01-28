import pytest
import funkcje

def test_dodaj():
    assert funkcje.dodaj(10,5) == 15

def test_czy_palindrom():
    assert funkcje.czy_palindrom("oko") == True
    assert funkcje.czy_palindrom("zez") 

def test_czy_nie_palindrom():
    assert funkcje.czy_palindrom("mysz") == False
    assert not funkcje.czy_palindrom("komputer")
