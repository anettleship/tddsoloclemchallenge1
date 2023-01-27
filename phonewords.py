import typing

class phonewords:
    def __init__(self):
        self.lookup = {
            "1" : {"d","e","f"},
            "2" : {"a","b","c"},
            "3" : {"d","e","f"},
            "4" : {"d","e","f"},
            "5" : {"d","e","f"},
            "6" : {"d","e","f"},
            "7" : {"d","e","f"},
            "8" : {"d","e","f"},
            "9" : {"d","e","f"},
            "0" : {"d","e","f"},
        }
        

    def list_words(self, numstring: str, wordlist: list) -> list:

              
        result = []

        this_lookup = set()

        for num in numstring:
            this_lookup.update(self.lookup[num])

        for word in wordlist:
            if word in this_lookup: 
                result.append(word)


        return result 