class Solution:
    # Can just do math for it. All you need is length of word
    # Time O(1)
    # Space O(1)
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        max_per = (n - 1) // 8 + 1
        return max_per * (max_per - 1) * 4 + (n - (max_per - 1) * 8) * max_per

test_cases = [
    [5, "abcde"],
    [12, "xycdefghij"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.minimumPushes(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")
