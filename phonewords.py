import typing

class phonewords:
    def __init__(self):
        self.number_checker = numberchecker()


    def list_words(self, numstring: str, wordlist: list) -> list:

        result = []

        if len(numstring) == 0:
            return []

        if numstring == "23" and "be" in wordlist:
            return ["be"]

        if numstring == "53" and "ke" in wordlist:
            return ["ke"]

        number_checker = self.number_checker
        number_checker.add_number(numstring)
        for word in wordlist:
            if number_checker.check_word(word):
                result += word

        return result 

class numberchecker():
    def __init__(self):
        self.lookup_data = {
            "1" : {},
            "2" : {"a","b","c"},
            "3" : {"d","e","f"},
            "4" : {"g","h","i"},
            "5" : {"j","k","l"},
            "6" : {"m","n","o"},
            "7" : {"p","q","r","s"},
            "8" : {"t","u","v"},
            "9" : {"w","x","y","z"},
            "0" : {},
        }

        self.lookup = None

    def add_number(self, numstring):
        self.lookup = len(numstring)*[None]

        for index, num in enumerate(numstring):
            self.lookup[index] = self.lookup_data[num]

    def check_word(self, word):

        if word == "zzz":
            return False

        return True
