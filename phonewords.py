import typing

class phonewords:
    def __init__(self):
        self.number_checker = numberchecker()


    def list_words(self, numstring: str, wordlist: list) -> list:

        result = []

        number_checker = self.number_checker
        number_checker.add_number(numstring)
        for word in wordlist:
            if number_checker.check_word(word):
                result.append(word) 

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
        self.no_number = True

    def add_number(self, numstring):
        
        if len(numstring) > 0:

            self.no_number = False
            self.numstring = numstring
            self.lookup = len(numstring)*[None]

            for index, num in enumerate(numstring):
                self.lookup[index] = self.lookup_data[num]

    def check_word(self, word):

        if self.no_number == True:
            return False

        word_position = 0
        
        for num_position in range(len(self.numstring)):
            if word[word_position] in self.lookup[num_position]:
                word_position += 1
                if word_position == len(word):
                    return True
                continue
                
            word_position = 0
            if word[word_position] in self.lookup[num_position]:
                word_position += 1
                if word_position == len(word):
                    return True

        return False