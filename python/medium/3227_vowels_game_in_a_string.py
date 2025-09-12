class Solution:
    # The only scenario where Alice doesn't win is if there are no vowels
    # If there are an odd number she can take the whole string
    # If there are an even number she can take all but one then win next turn
    # Time O(n) as we go over the string once
    # Space O(1)
    def doesAliceWin(self, s: str) -> bool:
        for char in s:
            # Alphabet guaranteed lowercase
            if char in "aeiou":
                return True

        # No vowels
        return False

test_cases = [
    [True, "leetcoder"],
    [True, "e"],
    [True, "ee"],
    [False, "bcd"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.doesAliceWin(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")