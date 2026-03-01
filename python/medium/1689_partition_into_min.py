class Solution:
    # Don't need any more than just max number
    # Time O(n)
    # Space O(1)
    def minPartitions(self, n: str) -> int:
        return int(max(n))

test_cases = [
    [3, "32"],
    [8, "82734"],
    [9, "27346209830709182346"]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.minPartitions(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
