class Solution:
    # Just check to see if a second string of ones is ever started
    # Since it has no leading 0's we know it starts with a 1
    # Time O(n)
    # Space O(1)
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s

test_cases = [
    [False, "1001"],
    [True, "110"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.checkOnesSegment(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
