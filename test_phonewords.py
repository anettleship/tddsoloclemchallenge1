from phonewords import phonewords

def test_phonewords_should_return_empty_list_when_given_empty_list_and_blank_number():
    number = ""
    wordlist = []
    assert phonewords(number, wordlist) == [] 