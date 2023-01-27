import typing

class phonewords:
    def list_words(self, numstring: str, wordlist: list) -> list:

        if len(numstring) == 0:
            return []
        
        return wordlist 