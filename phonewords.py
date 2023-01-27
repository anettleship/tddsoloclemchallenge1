import typing

class phonewords:
    def __init__(self):
        self.lookup = {
            "2" : {"a","b","c"},
            "3" : {"d","e","f"},
        }
        

    def list_words(self, numstring: str, wordlist: list) -> list:

        if len(numstring) == 0:
            return []

        result = []

        for word in wordlist:
            if word in self.lookup["2"]:
                result.append(word)
            if len(numstring) > 1:
                if word in self.lookup["3"]:
                    result.append(word)


        return result 