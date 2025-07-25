from collections import defaultdict
from typing import List


class Solution:
    # Create a dict of len, start, final to words
    # Then for each of those entries create a trie with counts
    # Create abbreviations from trie
    # Time O(c) where c is total characters across words (each char operated on)
    # Space O(c) each char also has information stored with it
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        # Groups of len, start, end. If multiple then know overlapping abbrev
        # Create grouping
        groups = defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        # Every word will have 1 entry
        answer = [None] * len(words)


        Trie = lambda: defaultdict(Trie)
        COUNT = False

        # Go over every group and create the abbrevs for each word
        for group in groups.values():
            # Create a Trie for each group
            trie = Trie()
            for word, _ in group:
                cur = trie
                # Update count of each letter in the words
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            # Go over all the words again and append abbreviation to answer
            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    # If this is the only word in the group that has the next
                    # Letter than we have our abbreviation so just quit
                    if cur[COUNT] == 1: 
                        break

                    # Otherwise go down to next letter
                    cur = cur[letter]
                
                # Make sure abbreviation is actually shorter
                if len(word) - i - 1 > 1:
                    answer[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    answer[index] = word
    
        return answer
    
test_cases = [
    [["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"], ["like","god","internal","me","internet","interval","intension","face","intrusion"]],
    [["aa","aaa"], ["aa","aaa"]]
]
solution = Solution()
for expected, words in test_cases:
    actual = solution.wordsAbbreviation(words)
    if set(expected) != set(actual):
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: words: {words}")

print("Ran all tests")