from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = len(words) - 1

        while i > 0:
            if sorted(words[i]) == sorted(words[i-1]):
                words.pop(i)
            i -= 1
        
        return words

test_cases = [
    [["abba","cd"], ["abba","baba","bbaa","cd","cd"]],
    [["a","b","c","d","e"], ["a","b","c","d","e"]]
]
solution = Solution()
for expected, words in test_cases:
    actual = solution.removeAnagrams(words)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: words: {words}")

print("Ran all tests")