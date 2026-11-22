class Solution:
    # Just go over string once and see if there is a ba ever
    # Time O(n)
    # Space O(1)
    def checkString(self, s: str) -> bool:
        return s.find("ba") == -1

test_cases = [
    [True, "aaabbb"],
    [False, "abab"],
    [True, "bbb"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.checkString(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}")

print("Ran all tests")
