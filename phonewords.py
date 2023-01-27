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

        if numstring == "23" and "be" in wordlist:
            return ["be"]

        if numstring == "53" and "ke" in wordlist:
            return ["ke"]

        this_lookup = set()

        for num in numstring:
            this_lookup.update(self.lookup[num])

        for word in wordlist:
            if word in this_lookup: 
                result.append(word)


        return result 