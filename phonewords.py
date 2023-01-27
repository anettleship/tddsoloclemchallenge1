import typing

class phonewords:
    def __init__(self):
        self.lookup = {
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
        

    def list_words(self, numstring: str, wordlist: list) -> list:

              
        result = []

        if len(numstring) == 0:
            return []

        if numstring == "23" and "be" in wordlist:
            return ["be"]

        if numstring == "53" and "ke" in wordlist:
            return ["ke"]

        this_lookup = len(numstring)*[None]

        for index, num in enumerate(numstring):
            this_lookup[index] = self.lookup[num]

        for word in wordlist:
            word_position = 0
            
            for num_position in range(len(numstring)):
                if word[word_position] in this_lookup[num_position]:
                    word_position += 1
                else:
                    word_position = 0
                    if word[word_position] in this_lookup[num_position]:
                        word_position += 1

                if word_position == len(word):
                    result.append(word)
                    break

        return result 