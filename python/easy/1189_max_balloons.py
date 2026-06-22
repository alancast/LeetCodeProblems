from collections import Counter


class Solution:
    # Just store the instances of the characters and find min
    # Time O(n)
    # Space O(n)
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(counts["b"], counts["a"], counts["l"]//2, counts["o"]//2, counts["n"])

test_cases = [
    [1, "nlaebolko"],
    [2, "loonbalxballpoon"],
    [0, "leetcode"]
]
solution = Solution()
for expected, text in test_cases:
    actual = solution.maxNumberOfBalloons(text)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: text: {text}")

print("Ran all tests")
