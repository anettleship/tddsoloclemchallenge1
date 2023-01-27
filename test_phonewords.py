import pytest
from phonewords import phonewords


def test_phonewords_should_return_empty_list_when_given_empty_list_and_blank_number():
    phonewords_maker = phonewords()
    number = ""
    wordlist = []
    assert phonewords_maker.list_words(number, wordlist) == [] 


def test_phonewords_should_return_empty_list_when_given_any_list_and_blank_number():
    phonewords_maker = phonewords()
    number = ""
    wordlist = ["a"]
    assert phonewords_maker.list_words(number, wordlist) == []


@pytest.mark.parametrize("number", [(""),("1"),("12345"),("987654321")])
def test_phonewords_should_return_empty_list_when_given_empty_list_and_any_number(number):
    phonewords_maker = phonewords()
    wordlist = []
    assert phonewords_maker.list_words(number, wordlist) == [] 


def test_phonewords_should_return_list_when_wordlist_is_single_letter_and_number_matches():
    phonewords_maker = phonewords()
    number = "2"
    wordlist = ["a"]
    assert phonewords_maker.list_words(number, wordlist) == wordlist