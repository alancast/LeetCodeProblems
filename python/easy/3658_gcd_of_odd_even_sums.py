class Solution:
    # Just a math problem today
    # Time O(1)
    # Space O(1)
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

test_cases = [
    [4,4],
    [5,5]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.gcdOfOddEvenSums(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
