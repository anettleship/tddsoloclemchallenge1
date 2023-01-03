import pytest
from phonewords import phonewords

def test_phonewords_should_return_empty_list_when_given_empty_list_and_blank_number():
    number = ""
    wordlist = []
    assert phonewords(number, wordlist) == [] 


def test_phonewords_should_return_empty_list_when_given_any_list_and_blank_number():
    number = ""
    wordlist = ["a"]
    assert phonewords(number, wordlist) == []


@pytest.mark.parametrize("number", [(""),("1"),("12345"),("987654321")])
def test_phonewords_should_return_empty_list_when_given_empty_list_and_any_number(number):
    wordlist = []
    assert phonewords(number, wordlist) == [] 