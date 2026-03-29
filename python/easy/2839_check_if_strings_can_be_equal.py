class Solution:
    # Stupid hard coded problem due to input being only 4 chars
    # Time O(1)
    # Space O(1)
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return ((s1[0] == s2[0] and s1[2] == s2[2]) or
                (s1[0] == s2[2] and s1[2] == s2[0])) and \
               ((s1[1] == s2[1] and s1[3] == s2[3]) or
                (s1[1] == s2[3] and s1[3] == s2[1]))

test_cases = [
    [True, "abcd", "cdab"],
    [False, "abcd", "dacb"]
]
solution = Solution()
for expected, s1, s2 in test_cases:
    actual = solution.canBeEqual(s1, s2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s1: {s1}, s2: {s2}")

print("Ran all tests")
