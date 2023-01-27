import pytest

from phonewords import phonewords, numberchecker

input_sample_true = [
    ("222","bac"),
    ("3662277", "foobar")
]
@pytest.mark.parametrize("number,word", input_sample_true)
def test_numberchecker_should_return_true_when_given_a_word_which_matches_its_number(number, word):
    number_checker = numberchecker()
    number_checker.add_number(number)
    assert number_checker.check_word(word) == True


input_sample_false = [
    ("222","zzz"),
    ("3662277", "zfoobar")
]
@pytest.mark.parametrize("number,word", input_sample_false)
def test_numberchecker_should_return_false_when_given_a_word_which_matches_its_number(number, word):
    number_checker = numberchecker()
    number_checker.add_number(number)
    assert number_checker.check_word(word) == False 