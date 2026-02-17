class Solution:
    # Can be greedy, just take the first one and every time one switches
    # Time O(n)
    # Space O(1)
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        answer = []

        answer.append(words[0])
        next = groups[0]

        for i in range(1, len(groups)):
            # XOR operation
            if groups[i] ^ next:
                next = groups[i]
                answer.append(words[i])

        return answer

test_cases = [
    [["e","b"], ["e","a","b"], [0,0,1]],
    [["a","b","c"], ["a","b","c","d"], [1,0,1,1]]
]
solution = Solution()
for expected, words, groups in test_cases:
    actual = solution.getLongestSubsequence(words, groups)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words: {words}, groups: {groups}")

print("Ran all tests")
