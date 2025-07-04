from typing import List


class Solution:
    # Apparently you can also do this silly math, good luck figuring that out
    # Time O(logk)
    # Space O(1)
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1

        return chr(ord("a") + (ans % 26))

    # Brute Force exceeds time limit
    def kthCharacter_brute_force(self, k: int, operations: List[int]) -> str:
        word = "a"
        index = 0
        while len(word) < k:
            operation = operations[index]
            if operation == 0:
                word = self._duplicate_word(word)
            else:
                word = self._rotate_and_append_word(word)

            index += 1
        
        return word[k-1]
    
    def _duplicate_word(self, word: str) -> str:
        return word + word
    
    def _rotate_and_append_word(self, word: str) -> str:
        char_map = {'z': 'a'}
        next_word = []

        for char in word:
            if char in char_map:
                next_word.append(char_map[char])
            else:
                next_word.append(chr(ord(char) + 1))

        return word + ''.join(next_word)
    
test_cases = [
    ["a", 5, [0,0,0]],
    ["b", 10, [0,1,0,1]]
]
solution = Solution()
for expected, k, operations in test_cases:
    actual = solution.kthCharacter(k, operations)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: k: {k}, operations: {operations}")

print("Ran all tests")