class Solution:
    # Just go over patterns and search for each one
    # Time O(n*m)
    # Space O(1)
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        answer = 0
        for i in patterns:
            if i in word:
                answer +=1

        return answer

test_cases = [
    [True, [2,5,7,8,9,2,3,4,3,1], 3],
    [True, [19,5], 1],
    [False, [1,2,3,4,4,4,4,5,6,7], 5]
]
solution = Solution()
for expected, patterns, word in test_cases:
    actual = solution.numOfStrings(patterns, word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: patterns: {patterns}, word: {word}")

print("Ran all tests")
