from collections import defaultdict


class AlphabetSetUnion:
    def __init__(self):
        # The parent of every char
        self.parents = [i for i in range(26)]
    
    def join(self, char1: str, char2: str) -> None:
        parent1 = self.find(char1)
        index1 = ord(parent1) - ord('a')
        parent2 = self.find(char2)
        index2 = ord(parent2) - ord('a')

        # parent2's parent should now be parent1
        if parent1 < parent2:
            self.parents[index2] = index1
        # parent1's parent should now be parent2
        else:
            self.parents[index1] = index2
    
    # Worst case scenario O(26)
    def find(self, char1: str) -> str:
        index = ord(char1) - ord('a')

        while self.parents[index] != index:
            index = self.parents[index]

        return chr(index + ord('a'))

class Solution:
    # Time O(n + m) where n is length of s1 m is length of baseStr
    # Space O(26) just takes up array of size 26
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Populate the set union
        asu = AlphabetSetUnion()
        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]

            asu.join(char1, char2)

        # Build the answer from baseStr
        answer = []
        for char in baseStr:
            answer.append(asu.find(char))

        return ''.join(answer)
    
test_cases = [
    ["makkek", "parker", "morris", "parser"],
    ["hdld", "hello", "world", "hold"],
    ["aauaaaaada", "leetcode", "programs", "sourcecode"]
]
solution = Solution()
for expected, s1, s2, baseStr in test_cases:
    actual = solution.smallestEquivalentString(s1, s2, baseStr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s1: {s1}, s2: {s2}, baseStr: {baseStr}")

print("Ran all tests")