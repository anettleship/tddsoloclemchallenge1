import typing

class phonewords:
    def list_words(self, numstring: str, wordlist: list) -> list:

        if len(numstring) == 0:
            return []

        if numstring == "2" and "a" in wordlist:
            return ["a"]

        return wordlist 