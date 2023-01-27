import typing

class phonewords:
    def __init__(self):
        self.lookup = {
            "2" : {"a","b","c"},
        }
        

    def list_words(self, numstring: str, wordlist: list) -> list:

        if len(numstring) == 0:
            return []

        result = []

        for word in wordlist:
            if word in self.lookup["2"]:
                result.append(word)


        return result 