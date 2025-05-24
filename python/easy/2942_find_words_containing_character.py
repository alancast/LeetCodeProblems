from typing import List


class Solution:
    # Time O(n*m) where n is len words and m is len of each word
    # Space O(1) only thing stored is answer array
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []

        for i, word in enumerate(words):
            for char in word:
                if char == x:
                    answer.append(i)
                    break

        return answer
    
test_cases = [
    [[0,1], ["leet","code"], "e"],
    [[0,2], ["abc","bcd","aaaa","cbc"], "a"],
    [[], ["abc","bcd","aaaa","cbc"], "z"]
]
solution = Solution()
for expected, words, x in test_cases:
    actual = solution.findWordsContaining(words, x)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words: {words}, x: {x}")

print("Ran all tests")