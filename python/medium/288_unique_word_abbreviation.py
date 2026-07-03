from collections import defaultdict


class ValidWordAbbr:
    abbrevs: dict
    words: set

    def __init__(self, dictionary: list[str]) -> None:
        self.abbrevs = defaultdict(int)
        self.words = set()

        for word in dictionary:
            # Make sure not to add duplicate words
            if word in self.words:
                continue

            self.words.add(word)
            length = len(word)
            if length <= 2:  # noqa: PLR2004
                self.abbrevs[word] += 1
            else:
                self.abbrevs[word[0] + str(length - 2) + word[-1]] += 1

    def isUnique(self, word: str) -> bool:
        # Find the words abbreviation
        abbrev = word
        if len(abbrev) > 2:  # noqa: PLR2004
            abbrev = word[0] + str(len(word) - 2) + word[-1]

        # If no word in dictionary with abbreviation it's unique
        if abbrev not in self.abbrevs:
            return True

        # If multiple words have same abbrev then it's not unique
        if self.abbrevs[abbrev] > 1:
            return False

        # If there is 1 word in dictionary with this abbrev, see if it's same word as dict
        # If it is then it's unique, if not, then it's not
        return word in self.words


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
